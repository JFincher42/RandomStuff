"""
Neptune Animation
"""
# Setup
import math
import pygame
pygame.init()
 
# Open Window
window = pygame.display.set_mode([600, 400])
window.fill((255, 255, 255))
 
# Variables
black = (0,0,0)
blue = (0,0,255)
white = (255,255,255)
circa = 0
 
# Loop
while circa <= 360:                                 #(while True, infinite loop)
    window.fill(black)
    
    # Draw planet
    pygame.draw.circle(window,blue,(300,200),100)
    
    # Animation of moon
    x = int(300 + 100*math.cos(2*math.pi*circa/360))
    y = int(200 + 100*math.sin(2*math.pi*circa/360))
               
    pygame.draw.circle(window,white,(x,y),10)
    circa += 10
    
    # Display
    pygame.display.flip()
    pygame.time.wait(50)
input("Hit enter to close window")
