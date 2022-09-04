import time
import pygame
from variables import *
import random

pygame.init()

branco = (255, 255, 255)
amarelo = (255, 255, 102)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
green = (0, 255, 0)
azul = (0, 0, 255)


width = 400
height = 300
a_height = height/2 - 10

board = pygame.display.set_mode((width, height))

timer = pygame.time.Clock()
 
movimento = 10
velocidade = 10
lista_da_cobrinha = []
comprimento_da_cobrinha = 1
cabeça_da_cobrinha = []
gambiarra = []

fonte_placar = pygame.font.SysFont("comicsansms", 35)
fonte = pygame.font.SysFont(None, 30)

fechar = False
perder = False

x1 = width / 2
y1 = height / 2

x1_mudando = 0
y1_mudando = 0

comidinhax = round(random.randrange(10, width - movimento) / 10.0) * 10.0
comidinhay = round(random.randrange(10, width - movimento) / 10.0) * 10.0
