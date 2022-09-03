from tkinter import font
import time
import pygame
from variables import *

def board():
    pygame.init()

    pygame.display.update()
    pygame.display.set_caption('snak')
    
    def mensagem(msg, color):
        mnsg= font_style.render(msg, True, color)
        board.blit(mnsg, [width/3, height/3])

    def loop():
        perdeu = False

    while not perdeu:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                perdeu = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_mudando = -movimento
                    y1_mudando = 0
                if event.key == pygame.K_RIGHT:
                    x1_mudando = movimento
                    y1_mudando = 0
                if event.key == pygame.K_UP:
                    x1_mudando = 0
                    y1_mudando = -movimento
                if event.key == pygame.K_DOWN:
                    x1_mudando = 0
                    y1_mudando = movimento

            print(event)

        if x1>= width or x1 < 0 or y1 >= height or y1 < 0:
            perdeu=True

        x1 += x1_mudando
        y1 += y1_mudando
        board.fill(white)

        pygame.draw.circle(board, black, [x1, y1], 10, 0)
        pygame.display.update()

        clock.tick(velocidade_da_cobrinha)

    mensagem("perdeu ruinzao", red)
    pygame.display.update()
    time.sleep(2)

    pygame.quit()        
    quit()