## displays smiley face using pygame

import pygame

drawingWindow = pygame.display.set_mode((400, 400))

# define colors
white = (255, 255, 255)
black = (0, 0, 0)
brown = (139 , 69, 19)

drawingWindow.fill(white)

# draw grid
for i in range(20,400,20):
  pygame.draw.line(drawingWindow, black, (0, i), (400, i)) # horizontal line
  pygame.draw.line(drawingWindow, black, (i, 0), (i, 400)) # vertical line

# face - circle
pygame.draw.circle(drawingWindow, black, (200, 200), 100, 3)

# face - eyes
pygame.draw.circle(drawingWindow, black, (160, 170), 11)
pygame.draw.circle(drawingWindow, brown, (160, 170), 10)

pygame.draw.circle(drawingWindow, black, (240, 170), 11)
pygame.draw.circle(drawingWindow, brown, (240, 170), 10)

# face - mouth
# pygame.draw.rect(drawingWindow, brown, (150, 230, 100, 40))
pygame.draw.arc(drawingWindow, black, (150, 220, 100, 50), 3, 0, 4)
 
# update surface
pygame.display.update()

# display drawing for 5000ms
pygame.time.delay(5000)

pygame.image.save(drawingWindow, "Tutorials/T5/img/smile.png")