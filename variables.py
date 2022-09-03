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

thing = False
perdeu=False

movimento = 10
velocidade_da_cobrinha=30
clock = pygame.time.Clock()

board=pygame.display.set_mode((width,height))
board.fill((255, 255, 255))
font_style = pygame.font.SysFont(None, 50)

comidinhax = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
comidinhay = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0