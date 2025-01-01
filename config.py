import pygame
import random

# Configuração da janela
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simulador de Física")
clock = pygame.time.Clock()

# Constantes
G = 6.67430e-11  # Constante gravitacional
scale = 1e9      # Escala de visualização

# Objetos e cores
objects = []
colors = [(random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)) for _ in range(100)]