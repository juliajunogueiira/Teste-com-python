import pygame
import sys

# Inicializar Pygame
pygame.init()

# Obter dimensões da tela
info = pygame.display.Info()
largura_tela, altura_tela = info.current_w, info.current_h

# Criar janela em tela cheia
janela = pygame.display.set_mode((largura_tela, altura_tela), pygame.FULLSCREEN)
pygame.display.set_caption("Tela interativa")

# Carregar imagens
fundo = pygame.image.load("Imagem_FundoBlack.png")
fundo = pygame.transform.scale(fundo, (largura_tela, altura_tela))

imagem_azul = pygame.image.load("Imagem_Azul_2.png")
imagem_azul = pygame.transform.scale(imagem_azul, (largura_tela // 2, altura_tela))

imagem_vermelho = pygame.image.load("Imagem_Vermelho_2.png")
imagem_vermelho = pygame.transform.scale(imagem_vermelho, (largura_tela // 2, altura_tela))

imagem_final = pygame.image.load("Imagem_AzulVermelho.png")
imagem_final = pygame.transform.scale(imagem_final, (largura_tela, altura_tela))

# Estados
mostrar_esquerda = False
mostrar_direita = False

# Loop principal
rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:  # tecla 'a' → ativa lado esquerdo azul
                mostrar_esquerda = True
            elif event.key == pygame.K_d:  # tecla 'd' → ativa lado direito vermelho
                mostrar_direita = True
            elif event.key == pygame.K_s:  # tecla 's' → resetar para fundo preto
                mostrar_esquerda = False
                mostrar_direita = False
            elif event.key == pygame.K_ESCAPE:  # tecla Esc → sair do modo tela cheia
                janela = pygame.display.set_mode((800, 600))

    # Desenhar fundo
    janela.blit(fundo, (0, 0))

    # Estados visuais
    if mostrar_esquerda and mostrar_direita:
        # Estado final: imagem completa AzulVermelho
        janela.blit(imagem_final, (0, 0))
    elif mostrar_esquerda and not mostrar_direita:
        # Azul e preto
        janela.blit(imagem_azul, (0, 0))
    elif mostrar_direita and not mostrar_esquerda:
        # Preto e vermelho
        janela.blit(imagem_vermelho, (largura_tela // 2, 0))
    # Se nenhum ativo → apenas fundo preto (já desenhado acima)

    # Atualizar tela
    pygame.display.flip()

# Encerrar Pygame
pygame.quit()
sys.exit()
