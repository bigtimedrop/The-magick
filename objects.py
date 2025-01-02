import pygame
import random
import math
from config import G, screen, scale, objects, colors

class SpaceObject:
    def __init__(self, x, y, vx, vy, mass, resistencia, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.mass = mass
        self.resistencia = resistencia
        self.color = color

    def draw(self):
        # Desenhar o corpo principal
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.mass**0.3))
        
        # Desenhar esfera de atração
        attraction_radius = self.mass**0.5 * 9  # Ajuste o fator de escala
        pygame.draw.circle(screen, (100, 100, 255), (int(self.x), int(self.y)), int(attraction_radius), 1)

        self.draw_force_vectors()

    def draw_force_vectors(self):
        for obj in objects:
            if obj != self:
                dx, dy = obj.x - self.x, obj.y - self.y
                distance = math.sqrt(dx**2 + dy**2)
                if distance > 0:
                    force = G * self.mass * obj.mass / distance**2
                    fx, fy = (force * dx / distance, force * dy / distance)
                    pygame.draw.line(screen, (255, 0, 0), (self.x, self.y), (self.x + fx * scale, self.y + fy * scale), 1)

    def update(self):
        ax, ay = 0, 0

        for obj in objects:
            if obj != self:
                dx, dy = obj.x - self.x, obj.y - self.y
                distance = math.sqrt(dx**2 + dy**2)

                # Aplicar força gravitacional apenas dentro da esfera de atração
                attraction_radius = self.mass**0.5 * 10
                if distance > 0 and distance <= attraction_radius:
                    force = G * self.mass * obj.mass / distance**2
                    ax += force * dx / distance / self.mass
                    ay += force * dy / distance / self.mass

                # Verificar colisão
                if distance < (self.mass**0.3 + obj.mass**0.3):
                    self.handle_collision(obj)

        self.vx += ax
        self.vy += ay
        self.x += self.vx
        self.y += self.vy

    def handle_collision(self, obj):
        # Calcular velocidade relativa
        relative_velocity = math.sqrt((self.vx - obj.vx)**2 + (self.vy - obj.vy)**2)

        # Se a resistência for menor que a força do impacto, fragmentar
        impact_force = relative_velocity * obj.mass
        if impact_force > self.resistencia:
            self.explode(obj)

    def explode(self, obj):
        num_fragments = random.randint(2, 4)
        for _ in range(num_fragments):
            fragment_mass = self.mass / num_fragments
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(1, 3)
            vx, vy = speed * math.cos(angle), speed * math.sin(angle)
            objects.append(SpaceObject(self.x, self.y, vx, vy, fragment_mass, self.resistencia / num_fragments, random.choice(colors)))

        try:
            objects.remove(self)
            objects.remove(obj)
        except ValueError:
            pass

def create_object(x, y, vx, vy, mass, resistencia):
    color = random.choice(colors)
    objects.append(SpaceObject(x, y, vx, vy, mass, resistencia, color))