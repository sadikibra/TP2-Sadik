from io_terminal import imprime_lista

nome_ficheiro_lista_de_clientes = "lista_de_cliente.pk"

def cria_novo_cliente():
    """ pede os dados de um novo cliente

    :return: dicionario com o novo utilizador, {"nome": <<nome>>, "email": <<email>>}
    """
    nome = input("nome? ")
    email = input("email? ")
    return {"nome": nome, "email": email}


def imprime_lista_de_clientes(lista_de_clientes):
    """ ..."""
   
    imprime_lista(cabecalho="Lista de Cliente", lista=lista_de_clientes)

nome_ficheiro_lista_de_clientes = "lista_de_cliente.pk"
    