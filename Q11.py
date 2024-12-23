from collections import deque

class Atendimento:
    def __init__(self):
        self.fila = deque()

    def adicionar_chamado(self, chamado):

        self.fila.append(chamado)
        print(f"Chamado '{chamado}' adicionado à fila.")

    def atender_chamado(self):

        if not self.fila:
            print("Não há chamados para atender.")
            return None
        chamado = self.fila.popleft()
        print(f"Atendendo chamado: {chamado}")
        return chamado

    def exibir_fila(self):

        if not self.fila:
            print("A fila está vazia.")
        else:
            print(f"Chamados na fila: {list(self.fila)}")

# Simulação do Sistema de Atendimento
sistema_atendimento = Atendimento()

# Adicionando chamados à fila
sistema_atendimento.adicionar_chamado("Erro na entregado AT")
sistema_atendimento.adicionar_chamado("Solicitação de reentrega de AT")
sistema_atendimento.adicionar_chamado("Solicitação para o professor abrir o AT")

# Exibindo o estado atual da fila
sistema_atendimento.exibir_fila()

# Atendendo os chamados
sistema_atendimento.atender_chamado()
sistema_atendimento.exibir_fila()

sistema_atendimento.atender_chamado()
sistema_atendimento.exibir_fila()

sistema_atendimento.atender_chamado()
sistema_atendimento.exibir_fila()

# Tentando atender um chamado com a fila vazia
sistema_atendimento.atender_chamado()
