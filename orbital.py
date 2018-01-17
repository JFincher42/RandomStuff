"""
Orbital

Plots a simple 2D orbit of a satellite around a planetary body

"""

import random                   # Used for a random initial setup of the satellite
import pygame                   # Need PyGame for graphics
import math                     # Math is always good

# Some basic constants
WIDTH = 500                     # Width and height of the window
HEIGHT = 500
CENTERX = int(WIDTH/2)               # Precalc the center point
CENTERY = int(HEIGHT/2)
WHITE = (255,255,255)           # Some basic colors
BLACK = (0,0,0)
RED = (255, 40, 50)
GRAVITY = 1.0                  # Gravity constant to smooth out calculations

# Setup PyGame and give me an initial 500x500 window filled with white
pygame.init()
win = pygame.display.set_mode([WIDTH, HEIGHT])

# The relative masses of the planet and satellite are needed here
massPlanet = 10000
massSat = 10

# Where is the planet
planet = (CENTERX, CENTERY)
planetradius = int(WIDTH/20)

# Where is the satellite
satx = 450                      # Make this random next time
saty = 50
satradius = 5
satellite = (satx, saty)

# Give me a vector, Victor
satVector = (-10, 0)            # This is the force vector for the satellite

# Simple frames counter for now
frames = 0

while frames < 100:
    win.fill(WHITE)                 # Blank the window
    frames += 1                     # Next frame
    
    # Draw the planet
    pygame.draw.circle(win, BLACK, planet, planetradius)

    # Draw the satellite
    pygame.draw.circle(win, RED, satellite, satradius)

    # Figure out the next position
    xdist = satellite[0]-planet[0]
    ydist = satellite[1]-planet[1]
    dist = math.hypot(xdist, ydist)
    force = GRAVITY * (massPlanet*massSat)/(dist*dist)

    satellite = (int(satellite[0]+force), int(satellite[1]+force))
    print("New x: " + str(satellite[0]) + ", new y: " + str(satellite[1]))

    pygame.display.flip()
    pygame.time.wait(20)
