#collisions map
import pygame
from variables import blockSize, maps, screen

def DrawMapAndCheckCollisions(place, player, objects):
    def CheckCollisions(blockValue, objects, player):

        if (not blockValue == 0 and blockValue < 100):
            if (
                player.x + player.w > x 
                and player.x < x + blockSize 
                and player.y + player.h >= y
                and player.y + player.h < y + player.maxVelocity + 25
                and player.jump == False
            ):
                player.fall = False 
                player.y = y - player.h
                player.velocity = 0

            if (
                player.x + player.w > x 
                and player.x < x + blockSize 
                and player.y < y + blockSize
                and player.y > y + blockSize - 20
            ):
                player.y = y + blockSize
                player.jump=False
                player.fall=True
                player.velocity = 0
            
            if (
                player.x + player.w > x 
                and player.x + player.w < x + 7 + 2
                and player.y + player.h > y 
                and player.y < y + blockSize
            ):
                player.collisions["right"] = True
                player.x = x - player.w

            else: player.collisions["right"] = False

            if (
                player.x < x + blockSize
                and player.x > x + blockSize - 7 - 2
                and player.y + player.h > y 
                and player.y < y + blockSize
            ):
                player.collisions["left"] = True
                player.x = x + blockSize
            else: player.collisions["left"] = False

        if objects:
            for key, value in objects.items():
                if key == "block":
                    rect = pygame.Rect(value[0], value[1], 50, 50)
                    pygame.draw.rect(screen, (50, 50, 50), rect)

                if (
                    player.x + player.w > rect.x
                    and player.x < rect.x + rect.w
                    and player.y + player.h >= rect.y
                    and player.y + player.h < rect.y + player.maxVelocity + 25
                    and player.jump == False
                ):
                    player.fall = False 
                    player.y = rect.y - player.h
                    player.velocity = 0

                if (
                    player.x + player.w > rect.x
                    and player.x < rect.x + rect.w 
                    and player.y < rect.y + rect.h
                    and player.y > rect.y + rect.h  - 20
                ):
                    player.y = rect.y + rect.h
                    player.jump=False
                    player.fall=True
                    player.velocity = 0
                
                if (
                    player.x + player.w > rect.x 
                    and player.x + player.w < rect.x + rect.w + 7
                    and player.y + player.h > rect.y 
                    and player.y < rect.y + rect.h
                ):
                    player.collisions["right"] = True
                    player.x = rect.x - player.w

                else: player.collisions["right"] = False

                if (
                    player.x < rect.x + rect.w
                    and player.x > rect.x + rect.w - 7 - 2
                    and player.y + player.h > rect.y 
                    and player.y < rect.y + rect.h
                ):
                    player.collisions["left"] = True
                    player.x = rect.x + rect.w

                else: player.collisions["left"] = False


    for lineIndex in range(len(maps[place])):
        for blockIndex in range(len(maps[place][lineIndex])):
            x = blockIndex * blockSize
            y = lineIndex * blockSize
            blockValue = maps[place][lineIndex][blockIndex]

            rect = pygame.Rect(x, y, blockSize, blockSize)

            if player.rect.colliderect(rect) and blockValue == 0: player.fall = True

            if blockValue == 4: pygame.draw.rect(screen, (50, 50, 50), rect)
            CheckCollisions(blockValue, objects, player)

    return player