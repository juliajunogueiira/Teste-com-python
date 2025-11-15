import pygame
import time
import sys


# Inicializa o Pygame
print("[INFO] Iniciando Pygame...")
try:
    pygame.init()
    print("[OK] Pygame inicializado com sucesso")
except Exception as e:
    print(f"[ERRO] Falha ao inicializar Pygame: {e}")
    sys.exit(1)

# Configurações da tela
largura_tela = 400
altura_tela = 300

print("[INFO] Criando janela...")
try:
    tela = pygame.display.set_mode((largura_tela, altura_tela))
    pygame.display.set_caption("Exemplo de Fonte Pixel")
    print("[OK] Janela criada com sucesso")
except Exception as e:
    print(f"[ERRO] Falha ao criar janela: {e}")
    pygame.quit()
    sys.exit(1)

# Define as cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

# 1. Carrega o arquivo da fonte
print("[INFO] Tentando carregar fonte 'PressStart2P-Regular.ttf'...")
try:
    fonte_pixel = pygame.font.Font('PressStart2P-Regular.ttf', 16)
    print("[OK] Fonte carregada com sucesso")
except Exception as e:
    print(f"[AVISO] Não foi possível carregar a fonte: {e}")
    print("[INFO] Usando fonte padrão do sistema como fallback...")
    try:
        fonte_pixel = pygame.font.SysFont(None, 16)
        print("[OK] Fonte padrão carregada com sucesso")
    except Exception as e2:
        print(f"[ERRO] Falha ao carregar fonte padrão: {e2}")
        pygame.quit()
        sys.exit(1)

# 2. Renderiza o texto
print("[INFO] Renderizando texto...")
try:
    texto_superficie = fonte_pixel.render('Ola, mundo pixel!', True, BRANCO)
    print("[OK] Texto renderizado com sucesso")
except Exception as e:
    print(f"[ERRO] Falha ao renderizar texto: {e}")
    pygame.quit()
    sys.exit(1)

# Posição do texto
texto_rect = texto_superficie.get_rect()
texto_rect.center = (largura_tela // 2, altura_tela // 2)

# Loop principal do jogo
print("[INFO] Iniciando loop principal (5 segundos)...")
executando = True
duracao_segundos = 5
inicio = time.time()

try:
    while executando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                print("[INFO] Evento QUIT recebido")
                executando = False
            # Fechar com ESC
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    print("[INFO] Tecla ESC pressionada")
                    executando = False

        # Sai automaticamente após N segundos
        tempo_decorrido = time.time() - inicio
        if tempo_decorrido > duracao_segundos:
            print(f"[INFO] Tempo limite de {duracao_segundos}s atingido")
            executando = False

        # Desenha
        tela.fill(PRETO)
        tela.blit(texto_superficie, texto_rect)
        pygame.display.flip()
        
        # Controla FPS
        time.sleep(0.016)  # ~60 FPS

except Exception as e:
    print(f"[ERRO] Exceção no loop principal: {e}")
    import traceback
    traceback.print_exc()

# Encerra o Pygame
print("[INFO] Encerrando Pygame...")
pygame.quit()
print("[OK] Programa finalizado com sucesso")
