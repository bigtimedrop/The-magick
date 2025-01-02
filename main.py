import pygame
import random
from objects2 import create_object
from config import screen, clock, objects

# Inicialização do Pygame
pygame.init()

# Variável de controle do loop principal
running = True

while running:
    # Processamento de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Criação de objeto ao clicar
            x, y = pygame.mouse.get_pos()
            create_object(
                x=x,
                y=y,
                vx=random.uniform(-2, 2),
                vy=random.uniform(-2, 2),
                mass=random.uniform(1e10, 1e12),
                resistencia=random.uniform(1e5, 1e7)
            )

    # Limpeza da tela
    screen.fill((0, 0, 0))  # Fundo preto

    # Atualização e renderização dos objetos
    for obj in objects:
        obj.update()  # Atualiza posição e verifica colisões
        obj.draw()    # Renderiza o objeto na tela

    # Atualização da tela
    pygame.display.flip()

    # Controle de taxa de quadros
    clock.tick(60)

pygame.quit()
