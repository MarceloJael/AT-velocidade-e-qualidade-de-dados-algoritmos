class Navegador:
    def __init__(self):
        self.pilha_voltar = []  # Armazena páginas anteriores
        self.pilha_avancar = []  # Armazena páginas para avançar
        self.pagina_atual = None  # Página atualmente acessada

    def visitar_pagina(self, url):
        
        if self.pagina_atual:
            self.pilha_voltar.append(self.pagina_atual)
        self.pagina_atual = url
        self.pilha_avancar.clear()
        print(f"Visitando página: {url}")

    def voltar(self):

        if not self.pilha_voltar:
            print("Não há páginas para voltar.")
            return
        self.pilha_avancar.append(self.pagina_atual)
        self.pagina_atual = self.pilha_voltar.pop()
        print(f"Voltando para: {self.pagina_atual}")

    def avancar(self):

        if not self.pilha_avancar:
            print("Não há páginas para avançar.")
            return
        self.pilha_voltar.append(self.pagina_atual)
        self.pagina_atual = self.pilha_avancar.pop()
        print(f"Avançando para: {self.pagina_atual}")

    def exibir_estado(self):

        print("\nEstado do Navegador:")
        print(f"Página atual: {self.pagina_atual}")
        print(f"Pilha Voltar: {self.pilha_voltar}")
        print(f"Pilha Avançar: {self.pilha_avancar}")


# Testando a implementação
navegador = Navegador()
navegador.visitar_pagina("chatgpt.com")
navegador.visitar_pagina("google.com.br")
navegador.visitar_pagina("infnet.edu.br")
navegador.exibir_estado()
navegador.voltar()
navegador.exibir_estado()
navegador.voltar()
navegador.exibir_estado()
navegador.avancar()
navegador.exibir_estado()
navegador.visitar_pagina("python.org")
navegador.exibir_estado()