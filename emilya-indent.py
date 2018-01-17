"""
LESSON: 3.5 - Mouse & Keyboard
EXERCISE: Zen Flycatcher
"""

#### ---- SETUP ---- ####

# --- Libraries --- #

# Import tsk
import tsk
import random
import pygmame
# INITialize pygame
pygame.init()

# Open a WINDOW of size [500, 300] and assign to window
window = pygame.display.set_mode([500,300])

# Assign the variable fly a RECT that starts at 100, 150,
# with height and width 20
fly = pygame.RECT(100,150,20,20)
box = pygame.Rect(200,100,100,100)

# Create variable caught and assign value False
caught = False
done = False
#### ---- MAIN LOOP ---- ####

# Loop while not done and not caught

while not done and not caught:
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == KEYDOWN and event.key == SPACE:
            in_x =(fly.x - box.x >= 0) and (fly.x - box.x <= 80)
            in_y = (fly.y - box.y >= 0) and (fly.y - box.y <= 80)
            if in_x and in_y:
                caught = True

    # Increment fly.x by randint between -5 and 5
    fly.x += random.randint(-5,5)

    # Increment fly.y by randint between -5 and 5
    # ---> TEST AFTER THIS LINE <--- #

    fly.y += random.randint(-5,5)

    # --- Don't let fly leave window --- #

    # If fly.x is less than 0

    if fly.x <0:
        fly.x = 0
        # Assign fly.x the value 0


    # If fly.x is greater than 480
    if fly.x > 480:
        fly.x = 480

        # Assign fly.x the value 480


    # If fly.y is less than 0

    if fly.y <0:
        fly.y = 0
        # Assign fly.y the value 0


    # If fly.y is greater than 280
    if fly.y > 280:
        fly.y = 280

        # Assign fly.y the value 280
        # ---> TEST AFTER THIS LINE <--- #



    # --- Control box --- #

    # If GET_KEY_PRESSED with RIGHT

      if GET_KEY_PRESSED with RIGHT:
            box.x += 2
        # Increment box.x by 2


    # If GET_KEY_PRESSED with LEFT
    if GET_KEY_PRESSED with LEFT:
        box.x -= 2

        # Decrement box.x by 2
        # ---> TEST AFTER THIS LINE <--- #



    # --- Draw frame --- #

    # FILL the window with WHITE
    window.fill((255,255,255))

    # Draw the box RECT with BLACK and a line width
    # of 2
    pygame.draw.rect(window, black, box, 2)

    # Draw the fly ELLIPSE in window with any COLOR
    pygame.draw.ellipse(window, (255,255,0), fly)
    
    # FLIP the display
    pygame.display.flip()

    # WAIT 10 milliseconds
    pygame.time.wait(10)



#### ---- FINAL OUTPUT ---- ####

# If caught


    # Print a congratulations message
    # ---> TEST AFTER THIS LINE <--- #




# Turn in your Coding Exercise.
