def verificar_duplicatas(lista):

    elementos_vistos = set()

    for elemento in lista:
        if elemento in elementos_vistos:
            return True
        elementos_vistos.add(elemento)

    return False

# Lista de teste
lista_teste_1 = [1, 2, 3, 4, 5]  # Sem duplicatas
lista_teste_2 = [1, 2, 3, 4, 5, 3]  # Contém duplicatas
lista_teste_3 = [10, 20, 30, 40, 50, 10]  # Duplicata no início e fim

# Executando os testes
print("Teste 1 - Sem duplicatas:", verificar_duplicatas(lista_teste_1))  #Esperado: False
print("Teste 2 - Com duplicatas:", verificar_duplicatas(lista_teste_2))  #Esperado: True
print("Teste 3 - Com duplicatas:", verificar_duplicatas(lista_teste_3))  #Esperado: True
