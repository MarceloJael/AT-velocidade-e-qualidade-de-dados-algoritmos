def buscar_contato(contatos, nome_buscado):
    
    for contato in contatos:
        if contato['nome'] == nome_buscado:
            return f"Telefone encontrado: {contato['telefone']}"
    return "Contato não encontrado."

contatos = [
    {"nome": "Ana", "telefone": "1234-5678"},
    {"nome": "Bruno", "telefone": "8912-3456"},
    {"nome": "Carlos", "telefone": "7891-2345"},
    {"nome": "Diana", "telefone": "6789-1234"}
]

#Teste 1: Nome existente
print(buscar_contato(contatos, "Carlos"))

#Teste 2: Nome inexistente
print(buscar_contato(contatos, "Marcelo"))

#Teste 3: Nome no início da lista
print(buscar_contato(contatos, "Ana"))

#Teste 4: Nome no final da lista
print(buscar_contato(contatos, "Diana"))