"""
LESSON: 3.6 - Time
EXERCISE: Sunrise Timer
"""

#### ---- SETUP ---- ####

# --- Libraries --- #
import pygame
pygame.init()

w = pygame.display.set_mode([200,600])
# --- User input --- #
#seconds = int(input("How many seconds should the sunrise take? "))
seconds = 10
milliseconds = seconds * 1000


# --- Variables --- #
c = pygame.time.Clock()
running = True
timer = 0
sun_y = 600
b = 0
start = pygame.time.get_ticks()
#### ---- MAIN LOOP ---- ####
while running:
    
    # --- Event loop --- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Quit when time is up --- #
    now = pygame.time.get_ticks()
    if (now-start) >= milliseconds:
        running = False
        
    # --- Move sun --- #
    #sun_y -= (500/seconds)
    sun_y -= (500/milliseconds)*30
    sun_yy = int(sun_y)
    # --- Calculate sky color --- #
    b += int(500/milliseconds)
    if b >= 255:
        b = 255

    # --- Draw frame --- #
    w.fill((0,0,b))
    sun = pygame.draw.circle(w, (220,220,0), (100,sun_yy), 50)

    # --- Finish --- #

    c.tick(30)
    pygame.display.flip()
