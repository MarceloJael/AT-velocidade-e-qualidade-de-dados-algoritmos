import random

def busca_binaria(lista, isbn_buscado):
    
    inicio, fim = 0, len(lista) - 1
    iteracoes = 0

    while inicio <= fim:
        iteracoes += 1
        meio = (inicio + fim) // 2

        if lista[meio] == isbn_buscado:
            return meio, iteracoes
        elif lista[meio] < isbn_buscado:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1, iteracoes

def busca_linear(lista, isbn_buscado):

    for i, isbn in enumerate(lista):
        if isbn == isbn_buscado:
            return i, i + 1
    return -1, len(lista)

isbn_lista = list(range(1, 100001))

isbn_teste = random.choice(isbn_lista)

# Busca Binária
posicao_binaria, iteracoes_binaria = busca_binaria(isbn_lista, isbn_teste)
print(f"Busca Binária: ISBN {isbn_teste} encontrado na posição {posicao_binaria} em {iteracoes_binaria} iterações.")

# Busca Linear
posicao_linear, iteracoes_linear = busca_linear(isbn_lista, isbn_teste)
print(f"Busca Linear: ISBN {isbn_teste} encontrado na posição {posicao_linear} em {iteracoes_linear} iterações.")
