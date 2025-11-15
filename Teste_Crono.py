import pygame
import sys
import time

# Inicializar Pygame
pygame.init()

# Obter dimensões da tela
info = pygame.display.Info()
largura_tela, altura_tela = info.current_w, info.current_h

# Criar janela em tela cheia
janela = pygame.display.set_mode((largura_tela, altura_tela), pygame.FULLSCREEN)
pygame.display.set_caption("Tela interativa")

# Carregar imagens
imagem_original = pygame.image.load("TRIF_2025.jpeg")
imagem_original = pygame.transform.scale(imagem_original, (largura_tela, altura_tela))

fundo = pygame.image.load("Imagem_FundoBlack.png")
fundo = pygame.transform.scale(fundo, (largura_tela, altura_tela))

imagem_azul = pygame.image.load("Imagem_Azul_2.png")
imagem_azul = pygame.transform.scale(imagem_azul, (largura_tela // 2, altura_tela))

imagem_vermelho = pygame.image.load("Imagem_Vermelho_2.png")
imagem_vermelho = pygame.transform.scale(imagem_vermelho, (largura_tela // 2, altura_tela))

imagem_final = pygame.image.load("Imagem_AzulVermelho.png")
imagem_final = pygame.transform.scale(imagem_final, (largura_tela, altura_tela))

# Fonte PressStart2P
fonte_grande = pygame.font.Font("PressStart2P-Regular.ttf", 200)
fonte_timer = pygame.font.Font("PressStart2P-Regular.ttf", 250)

# Estados
mostrar_esquerda = False
mostrar_direita = False
mostrar_inicial = True
cronometro_ativo = False
tempo_inicial = None

def contagem_regressiva():
    """Mostra contagem regressiva 3,2,1,FIGHT com fundo azul"""
    sequencia = ["3", "2", "1", "FIGHT!"]
    for texto in sequencia:
        janela.fill((0, 0, 255))  # fundo azul
        render = fonte_grande.render(texto, True, (255, 255, 255))  # texto branco
        rect = render.get_rect(center=(largura_tela // 2, altura_tela // 2))
        janela.blit(render, rect)
        pygame.display.flip()
        time.sleep(1)

def desenhar_cronometro():
    """Desenha cronômetro regressivo com fundo colorido e números brancos"""
    global tempo_inicial, cronometro_ativo

    if not cronometro_ativo:
        return

    # Tempo total em segundos (2 minutos = 120s)
    tempo_total = 120
    tempo_passado = time.time() - tempo_inicial
    tempo_restante = max(0, tempo_total - int(tempo_passado))

    minutos = tempo_restante // 60
    segundos = tempo_restante % 60
    texto_tempo = f"{minutos}:{segundos:02d}"

    # Definir cor do fundo conforme intervalo
    if tempo_restante >= 80:  # 2:00 até 1:20
        cor_fundo = (0, 255, 0)  # verde
    elif 60 <= tempo_restante <= 79:  # 1:19 até 1:00
        cor_fundo = (255, 255, 0, 1)  # amarelo
    else:  # 0:59 até 0:00
        cor_fundo = (255, 0, 0)  # vermelho

    # Pintar fundo com a cor escolhida
    janela.fill(cor_fundo)

    # Texto do cronômetro em branco
    render = fonte_timer.render(texto_tempo, True, (255, 255, 255))
    rect = render.get_rect(center=(largura_tela // 2, altura_tela // 2))
    janela.blit(render, rect)

# Loop principal
rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mostrar_esquerda = True
                mostrar_inicial = False
            elif event.key == pygame.K_d:
                mostrar_direita = True
                mostrar_inicial = False
            elif event.key == pygame.K_s:
                mostrar_esquerda = False
                mostrar_direita = False
                mostrar_inicial = False
            elif event.key == pygame.K_c:
                contagem_regressiva()
                tempo_inicial = time.time()
                cronometro_ativo = True
                mostrar_esquerda = False
                mostrar_direita = False
                mostrar_inicial = False
            elif event.key == pygame.K_ESCAPE:
                rodando = False

    # Renderizar estados visuais
    if cronometro_ativo:
        desenhar_cronometro()
    else:
        if mostrar_inicial:
            janela.blit(imagem_original, (0, 0))
        elif mostrar_esquerda and mostrar_direita:
            janela.blit(imagem_final, (0, 0))
        elif mostrar_esquerda and not mostrar_direita:
            janela.blit(fundo, (0, 0))
            janela.blit(imagem_azul, (0, 0))
        elif mostrar_direita and not mostrar_esquerda:
            janela.blit(fundo, (0, 0))
            janela.blit(imagem_vermelho, (largura_tela // 2, 0))
        else:
            janela.blit(fundo, (0, 0))

    pygame.display.flip()

# Encerrar Pygame
pygame.quit()
sys.exit()


