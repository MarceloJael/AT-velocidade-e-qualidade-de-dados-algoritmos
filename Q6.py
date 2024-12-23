import time
import random

def bubble_sort(lista):

    n = len(lista)
    for i in range(n):
        trocou = False
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                trocou = True
        if not trocou:
            break
    return lista

def medir_tempo_execucao(tamanho_lista):

    lista = [random.uniform(1, 1000) for _ in range(tamanho_lista)]
    inicio = time.time()
    bubble_sort(lista)
    fim = time.time()
    return fim - inicio

# Testes com 1 mil e 10 mil elementos
tempo_1mil = medir_tempo_execucao(1000)
tempo_10mil = medir_tempo_execucao(10000)

print(f"Tempo para ordenar 1 mil elementos: {tempo_1mil:.4f} segundos")
print(f"Tempo para ordenar 10 mil elementos: {tempo_10mil:.4f} segundos")