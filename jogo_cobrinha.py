import pygame
from pygame.locals import *
from random import randint


def colocar_rato_aqui():
    x = randint(0, 590)
    y = randint(0, 590)
    return x//10 * 10, y//10 * 10


def colisao(cabeca, rato):
    return (cabeca[0] == rato[0]) and (cabeca[1] == rato[1])


pra_cima = 0
pra_esquerda = 1
pra_baixo = 2
pra_direita = 3


pygame.init()
largura = 600
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo da cobrinha')

cobra = [(200, 200), (210, 200), (220, 200)]
cor_da_cobra = pygame.Surface((10, 10))
cor_da_cobra.fill((131, 111, 255))

rato = pygame.Surface((10, 10))
rato.fill((144, 238, 144))
posicao_rato = colocar_rato_aqui()

direcao = pra_esquerda

fps = pygame.time.Clock()

pygame.mixer.music.load('music/awesomeness.wav')
pygame.mixer.music.play(100)

som_comendo_rato = pygame.mixer.Sound('music/crunch.4.ogg')

fim_de_jogo = False
font = pygame.font.SysFont(None, 25, bold=True)


def texto(msg, cor):
    texto1 = font.render(msg, True, cor)
    tela.blit(texto1, [170, altura/2])


while True:
    while fim_de_jogo:
        tela.fill((255, 255, 255))
        texto('Fim de Jogo - Aperte S para sair', (131, 111, 255))
        pygame.display.update()
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()

            if evento.type == KEYDOWN:
                if evento.key == pygame.K_s:
                    pygame.quit()
    fps.tick(12)
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()

        if evento.type == KEYDOWN:
            if evento.key == K_UP:
                direcao = pra_cima
            elif evento.key == K_RIGHT:
                direcao = pra_direita
            elif evento.key == K_DOWN:
                direcao = pra_baixo
            elif evento.key == K_LEFT:
                direcao = pra_esquerda

    if colisao(cobra[0], posicao_rato):
        som_comendo_rato.play()
        posicao_rato = colocar_rato_aqui()
        cobra.append((0, 0))

    for x in range(len(cobra)):
        if x > 0:
            if cobra[0] == cobra[x]:
                pygame.mixer.music.stop()
                fim_de_jogo = True

    for x in range(len(cobra) - 1, 0, -1):
        cobra[x] = (cobra[x-1][0], cobra[x-1][1])

    if direcao == pra_cima:
        cobra[0] = (cobra[0][0], cobra[0][1] - 10)
    elif direcao == pra_baixo:
        cobra[0] = (cobra[0][0], cobra[0][1] + 10)
    elif direcao == pra_esquerda:
        cobra[0] = (cobra[0][0] - 10, cobra[0][1])
    elif direcao == pra_direita:
        cobra[0] = (cobra[0][0] + 10, cobra[0][1])

    tela.fill((0, 0, 0))
    tela.blit(rato, posicao_rato)
    for posicao in cobra:
        tela.blit(cor_da_cobra, posicao)

    pygame.display.update()
