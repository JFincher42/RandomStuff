import random
import pygame

pygame.init()
win = pygame.display.set_mode([500, 500])
white = (255,255,255)
black = (40,20,255)
red = (255, 40, 50)

x1 = random.randint(100,400)
y1 = random.randint(100,400)
x2 = random.randint(100,400)
y2 = random.randint(100,400)
radius = 10
x1speed = random.randint(3,8)
y1speed = random.randint(3,8)
x2speed = random.randint(3,8)
y2speed = random.randint(3,8)

while hits>0:
    win.fill(white)
    pygame.draw.circle(win, black, (x1,y1), radius)
    pygame.draw.circle(win, red,   (x2,y2), radius)
    x1+=x1speed
    y1+=y1speed
    x2+=x2speed
    y2+=y2speed
    
    if (x1>=490 or x1<=10):
        x1speed*=-1
        hits-=1
    if (y1>=490 or y1<=10):
        y1speed*=-1
        hits-=1

    if (x2>=490 or x2<=10):
        x2speed*=-1
        hits-=1
    if (y2>=490 or y2<=10):
        y2speed*=-1
        hits-=1

    pygame.display.flip()
    pygame.time.wait(15)
