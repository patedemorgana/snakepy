import pygame
import time
import random
import variables

pygame.init()
pygame.display.set_caption('snak')

def cobrinha(movimento, snake_list):
    for x in variables.lista_da_cobrinha:
        pygame.draw.rect(variables.board, variables.preto, [x[0], x[1], variables.movimento, variables.movimento] )

 
def message(msg, color):
    mesg = variables.fonte.render(msg, True, color)
    variables.board.blit(mesg, [variables.width/4, variables.height/2])
 
 
def loop(): 
    while not variables.fechar:
 
        while variables.perder == True:
            variables.board.fill(variables.branco)
            message("perdeu ruinzao! aperta Q-quitar ou C-perder de novo", variables.vermelho)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        variables.fechar = True
                        variables.perder = False
                    if event.key == pygame.K_c:
                        loop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                variables.fechar = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    variables.x1_mudando = -variables.movimento
                    variables.y1_mudando = 0
                elif event.key == pygame.K_RIGHT:
                    variables.x1_mudando = variables.movimento
                    variables.y1_mudando = 0
                elif event.key == pygame.K_UP:
                    variables.y1_mudando = -variables.movimento
                    variables.x1_mudando = 0
                elif event.key == pygame.K_DOWN:
                    variables.y1_mudando = variables.movimento
                    variables.x1_mudando = 0
 
        if variables.x1 >= variables.width or variables.x1 < 0 or variables.y1 >= variables.height or variables.y1 < 0:
            variables.perder = True
 
        variables.x1 += variables.x1_mudando
        variables.y1 += variables.y1_mudando
        variables.board.fill(variables.branco)
        pygame.draw.rect(variables.board, variables.azul, [variables.comidinhax, variables.comidinhay, variables.movimento, variables.movimento])
        variables.cabeça_da_cobrinha.append(variables.x1)
        variables.cabeça_da_cobrinha.append(variables.y1)
        variables.lista_da_cobrinha.append(variables.cabeça_da_cobrinha)
        if len(variables.lista_da_cobrinha) > variables.comprimento_da_cobrinha:
            del variables.lista_da_cobrinha [0]

        for x in variables.lista_da_cobrinha[:-1]:
            if x == variables.cabeça_da_cobrinha:
                perder = True

        cobrinha(variables.movimento, variables.lista_da_cobrinha)
        
        pygame.display.update()

        if variables.x1 == variables.comidinhax and variables.y1 == variables.comidinhay:
            variables.comprimento_da_cobrinha += 1

        variables.timer.tick(variables.velocidade)
 
    pygame.quit()
    quit()
 

