import pygame
import math
import sys


def beating_heart():
    pygame.init()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    scale = 10
    beat_speed = 0.05
    time = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        time += beat_speed
        current_scale = scale * (1 + 0.1 * math.sin(time * 5))

        points = []
        for angle in range(0, 360, 5):
            rad = math.radians(angle)
            x = 16 * math.sin(rad) ** 3
            y = 13 * math.cos(rad) - 5 * math.cos(2 * rad) - 2 * math.cos(3 * rad) - math.cos(4 * rad)
            points.append((width // 2 + x * current_scale, height // 2 - y * current_scale))

        pygame.draw.polygon(screen, (255, 0, 0), points)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


beating_heart()