from random import randint

import pygame, sys
import numpy
pygame.init()
size = width, height = 700, 600
x = randint(1, 3)
y = randint(1, 3)
speed = [x, y]
Black = 0, 0, 0
screen = pygame.display.set_mode(size)
pygame.display. set_caption("Mygame")
ball = pygame.image.load("D:/PYG02-ball.gif")
ballrect=ball.get_rect()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    ballrect = ballrect.move(speed[0], speed[1])
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.right > height:
        speed[1] = -speed[1]
    screen.fill(Black)
    screen.blit(ball, ballrect)
    pygame.display.update()



