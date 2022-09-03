import pygame

def board():
    pygame.init()
    dis=pygame.display.set_mode((400,300))
    pygame.display.update()
    pygame.display.set_caption('snak')
    perdeu=False
    while not perdeu:
        for event in pygame.event.get():
            print(event)
    pygame.quit()        
    quit()