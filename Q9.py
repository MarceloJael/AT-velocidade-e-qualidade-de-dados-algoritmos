class RedeSocial:
    def __init__(self):
        self.usuarios = {}

    def adicionar_usuario(self, nome_usuario, perfil):

        self.usuarios[nome_usuario] = perfil
        print(f"Usuário '{nome_usuario}' adicionado com sucesso.")

    def buscar_usuario(self, nome_usuario):

        return self.usuarios.get(nome_usuario, "Usuário não encontrado.")

    def remover_usuario(self, nome_usuario):

        if nome_usuario in self.usuarios:
            del self.usuarios[nome_usuario]
            return f"Usuário '{nome_usuario}' removido com sucesso."
        return "Usuário não encontrado."


# Testando a Hashtable
rede_social = RedeSocial()

rede_social.adicionar_usuario("alice123", {"nome": "Alice", "idade": 25, "cidade": "São Paulo"})
rede_social.adicionar_usuario("bob456", {"nome": "Bob", "idade": 30, "cidade": "Rio de Janeiro"})
rede_social.adicionar_usuario("charlie789", {"nome": "Charlie", "idade": 22, "cidade": "Belo Horizonte"})

# Buscando perfis
print("\nBuscando usuários:")
print(rede_social.buscar_usuario("alice123"))
print(rede_social.buscar_usuario("bob456"))
print(rede_social.buscar_usuario("diana000"))

# Removendo um perfil
print("\nRemovendo usuário:")
print(rede_social.remover_usuario("bob456"))
print(rede_social.buscar_usuario("bob456"))
