import random
import pygame

pygame.init()
win = pygame.display.set_mode([800, 300])
white = (255,255,255)
black = (40,20,255)
red = (255, 40, 50)

x_speed = 3
y_speed = 3
y_speed_increment = 1

ball_x = 0
ball_y = 0

ceiling_y = 0
floor_y = 285
ceiling_increment = 100
max_y = 0

while ball_x < 800:
    ball_x += x_speed
    ball_y += y_speed
    y_speed += y_speed_increment
    if ball_y >= floor_y:
        y_speed = int(y_speed * -0.9)

    win.fill(white)
    pygame.draw.circle(win, red, (ball_x, ball_y), 15)
    pygame.display.flip()
    pygame.time.wait(20)