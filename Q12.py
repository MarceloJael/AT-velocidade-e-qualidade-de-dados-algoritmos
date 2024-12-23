import os

def listar_arquivos_recursivo(caminho):
    arquivos = []

    try:
        for item in os.listdir(caminho):
            item_caminho = os.path.join(caminho, item)

            if os.path.isfile(item_caminho):
                arquivos.append(item_caminho)

            elif os.path.isdir(item_caminho):
                arquivos.extend(listar_arquivos_recursivo(item_caminho))
    except PermissionError:
        print(f"Permissão negada para acessar: {caminho}")
    except FileNotFoundError:
        print(f"Caminho não encontrado: {caminho}")
    except Exception as e:
        print(f"Erro ao acessar {caminho}: {e}")

    return arquivos

# Testando o Algoritmo
diretorio_inicial = "C:\dev\Faculdade\Velocidade e Qualidade com Estruturas de Dados e Algoritmos\AT"

arquivos_encontrados = listar_arquivos_recursivo(diretorio_inicial)

print("\nArquivos encontrados:")
for arquivo in arquivos_encontrados:
    print(arquivo)
