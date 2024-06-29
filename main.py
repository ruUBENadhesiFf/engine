import pygame
from pygame.locals import *
from variables import * 
import Player, levels

pygame.init()

init = True
if init: continueUpdate = True

def Get_variables():
    keyPressed = pygame.key.get_pressed()
    mouseX, mouseY = pygame.mouse.get_pos()
    mouseRect = pygame.Rect(mouseX, mouseY, 1, 1)

    return keyPressed, mouseRect

def Check_events():
    global continueUpdate, events
    
    #reset
    events = []

    #check
    for e in pygame.event.get():
        events.append(e)
        if e.type==pygame.QUIT:
            continueUpdate = False




clock = pygame.time.Clock()

while continueUpdate:
    keyPressed, mouseRect = Get_variables()
    Check_events()

    screen.fill((0,0,0))

    levels.Levels(events, mouseRect, keyPressed)

    pygame.display.flip()
    clock.tick(fps)
    

pygame.quit()