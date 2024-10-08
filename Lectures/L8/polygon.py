''' 
    COMP 1005/1405 - Lecture 8 Polygon draws a pygame polygon with 5 points 
    represented as (x, y) tuples
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
          
    The polygon code has been modified from Dr. Robert Collier's example from 
    the COMP 1005/1405 Fall 2021 course.
    
    Notice that the variable have descriptive names.
'''

# import the pygame module
import pygame

# this creates a surface on which to draw
# the dimensions of this surface are 700 x 700 (n.b. width, height)
# drawing_window is the variable that contains the surface object
drawing_window = pygame.display.set_mode((700, 700))

# White
# drawing_window.fill(colour_tuple)
drawing_window.fill((255, 255, 255))

# draw.poloygon(surface, colour_tuple, (tuple_of_XYCoordinateTuples))
pygame.draw.polygon(drawing_window, (10, 10, 10), ((100, 140), (120, 120), (130, 160), (120, 200), (110, 180))) 

# uncomment if you want gridline on your surface
# # Draw grid lines on the surface
# for i in range(0,700, 20):
#     # line(surface, colour_tuple, (startX, startY), (endX, endY))
#     pygame.draw.line(drawing_window, (0,0,255), (0,i), (700, i))
#     pygame.draw.line(drawing_window, (0,0,255), (i,0), (i, 700))

# Update is required to update the surface with the changes.
pygame.display.update()

# this is a crude way to keep the window open long enough to see it
# after a couple of lectures we will come up with something more sophisticated
# that will repeatedly monitor what the user has done to determine if the close
# button has been pressed (and, if it has, then the program will end)
pygame.time.delay(5000)

# save an image of the surface to a file.
pygame.image.save(drawing_window, "Lectures/L8/img/polygon.png")