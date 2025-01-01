import math

G = 6.67430e-11  # Constante gravitacional simulada (ajustada para escala)

def apply_physics(objects, dt, width, height):
    for obj in objects:
        # Atualizar posição
        obj.x += obj.vx * dt
        obj.y += obj.vy * dt

        # Verificar colisão com bordas (parede invisível no espaço)
        if obj.x - obj.radius < 0 or obj.x + obj.radius > width:
            obj.vx *= -1
            obj.x = max(obj.radius, min(width - obj.radius, obj.x))

        if obj.y - obj.radius < 0 or obj.y + obj.radius > height:
            obj.vy *= -1
            obj.y = max(obj.radius, min(height - obj.radius, obj.y))

    # Aplicar gravidade entre objetos
    for i, obj1 in enumerate(objects):
        for j, obj2 in enumerate(objects[i + 1:], start=i + 1):
            apply_gravity(obj1, obj2)

    # Resolver colisões entre objetos
    for i, obj1 in enumerate(objects):
        for j, obj2 in enumerate(objects[i + 1:], start=i + 1):
            handle_collision(obj1, obj2)

def apply_gravity(obj1, obj2):
    # Vetor de distância entre os objetos
    dx = obj2.x - obj1.x
    dy = obj2.y - obj1.y
    distance = math.sqrt(dx**2 + dy**2)

    if distance < obj1.radius + obj2.radius:  # Evitar comportamento estranho em colisões
        return

    # Força gravitacional
    force = G * (obj1.mass * obj2.mass) / distance**2

    # Componentes da força
    fx = force * (dx / distance)
    fy = force * (dy / distance)

    # Aplicar aceleração (F = m * a -> a = F / m)
    obj1.vx += fx / obj1.mass
    obj1.vy += fy / obj1.mass
    obj2.vx -= fx / obj2.mass
    obj2.vy -= fy / obj2.mass

def handle_collision(obj1, obj2):
    # Distância entre os centros
    dx = obj2.x - obj1.x
    dy = obj2.y - obj1.y
    distance = math.sqrt(dx**2 + dy**2)

    # Verificar colisão
    if distance < obj1.radius + obj2.radius:
        # Resolver sobreposição
        overlap = obj1.radius + obj2.radius - distance
        angle = math.atan2(dy, dx)
        obj1.x -= overlap * math.cos(angle) / 2
        obj1.y -= overlap * math.sin(angle) / 2
        obj2.x += overlap * math.cos(angle) / 2
        obj2.y += overlap * math.sin(angle) / 2

        # Resolver velocidades após colisão
        normal_x = dx / distance
        normal_y = dy / distance

        relative_vx = obj2.vx - obj1.vx
        relative_vy = obj2.vy - obj1.vy
        dot_product = relative_vx * normal_x + relative_vy * normal_y

        if dot_product > 0:
            return

        impulse = 2 * dot_product / (obj1.mass + obj2.mass)
        impulse_x = impulse * normal_x
        impulse_y = impulse * normal_y

        obj1.vx += impulse_x * obj2.mass
        obj1.vy += impulse_y * obj2.mass
        obj2.vx -= impulse_x * obj1.mass
        obj2.vy -= impulse_y * obj1.mass