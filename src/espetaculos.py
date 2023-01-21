from src.io_terminal import imprime_lista

def cria_espetaculos():
    """ Pede ao utilizador para introduzir uma novo espetaculos

    :return: dicionario com um espetaculo na forma 
        {"marca": <<marca>>, "modelo": <<modelo>>, ... COMPLETAR ...}
    """

    nome_espetaculo = input("nome? ")
    local_espetaculo = input("local? ").upper()
    return {"nome": nome_espetaculo, "local": local_espetaculo}
 

def imprime_lista_de_espetaculos(lista_de_espetaculos):
    """ ..."""

    imprime_lista(cabecalho="Lista de Espetaculos", lista=lista_de_espetaculos)

nome_ficheiro_lista_de_espetaculos = "lista_de_espetaculos.pk"