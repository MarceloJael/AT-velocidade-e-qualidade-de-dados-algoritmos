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

    def encontrar_minimo(self):

        if self.raiz is None:
            return None
        atual = self.raiz
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual.valor

    def encontrar_maximo(self):

        if self.raiz is None:
            return None
        atual = self.raiz
        while atual.direita is not None:
            atual = atual.direita
        return atual.valor

notas = [85, 70, 95, 60, 75, 90, 100]
arvore = ArvoreBST()

for nota in notas:
    arvore.inserir(nota)

nota_minima = arvore.encontrar_minimo()
nota_maxima = arvore.encontrar_maximo()

print(f"Nota mínima: {nota_minima}")
print(f"Nota máxima: {nota_maxima}")
