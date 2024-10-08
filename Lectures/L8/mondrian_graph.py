''' 
    COMP 1005/1405 - Lecture 8 Mondrian picture using pygame shapes
    Name: Sean Benjamin
    Date: October 2, 2024
'''
'''
    Note: changed iamge save path
            - Derek Yu, 10/07/2024
'''
'''
    Note: You do not need to include these comments in your assignment (but you may).  These comments
          are for educational purposes.
          
    The modrian_graph code has been modified from Dr. Robert Collier's example from 
    the COMP 1005/1405 Fall 2021 course.
    
    Notice that the variable have descriptive names.
'''

# this will import the functions from the pygame library
# you will need to precede calls to these functions with "pygame."
import pygame

# this creates a surface on which to draw
# the dimensions of this surface are 700 x 700 (n.b. width, height)
drawing_window = pygame.display.set_mode((700, 700))

# this will fill the surface with a colour that is almost white
drawing_window.fill((240, 240, 250))

# this will draw the large red rectangle
pygame.draw.rect(drawing_window, (220, 40, 30), (175, 0, 525, 500))

# this will draw the blue rectangle in the bottom left
pygame.draw.rect(drawing_window, (0, 90, 150), (0, 525, 150, 175))

# this will draw the small gold rectangle in the bottom right
pygame.draw.rect(drawing_window, (230, 220, 100), (650, 625, 50, 75))

# this will draw a large (and complicated polygon) that is all the black areas of the composition
pygame.draw.polygon(drawing_window, (10, 10, 10), ((150, 0), (175, 0), (175, 500), (700, 500), (700, 525), (650, 525), (650, 600), (700, 600), (700, 625), (650, 625), (650, 700), (625, 700), (625, 525), (175, 525), (175, 700), (150, 700), (150, 525), (0, 525), (0, 500), (150, 500), (150, 250), (0, 250), (0, 200), (150, 200)))


# this actually updates the screen with what you have drawn
pygame.display.update()

# this is a crude way to keep the window open long enough to see it
# after a couple of lectures we will come up with something more sophisticated
# that will repeatedly monitor what the user has done to determine if the close
# button has been pressed (and, if it has, then the program will end)
pygame.time.delay(5000)

# save an image of the surface to a file.
pygame.image.save(drawing_window, "Lectures/L8/img/mondrian.png")