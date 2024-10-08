''' 
    COMP 1005/1405 - Lecture 8 Draw and line using pygame
    Name: Sean Benjamin
    Date: October 2, 2024
'''
'''
    Note: changed image save path
            - Derek Yu, 10/07/2024
'''
'''
    Note: You do not need to include these comments in your assignment (but you may).  These comments
          are for educational purposes.
          
    The lines code has been modified from Dr. Robert Collier's example from 
    the COMP 1005/1405 Fall 2021 course.
    
    Notice that the variable have descriptive names.
'''
# import the pygame module
import pygame

# this creates a surface on which to draw
# the dimensions of this surface are 700 x 700 (n.b. width, height)
drawing_window = pygame.display.set_mode((700, 700))

drawing_window.fill((240, 240, 250))

# line(surface, colour_tuple, (startX, startY), (endX, endY))
pygame.draw.line(drawing_window, (0,0,255), (200,0), (200, 700))

# uncomment to draw a red line.  Notice that the colour red can be represented as
# a variable.  The red variable is assigned a tuple that represents red.
# red = (255, 0, 0)
# pygame.draw.line(drawing_window, red, (300,0), (300, 700))

# Update is required to update the surface with the changes.
pygame.display.update()

# this is a crude way to keep the window open long enough to see it
# after a couple of lectures we will come up with something more sophisticated
# that will repeatedly monitor what the user has done to determine if the close
# button has been pressed (and, if it has, then the program will end)
pygame.time.delay(5000)

# save an image of the surface to a file.
pygame.image.save(drawing_window, "Lectures/L8/img/lines.png")