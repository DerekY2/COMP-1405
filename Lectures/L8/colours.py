''' 
    COMP 1005/1405 - Lecture 8 Colours is a pygame program that fills the surface
    with different colours.
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
          
    The colours code has been modified from Dr. Robert Collier's example from 
    the COMP 1005/1405 Fall 2021 course.
    
    Notice that the variable have descriptive names.
'''
# import the pygame module
import pygame

# this creates a surface on which to draw
# the dimensions of this surface are 700 x 700 (n.b. width, height)
drawing_window = pygame.display.set_mode((700, 700))

# Colours are based on the RGB tuple -- as known as red, green and blue
# Each value is between 0 - 255.
# A tuple simialar to a list but it is immutable
# Uncomment the colour you want to fill your surface

# # Black -- background for drawing_window surface
drawing_window.fill((0, 0, 0))

# # Salmon -- You can also enter a Hexadecimal value for a colour.
# drawing_window.fill('#FF9081')

# White -- background for drawing_window surface
# drawing_window.fill((255, 255, 255))

# Red -- background for drawing_window surface
# drawing_window.fill((255, 0, 0))

# # Green -- background for drawing_window surface
# drawing_window.fill((0, 255, 0))

# # Blue -- background for drawing_window surface
# drawing_window.fill((0, 0, 255))

# # Yellow -- background for drawing_window surface
# drawing_window.fill((255, 255, 0))

# Update is required to update the surface with the changes.
pygame.display.update()

# this is a crude way to keep the window open long enough to see it
# after a couple of lectures we will come up with something more sophisticated
# that will repeatedly monitor what the user has done to determine if the close
# button has been pressed (and, if it has, then the program will end)
pygame.time.delay(5000)

# save an image of the surface to a file.
pygame.image.save(drawing_window, "Lectures/L8/img/colours.png")