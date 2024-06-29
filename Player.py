import pygame
from pygame.locals import *
from variables import screen, infos

class Player:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.w, self.h = 90, 90
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

        self.rowX = 0
        self.rowY = 0
        self.position = "idle"
        self.direction = "right"
        self.timeR = 0
        self.timeL = 0
        self.maxTime = 10

        self.show = True 
        self.canMove = True
        self.speed = 2

        self.collisions = {
            "right": False,
            "left": False,
            "up": False,
            "down": False,
        }

        self.jump = False 
        self.fall = False 
        self.maxVelocity = 15
        self.velocity = 0
        self.jumpSpeed, self.fallSpeed = 1, 1

    def events(self, keyPressed, place):

        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

        def Draw():

            #screen.blit(playeR, self.rect, (self.rowX * self.w, self.rowY * self.h, self.w, self.h))
            pygame.draw.rect(screen, (200, 0, 0), (self.rect))

            if self.direction == "right":
                self.timeL = 0
                self.timeR += 1
                if self.timeR > self.maxTime:
                    self.timeR = 0
                    self.rowX += 1

                if self.position == "idle":
                    self.rowX = 0
                    self.rowY = 0
                elif self.position == "walk":
                    if self.rowX >=21: self.rowX = 0
                    self.rowY = 0

            elif self.direction == "left":
                self.timeR = 0
                self.timeL += 1
                if self.timeL > self.maxTime:
                    self.timeL = 0
                    self.rowX += 1
                    

                if self.position == "idle":
                    self.rowX = 0
                    self.rowY = 1
                elif self.position == "walk":
                    self.rowY = 1
                    if self.rowX >= 21:
                        self.rowX = 0


        def Move():
            if keyPressed[K_q] and not self.collisions["left"]:
                self.x -= self.speed
                self.position = "walk"
                self.direction = "left"
            elif keyPressed[K_d] and not self.collisions["right"]:
                self.x += self.speed
                self.position = "walk"
                self.direction = "right"
            else:
                self.position = "idle"

        def Jump():
    
            self.y -= self.velocity

            if keyPressed[K_z] and not self.jump and not self.fall:   

                self.jump = True
                self.position="idle"

            if self.jump :
                self.fall = False
                if self.velocity < self.maxVelocity:
                    self.velocity += self.jumpSpeed
                else:
                    self.velocity = 0
                    self.jump=False
                    self.fall=True
                
                if keyPressed[K_s]:

                    self.jump = False
                    self.fall = True
                    self.velocity = 0

            elif self.fall:
                self.jump = False
                self.velocity -= self.fallSpeed

                if keyPressed[K_s]:
                    self.y += 3

        if self.show:
            Draw()
        if self.canMove:
            Move()
            Jump()
