def selection_sort_jogadores(jogadores):
    
    n = len(jogadores)

    for i in range(n):
        indice_maior = i

        for j in range(i + 1, n):
            if jogadores[j]['pontuacao'] > jogadores[indice_maior]['pontuacao']:
                indice_maior = j

        jogadores[i], jogadores[indice_maior] = jogadores[indice_maior], jogadores[i]

    return jogadores

jogadores = [
    {'nome': 'Alice', 'pontuacao': 1200},
    {'nome': 'Bob', 'pontuacao': 800},
    {'nome': 'Charlie', 'pontuacao': 1500},
    {'nome': 'Diana', 'pontuacao': 950},
]

jogadores_ordenados = selection_sort_jogadores(jogadores)

print("Jogadores ordenados por pontuação:")
for jogador in jogadores_ordenados:
    print(f"{jogador['nome']}: {jogador['pontuacao']}")
