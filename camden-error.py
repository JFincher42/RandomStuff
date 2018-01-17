"""
LESSON: 3.5 - Mouse & Keyboard
EXERCISE: Zen Flycatcher
"""

#### ---- SETUP ---- ####

# --- Libraries --- #

# Import tsk
import tsk

# Import random
import random

# Import PYGAME
import pygame

# INITialize pygame
pygame.init()


# --- Animation variables --- #

# Open a WINDOW of size [500, 300] and assign to window
window = pygame.display.set_mode([500, 300])

# Assign the variable fly a RECT that starts at 100, 150,
# with height and width 20
fly = pygame.Rect(100, 150, 20, 20)

# Assign the variable box a RECT that starts at 200, 100,
# with height and width 100
box = pygame.Rect(200, 100, 100, 100)


# --- Loop variables --- #

# Create variable caught and assign value False
caught = False

# Create variable done and assign value False
done = False


#### ---- MAIN LOOP ---- ####

# Loop while not done and not caught
while not done and not caught:


    # --- Event loop --- #

    # Create an EVENT LOOP that gets all events
    for event in pygame.event.get():

        # If the event TYPE is QUIT
        if event.type == pygame.QUIT:

            # Assign done the value True
            # ---> TEST AFTER THIS LINE <--- #
            done = True


        # --- Spacebar pressed --- #

        # Elif event.type is equal to KEYDOWN
        # and event.key is equal to SPACE
        elif tsk.get_key_pressed(pygame.KEYDOWN) and tsk.get_key_pressed(pygame.K_SPACE): 


            # --- Check if fly is in the box --- #

            # Assign in_x the value False
            in_x = False

           # Assign in_y the value False
            in_y = False
            

            # If fly.x - box.x is greater than or equal to 0
            # and fly.x - box.x is less than or equal to 80
            if fly.x - box.x >= 0 and fly.x - box.x <= 80:

                # Assign in_x the value True
                in_x = True

            # If fly.y - box.y is greater than or equal to 0
            # and fly.y - box.y is less than or equal to 80
            if fly.y - box.y >= 0 and fly.y - box.y <= 80:

                # Assign in_y the value True
                in_y = True

            # If in_x and in_y
            if in_x and in_y:

                # Assign caught the value True
                # ---> TEST AFTER THIS LINE <--- #
                caught = True


    # --- Randomly animate fly --- #

    # Increment fly.x by randint between -5 and 5
    fly.x += random.randint(-5,5)

    # Increment fly.y by randint between -5 and 5
    # ---> TEST AFTER THIS LINE <--- #
    fly.y += random.randint(-5,5)


    # --- Don't let fly leave window --- #

    # If fly.x is less than 0
    if fly.x < 0:

        # Assign fly.x the value 0
        fly.x = 0

    # If fly.x is greater than 480
    if fly.x > 480:

        # Assign fly.x the value 480
        fly.x = 480

    # If fly.y is less than 0
    if fly.y < 0:

        # Assign fly.y the value 0
        fly.y = 0

    # If fly.y is greater than 280
    if fly.y > 280:

        # Assign fly.y the value 280
        # ---> TEST AFTER THIS LINE <--- #
        fly.y = 280


    # --- Control box --- #

    # If GET_KEY_PRESSED with RIGHT
    if tsk.get_key_pressed(pygame.K_RIGHT):
        
        # Increment box.x by 2
        box.x += 2

    # If GET_KEY_PRESSED with LEFT
    if tsk.get_key_pressed(pygame.K_LEFT):

        # Decrement box.x by 2
        # ---> TEST AFTER THIS LINE <--- #
        box.x -= 2


    # --- Draw frame --- #

    # FILL the window with WHITE
    window.fill((255, 255, 255))

    # Draw the box RECT with BLACK and a line width
    # of 2
    box = pygame.draw.rect(window, (0,0,0), box, 2)

    # Draw the fly ELLIPSE in window with any COLOR
    fly = pygame.draw.ellipse(window, (150, 50, 100), fly)

    # FLIP the display
    pygame.display.flip()

    # WAIT 10 milliseconds
    pygame.time.wait(10)



#### ---- FINAL OUTPUT ---- ####

# If caught
if caught:

    # Print a congratulations message
    # ---> TEST AFTER THIS LINE <--- #
    print("You caught it! ")



# Turn in your Coding Exercise.
