import pygame
import random

pygame.init()

# Setup some colors
tree = (10,180,50)
trunk = (100, 50, 80)
sky = (0, 120, 180)
snow = (255,255,255)
mountains = (180, 180, 180)
forest = (5, 150, 50)

RED   = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 240, 180)
BLUE = (0, 0, 255)

scale = 1
width = 160
height = 140

w = pygame.display.set_mode([width*scale, height*scale])
c = pygame.time.Clock()

# Setup some snow to fall
snowflake_count = 40
snowflakex = [0]*snowflake_count
snowflakey = [0]*snowflake_count
snowflake_speed = [0]*snowflake_count
snowflake_jitter = [0]*snowflake_count
for i in range(snowflake_count):
    snowflakex[i] = random.randint(-10,170)
    snowflakey[i] = random.randint(-50, -5)
    snowflake_speed[i] = random.randint(1,3)
    snowflake_jitter[i] = random.randint(-1,1)

# And setup some lights on the tree with random flash times

lights = [(75, 40), (70, 60), (80, 70), (60, 80), (70, 90), (90, 90)]
light_colors = [YELLOW, RED, GREEN, BLUE, RED, BLUE]
light_size = [4, 2, 2, 2, 2, 2]
light_draw = [True, False, True, True, False, False]
light_time = [0]*6
for i in range(6):
    light_time[i] = random.randint(1000,2000)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the background
    w.fill(sky)

    # draw the mountains
    mp = [(0,100), (10,90), (15, 100), (25, 80), (50, 140), (0, 140)]
    pygame.draw.polygon(w, mountains, mp)

    # draw background trees
    btp = [(120,140), (120,110), (130,90), (135,95), (143, 80), (147, 88), (155, 85), (160,100), (160, 140)]
    pygame.draw.polygon(w, forest, btp)

    # Draw the foreground tree
    trp = [(50,100), (60,80), (55,80), (70,60), (65,60), (75,40), (85,60), (80,60),(95,80),(90,80),(100,100)]
    trup = [(70,100),(80,100),(80,110),(70,110)]
    pygame.draw.polygon(w, trunk, trup)
    pygame.draw.polygon(w, tree, trp)

    # Draw the foreground snow
    fg = [(0,120),(30,120),(70,110),(120,110),(160,100), (160,140), (0,140)]
    pygame.draw.polygon(w, snow, fg)

    # Draw the falling snow
    for i in range(snowflake_count):
        pygame.draw.circle(w, snow, (snowflakex[i], snowflakey[i]), random.randint(1,2))
        # Update the position
        snowflakex[i] += snowflake_jitter[i]
        if (snowflakex[i] > 180 or snowflakex[i] < -20):
            snowflakex[i] = random.randint(0,160)
            snowflakey[i] = random.randint(-20, -5)
            
        snowflakey[i] += snowflake_speed[i]
        if (snowflakey[i] > 140):
            snowflakey[i] = random.randint(-20, -5)
            snowflake_speed[i] = random.randint(1,3)

        snowflake_jitter[i] = random.randint(-1,1)

    # Flashing lights
    for i in range(6):
        if light_draw[i]:
            pygame.draw.circle(w, light_colors[i], lights[i], light_size[i])
        light_time[i]-=c.get_time()
        if (light_time[i]<=0):
            light_time[i]=random.randint(1000,2000)
            light_draw[i] = not light_draw[i]

    pygame.display.flip()
    c.tick(30)
