import pygame
from pygame.locals import *
import math

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Estrella con gafas bailando en 3D")

# Colores
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# Función para dibujar una estrella
def draw_star(surface, color, size, position):
    points = []
    for i in range(5):
        angle = math.radians(90 + i * 144)
        x = size * math.cos(angle) + position[0]
        y = size * math.sin(angle) + position[1]
        points.append((x, y))
    pygame.draw.polygon(surface, color, points)

# Función para dibujar las gafas
def draw_glasses(surface, color, size, position):
    pygame.draw.circle(surface, color, (position[0] - size, position[1] + size), size // 2)
    pygame.draw.circle(surface, color, (position[0] + size, position[1] + size), size // 2)

# Loop principal
running = True
clock = pygame.time.Clock()
angle = 0
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Dibujar fondo
    screen.fill(BLACK)

    # Dibujar estrella con gafas
    star_size = 100 + int(50 * math.sin(math.radians(angle)))
    star_position = (width // 2, height // 2)
    draw_star(screen, YELLOW, star_size, star_position)
    draw_glasses(screen, WHITE, star_size // 2, star_position)

    # Actualizar ángulo
    angle += 5

    # Actualizar pantalla
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
