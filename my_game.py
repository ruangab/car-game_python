from random import randint
import pygame
#iniciando o pygame
pygame.init()

#inicialixando as cordenadas dos carros
x = 400
y = 300
pol_x = 275
pol_y = 0 - randint(300, 2000)
pol_y2 = 0 - randint(300, 2000)
pol_x2 = 505

#inicializando as velocidades dos carros
velo_policia = 7
velocidade = 6

#salvando as imagens em variáveis 
fundo = pygame.image.load('pista.png')
carro = pygame.image.load('carro.jpg')
policia = pygame.image.load('carro2.jpg')
policia2 = pygame.image.load('carro2.jpg')
#inicializando a janela do jogo
janela = pygame.display.set_mode((820,400))

pygame.display.set_caption("Criando um game em python")

WINDOW_OPEN = True

#enquanto a janela estiver aberta
while WINDOW_OPEN :
    
    pygame.time.delay(20)

    for event in pygame.event.get():
        #caso o botão de fechar seja selecionado, feche o jogo
        if event.type == pygame.QUIT:
            WINDOW_OPEN = False

    #pegando eventos do teclado    
    comand = pygame.key.get_pressed()

    #alterando as cordenadas do carro pelo teclado, movimentando ele
    if comand[pygame.K_UP]:
        y-= velocidade
    if comand[pygame.K_DOWN]:
        y+= velocidade
    if comand[pygame.K_RIGHT]:
        x+= velocidade
    if comand[pygame.K_LEFT]:
        x-= velocidade


    #caso a imagem do carro saia da tela
    if pol_y >= 450:
        pol_y = 0-randint(300, 2000)

    #movimentando o carro da polícia
    pol_y += velo_policia

    #caso a imagem do carro saia da tela
    if pol_y2 >= 450:
         pol_y2 = 0-randint(300, 2000)

    #movimentando o carro da polícia
    pol_y2 += velo_policia


    #inserindo as imagens na janela
    janela.blit(fundo,(0,0))
    janela.blit(carro,(x,y))
    janela.blit(policia2,(pol_x2, pol_y2))
    janela.blit(policia,(pol_x, pol_y))

    #atualizando o game
    pygame.display.update()

pygame.quit()