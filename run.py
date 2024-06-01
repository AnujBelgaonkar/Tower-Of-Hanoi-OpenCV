import pygame
import traceback

width = 1250
height = 720

pygame.init() ## initialize pygame
screen = pygame.display.set_mode((width,height)) ## set window size
pygame.display.set_caption("Tower of Hanoi")
running = True
clock = pygame.time.Clock() ## Clock object to control framerate
## base = pygame.Surface((width,height/4)) # defining the base for towers.
## base.fill('white')
base = pygame.image.load('graphics/base.jpg')
try:
    while running:
        for event in pygame.event.get(): # checks all user events.
            if event.type == pygame.QUIT: 
                running = False
        screen.blit(base,(0,4*height/5)) # attach base surface on the screen. top left point of base gets coordinates (0,3*height/4).
        pygame.display.update() # .update can be used to update whole sceen if no arguments are passed. # Use .update when updating a portion of screen
                                # the portion can be a rectangle. # Use .flip when updating the whole screen.
        clock.tick(60) ## ensures the while loop dosen't run more than 60 times in a second
except Exception as e:
    print(e)
    print(traceback.format_exc())
finally:
    pygame.quit() # uninitialize pygame
