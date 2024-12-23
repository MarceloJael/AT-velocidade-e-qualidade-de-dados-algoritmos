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

    def buscar(self, valor):

        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, no, valor):
        if no is None:
            return False
        if no.valor == valor:
            return True
        elif valor < no.valor:
            return self._buscar_recursivo(no.esquerda, valor)
        else:
            return self._buscar_recursivo(no.direita, valor)

precos = [100, 50, 150, 30, 70, 130, 170]
arvore = ArvoreBST()

for preco in precos:
    arvore.inserir(preco)

preco_procurado = 70
disponivel = arvore.buscar(preco_procurado)

print(f"O preço {preco_procurado} está disponível: {disponivel}")
