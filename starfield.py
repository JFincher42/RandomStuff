"""
LESSON: 4.3 - For Range
EXERCISE: Code Your Own

TITLE: [Your Title Here]
DESCRIPTION: [Your Description Here]
"""
import random
import math
import pygame

pygame.init()

# Set the window width and height here - everything is based on this
WIDTH = 600
HEIGHT = 600

w = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()

# Find the center of the window
centerx = WIDTH/2
centery = HEIGHT/2

# List of star points
stars = []
STARCOUNT = 125

# Each star consists of three numbers:
# * An angle in radians which determines the path,
# * A distance from the center, and
# * A random step it takes each frame
#
# Each star is a list of these three numbers, and we create a list of STARCOUNT of them
for i in range(STARCOUNT):
    x = random.uniform(-math.pi, math.pi)       # The full unit circle
    y = random.randint(5,15)                    # A random starting point
    step = random.randint(2,4)                  # A random step
    stars.append([x,y,step])                    # Append the new star

# Normal game loop here
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the window with dark blue
    w.fill((0,0,80))

    # Loop through the list of stars and do the following:
    # * Move each star by it's random step
    # * If it's off the screen, then regenerate it at the start
    # * Else draw the star
    for star in stars:
        # Move the star
        star[1] += star[2]

        # Figure out the x and y position
        xpos = int(math.cos(star[0])*star[1] + centerx)
        ypos = int(math.sin(star[0])*star[1] + centery)

        # Let's adjust the speed so it speeds up as it approaches the edge
        xdist = xpos-centerx
        ydist = ypos-centery
        hyp = int(math.hypot(xdist,ydist)*10/(WIDTH+HEIGHT))
        star[2] += int(hyp*(WIDTH+HEIGHT)/((WIDTH+HEIGHT)/2))

        # If it's off the screen, regenerate it
        if (xpos>WIDTH or xpos<0) or (ypos>HEIGHT or ypos<0):
            star[0] = random.uniform(-math.pi, math.pi)
            star[1] = random.randint(5,15)
            star[2] = random.randint(2,6)

        # Else, draw it
        else:
            # First, figure out the color - it's greyer the closer to center it is
            # This is done so they tend to fly in rather than just appear
            color = int(star[1]*255/30)
            if color>255:
                color=255

            # Next, figure out the size - it's bigger the further out it gets
            # This gives us the illusion of flyng through
            size =int(hyp*1.3)
            if size<1:
                size = 1

            # Now draw it
            pygame.draw.circle(w, (color,color,color), (xpos, ypos), size)
    
    # Flip the display and setup our framerate
    pygame.display.flip()
    clock.tick(30)
