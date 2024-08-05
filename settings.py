# settings.py

import pygame
import os

# Configurações
pygame.init()
largura, altura = 1280, 640
tamanho_quadrado = 32
velocidade_jogo = 15

# Tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo Snake Python")
relogio = pygame.time.Clock()

# Diretórios
diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, 'imagens')
diretorio_sons = os.path.join(diretorio_principal, 'sons')

# Imagens
sprite_sheet_comida1 = pygame.image.load(os.path.join(diretorio_imagens, 'comida1.png')).convert_alpha()
sprite_sheet_comida2 = pygame.image.load(os.path.join(diretorio_imagens, 'comida2.png')).convert_alpha()
sprite_sheet_comida3 = pygame.image.load(os.path.join(diretorio_imagens, 'comida3.png')).convert_alpha()
sprite_sheet_bomba = pygame.image.load(os.path.join(diretorio_imagens, 'bomba.png')).convert_alpha()
bg = pygame.image.load(os.path.join(diretorio_imagens, 'bg.png')).convert_alpha()

# Cores
preta = (0, 0, 0)
branca = (255, 255, 255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
amarelo = (255, 255, 0)
cinza = (128, 128, 128)

#som:
pygame.mixer.music.set_volume(0.20)
musica_de_fundo = pygame.mixer.music.load(os.path.join(diretorio_sons, 'Soundtrack from Pou _-_ - Connect _ Cliff Jump _ C(MP3_70K).mp3'))
pygame.mixer.music.play(-1)

barulho_colisao_comidas = pygame.mixer.Sound(os.path.join(diretorio_sons, 'smw_coin.wav'))
barulho_colisao_run_time = pygame.mixer.Sound(os.path.join(diretorio_sons, 'y2mate_rLgMJTu.wav'))
