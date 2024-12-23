class NoBST:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBST:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        
        if self.raiz is None:
            self.raiz = NoBST(valor)
        else:
            self._inserir_recursivo(self.raiz, valor)

    def _inserir_recursivo(self, no, valor):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = NoBST(valor)
            else:
                self._inserir_recursivo(no.esquerda, valor)
        elif valor > no.valor:
            if no.direita is None:
                no.direita = NoBST(valor)
            else:
                self._inserir_recursivo(no.direita, valor)

    def remover(self, valor):

        self.raiz = self._remover_recursivo(self.raiz, valor)

    def _remover_recursivo(self, no, valor):
        if no is None:
            return no

        if valor < no.valor:
            no.esquerda = self._remover_recursivo(no.esquerda, valor)
        elif valor > no.valor:
            no.direita = self._remover_recursivo(no.direita, valor)
        else:
            if no.esquerda is None and no.direita is None:
                return None
            if no.esquerda is None:
                return no.direita
            if no.direita is None:
                return no.esquerda
            sucessor = self._minimo(no.direita)
            no.valor = sucessor.valor
            no.direita = self._remover_recursivo(no.direita, sucessor.valor)

        return no

    def _minimo(self, no):
        
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

    def exibir_em_ordem(self):

        valores = []
        self._em_ordem_recursivo(self.raiz, valores)
        return valores

    def _em_ordem_recursivo(self, no, valores):
        if no is not None:
            self._em_ordem_recursivo(no.esquerda, valores)
            valores.append(no.valor)
            self._em_ordem_recursivo(no.direita, valores)

codigos = [45, 25, 65, 20, 30, 60, 70]
arvore = ArvoreBST()

for codigo in codigos:
    arvore.inserir(codigo)

print("Árvore em ordem crescente (inicial):", arvore.exibir_em_ordem())
arvore.remover(20)
print("Após remover 20 (nó folha):", arvore.exibir_em_ordem())
arvore.remover(25)
print("Após remover 25 (nó com um filho):", arvore.exibir_em_ordem())
arvore.remover(45)
print("Após remover 45 (nó com dois filhos):", arvore.exibir_em_ordem())