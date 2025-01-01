import pygame
import random
from objects2 import SpaceObject, create_object
from config import screen, clock, objects

# Inicialização do Pygame
pygame.init()

# Loop principal
running = True
while running:
    # Processamento de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Criar objeto ao clicar
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            create_object(
                x, y, 
                vx=random.uniform(-2, 2), 
                vy=random.uniform(-2, 2), 
                mass=random.uniform(1e10, 1e12), 
                resistencia=random.uniform(1e5, 1e7)
            )

    # Limpar a tela antes de desenhar novamente
    screen.fill((0, 0, 0))  # Cor de fundo preta (ajustar conforme necessário)

    # Atualizar e desenhar objetos
    for obj in objects:
        obj.update()
        obj.draw()

    pygame.display.flip()  # Atualiza a tela

    clock.tick(60)  # Controla a taxa de quadros (FPS)

pygame.quit()