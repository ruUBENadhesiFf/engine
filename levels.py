#levels
import pygame, Player
from DrawMapAndCheckCollisions import DrawMapAndCheckCollisions
from variables import *
from Button import Button_

player = Player.Player(200, 200)

def Button(x, y, txt, action, mouseRect, w=250, h=75, image = None, frames = 0, text_color = (255, 255, 255), color1 = (40, 40, 40), color2 = (65, 65, 65)):

    action = Button_(x, y, txt, action, mouseRect, w=250, h=75, image = None, frames = 0, text_color = (255, 255, 255), color1 = (40, 40, 40), color2 = (65, 65, 65))
    if action: exec(action, globals())
           

def Levels(events, mouseRect, keyPressed):
    global place, player

    def Homepage():
        global place
        Button(200, 200, "Play", "place='level1'", mouseRect)
        
    def Level1():
        global place, player
        objects = {}
        player = DrawMapAndCheckCollisions(place, player, objects)
        player.events(keyPressed, place)
        

    fction = str(place).capitalize() + "()"
    exec(fction)