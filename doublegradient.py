"""
LESSON: 3.2 - Shapes & Color
EXERCISE: Code Your Own

TITLE: [Your Title Here]
DESCRIPTION: [Your Description Here]
"""
import pygame
import random
import math

pygame.init()
w = pygame.display.set_mode([510, 510])
w.fill((255,255,255))

var = random.randint(0,255)
which = random.randint(1,3)

def getColor(num1, num2, which):
    if which == 1:
        return (var, num1, num2)
    if which == 2:
        return (num1, var, num2)
    return (num1, num2, var)
"""
num1 = 0
num2 = 0
while num1 < 255:
    num2 = 255
    while num2 > 0:
        color = getColor(num1, num2, which)
        r = pygame.Rect(num1*2, (255-num2)*2, 2, 2)
        pygame.draw.rect(w, color, r)
        pygame.display.flip()
        num2 -= 1
    num1 += 1
"""
pygame.display.flip()

len = 0
degree = 0
loop = 0
while loop < 20:
    while len < 510:
        rad = math.radians(degree)
        x = math.cos(rad) * len
        y = math.sin(rad) * len
        x = x + 255
        y = -y + 255
        pygame.draw.line(w, (len/2,127,200), (255, 255), (x,y), 1)
        degree += 1
        if degree == 360:
            degree = 0
        len += 3
        pygame.display.flip()

    while len > 0:
        rad = math.radians(degree)
        x = math.cos(rad) * len
        y = math.sin(rad) * len
        x = x + 255
        y = -y + 255
        pygame.draw.line(w, (80,200,len/2), (255, 255), (x,y), 1)
        degree += 1
        if degree == 360:
            degree = 0
        len -= 2
        pygame.display.flip()

    loop += 1


x = 255
while x > 0:
    pygame.draw.circle(w, (x, 0, 0), (255, 255), x)
    
    x-=1

    pygame.display.flip()
input()

