from tkinter import font
import pygame

def board():
    pygame.init()

    width = 1500
    height = 800
    a_height = height/2 - 10
    white=(255, 255, 255)
    black=(0,0,0)
    red=(255,0,0)

    x1 = width/2
    y1 = a_height

    x1_mudando = 0
    y1_mudando = 0

    perdeu=False

    clock = pygame.time.Clock()

    board=pygame.display.set_mode((width,height))
    board.fill((255, 255, 255))
    
    font_style = pygame.font.SysFont(None, 50)

    pygame.display.update()
    pygame.display.set_caption('snak')
    
    def mensagem(msg, color):
        mnsg= font.render(msg, True, color)
        board.blit(mnsg, [width/2, a_height])

    while not perdeu:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                perdeu = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_mudando = -10
                    y1_mudando = 0
                if event.key == pygame.K_RIGHT:
                    x1_mudando = 10
                    y1_mudando = 0
                if event.key == pygame.K_UP:
                    x1_mudando = 0
                    y1_mudando = -10
                if event.key == pygame.K_DOWN:
                    x1_mudando = 0
                    y1_mudando = 10

            print(event)

        if x1>= width or x1 < 0 or y1 >= height or y1 < 0:
            perdeu=True

        x1 += x1_mudando
        y1 += y1_mudando
        board.fill(white)

        pygame.draw.circle(board, black, [x1, y1], 10, 0)
        pygame.display.update()

        clock.tick(30)


    pygame.quit()        
    quit()