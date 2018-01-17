import pygame
import math
pygame.init()

win=pygame.display.set_mode([500,500])
win.fill((255,255,255))

width = win.get_width()
height = win.get_height()

center_x = width//2
center_y = height//2

spacing_x = 10
spacing_y = 10
mult_x = .5
mult_y = -.5

max_x = mult_x*(width - center_x) / spacing_x
min_x = mult_x*(center_x - width) / spacing_x

max_y = mult_y*(height - center_y) / spacing_y
min_y = mult_y*(center_y - height) / spacing_y

last_x = 0
last_y = 0
first = True

pygame.draw.line(win, (0,0,0), (0, center_y), (width, center_y), 1)
pygame.draw.line(win, (0,0,0), (center_x, 0), (center_x, height), 1)
pygame.display.flip()

for x in range(width):
    scale_x = mult_x*(x - center_x) / spacing_x
    scale_y = math.sin(scale_x)
    y = (scale_y * spacing_y / mult_y) + center_y

    if not first:
        pygame.draw.line(win, (0,0,0), (last_x, last_y), (x,y), 1)
    last_x = x
    last_y = y
    first = False
    pygame.display.flip()

input()