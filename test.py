import pygame
import math

pygame.init()

display_width = 800
display_height = 600


gameDisplay = pygame.display.set_mode((display_width,display_width))
pygame.display.set_caption('A bit racey')

black = (0,0,0)
white = ( 255,255,255)

clock = pygame.time.Clock()
crashed = False
ballImg = pygame.image.load('Intro_ball.gif')

def ball(x,y):
    gameDisplay.blit(ballImg, (x,y))

x = (display_width * 0.45)
y = (display_height * 0.8)

x_change = 0
deltatime = 0
getTicksLastFrame = 0

step = 0
amplitude = 100
offset = 300

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            x_change = -5
        else:
            x_change = 0

    gameDisplay.fill(black)
     
    x = offset + math.cos(step) * amplitude
    y = offset + math.sin(step) * amplitude

    ball(x, y)

    step += 0.02

    pygame.display.update()
    deltatime = clock.tick(60)

pygame.quit()
quit()