import pygame
pygame.init()
window = pygame.display.set_mode([500,500])

x_speed = 7
y_speed = 3
b_x = 15
b_y = 15

frames = 0

while frames < 750:
    frames += 1

    b_x += x_speed
    b_y += y_speed

    if b_x >= 485:
        b_x = 15
    elif b_x <= 15:
        b_x = 485

    if b_y >= 485:
        b_y = 15
    elif b_y <= 15:
        b_y = 485

    window.fill((255,255,255))
    pygame.draw.circle(window, (255,0,0), (b_x, b_y), 15)
    pygame.display.flip()
    pygame.time.wait(10)