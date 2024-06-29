import pygame
from variables import screen, arial

def Button_(x, y, txt, action, mouseRect, w=250, h=75, image=None, frames=0, text_color=(255, 255, 255), color1=(40, 40, 40), color2=(65, 65, 65)):
    rect = pygame.Rect(x, y, w, h)
    text = arial.render(str(txt), True, text_color)
    if not mouseRect.colliderect(rect):
        if image is None: 
            pygame.draw.rect(screen, color1, rect)
        screen.blit(text, (x + w/2 - text.get_width()/2, y + h/2 - text.get_height()/2))
    else:
        if image is None: 
            pygame.draw.rect(screen, color2, rect)
            pygame.draw.rect(screen, (120, 110, 90), rect, 3)
            screen.blit(text, (x + w/2 - text.get_width()/2, y + h/2 - text.get_height()/2))

        if pygame.mouse.get_pressed()[0]:
            return action
        
    return None
