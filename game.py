from calendar import c
import pygame

from pygame.locals import *
from sys import exit
from random import randint

pygame.init()
pygame.display.set_caption("Snake Game")

def armazenar(listc):
    for XeY in listc:
        pygame.draw.rect(tela,(0,255,0),(XeY[0], XeY[1], 20, 20))

def reiniciar():
    global pontuacao,comprimento, xcobra, ycobra, xfruta, yfruta, listc, listpoint,morte
    pontuacao = 0
    comprimento = 5
    xcobra = int(largura/2)
    ycobra = int(altura/2)
    xfruta = randint(40, 600)
    yfruta = randint(50, 430)
    listpoint = []
    listc = []
    morte = False
    
pygame.mixer.music.set_volume(0.1)
trilha = pygame.mixer.music.load('Trilha.mpeg')
som = pygame.mixer.Sound('song.mpeg')
pygame.mixer.music.play(-1)

largura = 640
altura = 480
xcobra = int(largura/2)
ycobra = int(altura/2)
xfruta = randint(40, 600)
yfruta = randint(50, 430)

velocidade = 10
xcontrole = 20
ycontrole = 0
comprimento = 5

pontuacao = 0
fonte = pygame.font.SysFont('arial', 35, True, True)

tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()
listc = []
morte = False

while True:
    relogio.tick(30)
    tela.fill((229,255,204))
    msg = (f"    score: {pontuacao}")
    text = fonte.render(msg, False, (51,102,0))

    for event in pygame.event.get(): #Condição de parada.
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                if xcontrole == velocidade:
                    pass
                else:
                    xcontrole = -20
                    ycontrole = 0
            if event.key == K_d:
                if xcontrole == -velocidade:
                    pass
                else:
                    xcontrole = 20
                    ycontrole = 0
            if event.key == K_w:
                if ycontrole == velocidade:
                    pass
                else:
                    ycontrole = -20
                    xcontrole = 0
            if event.key == K_s:
                if ycontrole == -velocidade:
                    pass
                else:
                    ycontrole = 20
                    xcontrole = 0

    xcobra = xcobra + xcontrole 
    ycobra = ycobra + ycontrole

    cobra = pygame.draw.rect(tela, (255,102,0), (xcobra,ycobra,20,20))  
    fruta = pygame.draw.rect(tela, (153,0,0), (xfruta,yfruta,20,20))

    if cobra.colliderect(fruta): #Colisão.
        xfruta = randint(40, 600)
        yfruta = randint(50, 430)
        pontuacao += 1
        som.play()
        comprimento = comprimento + 1

    listpoint = [] #Armazenar pontos de colisão.
    listpoint.append(xcobra)
    listpoint.append(ycobra)
    listc.append(listpoint)

    if listc.count(listpoint) > 1:
        font = pygame.font.SysFont('arial', 15, True, True)
        mensagem = 'Game over! Press "r" KEY to restart the game.'
        text = font.render(mensagem, True, (255,255,255))
        morte = True

        while morte:
            tela.fill((0,0,0))
            tela.blit(text, (largura//2 - 150, altura//2))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit
                if event.type ==KEYDOWN:
                    if event.key == K_r:
                        reiniciar()

    if len(listc) > comprimento:
        del listc[0]

    armazenar(listc)
    tela.blit(text, (200, 10))
    pygame.display.update() #Atualizar tela.
