import pygame
pygame.init()

#### -------------------------- ####
#### ---- CIRCLES FUNCTION ---- ####
#### -------------------------- ####

# Add a flag parameter
def circles(window, corner, flag):                            

    if corner == 1:
        x = 100
        y = 100
        modify_x = 100
        modify_y = 100

    elif corner == 2:
        x = 400
        y = 100
        modify_x = -100
        modify_y = 100

    elif corner == 3:
        x = 400
        y = 400
        modify_x = -100
        modify_y = -100

    elif corner == 4:
        x = 100
        y = 400
        modify_x = 100
        modify_y = -100

    # Draw circles
    size = 120
    for i in range(5):

        # Draw regular circle or outline
        if flag:
            pygame.draw.circle(window, (0, 0, 255), (x, y), size, 2) 
        else:
            pygame.draw.circle(window, (0, 0, 255), (x, y), size) 

        x += modify_x
        y += modify_y
        size -= 20


#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####
w = pygame.display.set_mode([500, 500])

start_val = 100
flag = True
start = 0

# Main loop
drawing = True
while drawing:

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    # Draw frame
    w.fill((0, 0, 0))

    # Add flag argument
    circles(w, start + 1, flag)                               

    # Change the style and location of next group
    flag = not flag
    start = ((start + 1) % 4)

    # Finish frame
    pygame.display.flip()
    pygame.time.wait(1000)
