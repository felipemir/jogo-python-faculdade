import pygame
import sys

class Game:
    def __init__(self, largura=1280, altura=720):
        pygame.init()
        self.largura = largura
        self.altura = altura
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("Detona Hero - Demo")
        self.clock = pygame.time.Clock()

        # Carregar imagens
        self.fundo = pygame.image.load("assets/fundo.png").convert()
        self.fundo = pygame.transform.scale(self.fundo, (self.largura, self.altura))
        
        self.lua = pygame.image.load("assets/lua.png").convert_alpha() 

        self.predio = pygame.image.load("assets/predio.png").convert_alpha()

        self.janela_quebrada = pygame.image.load("assets/janelaquebrada.png").convert_alpha()

        # Posição do prédio na tela
        self.predio_x = 440
        self.predio_y = 60

        # Criar lista vazia para posições das janelas quebradas
        self.posicoes_janelas_quebradas = []

        # Montar grade de janelas quebradas: 5 andares x 3 colunas
        for andar in range(5):      # 5 andares
            for coluna in range(3): # 3 colunas
                x = self.predio_x + -142 + coluna * 147   # ajuste a distância horizontal entre janelas aqui
                y = self.predio_y + -185 + andar * 130    # ajuste a distância vertical entre janelas aqui
                self.posicoes_janelas_quebradas.append((x, y))

        # Posição da lua
        self.posicao_lua = [(5, 30)]

        self.rodando = True

    def executar(self):
        while self.rodando:
            self.tratar_eventos()
            self.desenhar()
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

    def tratar_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.rodando = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.rodando = False

    def desenhar(self):
        self.tela.blit(self.fundo, (0, 0))
        self.tela.blit(self.predio, (self.predio_x, self.predio_y))

        for pos in self.posicoes_janelas_quebradas:
            self.tela.blit(self.janela_quebrada, pos)

        for pos in self.posicao_lua:
            self.tela.blit(self.lua, pos)

if __name__ == "__main__":
    jogo = Game()
    jogo.executar()
