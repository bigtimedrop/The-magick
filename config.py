import pygame

# Configuração da tela
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simulador de Física")
clock = pygame.time.Clock()

# Constante gravitacional
G = 6.67430e-11

# Escala para desenhar forças
scale = 0.1

# Lista de objetos
objects = []

# Cores aleatórias
colors = [
    (255, 0, 0),  # Vermelho
    (0, 255, 0),  # Verde
    (0, 0, 255),  # Azul
    (255, 255, 0),  # Amarelo
    (255, 0, 255),  # Magenta
    (0, 255, 255),  # Ciano
]
