"""
LESSON: 3.2 - Shapes & Color
EXERCISE: Code Your Own

TITLE: [Your Title Here]
DESCRIPTION: [Your Description Here]
"""

import pygame
import random
import math
import time

pygame.init()
w = pygame.display.set_mode([500, 500])

x = 0
while x<255:
    color = (x, 120, 50)
    deg = math.radians(x)
    center_x = int(math.cos(x)*x) + 250
    center_y = int(-math.sin(x)*x) + 250
    pygame.draw.circle(w, color, (center_x, center_y), 5)
    pygame.display.flip()
    x+=1
    time.sleep(.05)

input()










# Turn in your Coding Exercise.
