def knapsack(pesos, valores, capacidade):

    n = len(valores)

    dp = [[0] * (capacidade + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacidade + 1):
            if pesos[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], valores[i - 1] + dp[i - 1][w - pesos[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacidade]

pesos = [2, 3, 4, 5]
valores = [3, 4, 5, 6]
capacidade = 8

valor_maximo = knapsack(pesos, valores, capacidade)
print(f"Valor máximo que pode ser transportado: {valor_maximo}")
