import time
from src.bilhetes import(
    imprime_lista_de_bilhetes
)
from src.io_terminal import (
    imprime_lista_de_dicionarios
)
from src.espetaculos import (
    cria_espetaculos,
    imprime_lista_de_espetaculos,
    nome_ficheiro_lista_de_espetaculos
)
from src.clientes import (
    cria_novo_cliente,
    imprime_lista_de_clientes,
    nome_ficheiro_lista_de_clientes
)
from src.lotacao import(
    lotacao_salas
)
from src.io_ficheiros import (
    guarda_em_ficheiro,
    le_de_ficheiro
)
def menu():
    """ Funcao menu cria o menu da aplicacao"""
    lista_de_espetaculos = []
    lista_de_clientes = []
    lista_de_compra = []
    while True:
        print("""
        *********************************************************************
        :             Espetacular - criacao de espetaculos                  : 
        *********************************************************************
        :                                                                   :
        : en - novo espetaculo      el - lista espetaculos                  :
        : cn - novo cliente         cl - lista clientes                     :
        : bn - novo bilhete         bl - lista bilhetes                     :
        : ls - lotacao salas                                                :
        : ...                                                               :
        : ...                                                               :
        : g - guarda tudo           c - carrega tudo                        :
        :                                                                   :
        : x - sair                                                          :
        :                                                                   :
        *********************************************************************
        """)

        op = input("opcao?").lower()

        if op == "x":
            exit()
        elif op == "ls":
            lotacao_salas()
        elif op == "en":
            nova_espetaculos = cria_espetaculos()
            lista_de_espetaculos.append(nova_espetaculos)
        elif op == "el":
            imprime_lista_de_espetaculos(lista_de_espetaculos)
        elif op == "cn":
            novo_cliente = cria_novo_cliente()
            lista_de_clientes.append(novo_cliente)
        elif op == "cl":
            imprime_lista_de_clientes(lista_de_clientes)
        elif op == "bn":
            if lista_de_clientes and lista_de_espetaculos:
                id_comprador = pergunta_id(questao="Qual o id do comprador?", lista=lista_de_clientes)
                id_espetaculo = pergunta_id(questao="Qual o id do espetaculo?", lista=lista_de_espetaculos)
                lista_de_compra.append([id_comprador, id_espetaculo, time.time()])
            else:
                print("Erro: tem de ter clientes e espetaculos")
        elif op == "bl":
            imprime_lista_de_bilhetes(lista_de_compra)
        elif op == "g":
            guarda_as_listas_em_ficheiros(lista_de_espetaculos, lista_de_clientes)
        elif op == "c":
            lista_de_espetaculos, lista_de_clientes = carrega_as_listas_dos_ficheiros()
            

def pergunta_id(questao, lista):
    imprime_lista_de_dicionarios(lista)
    while True:
        idx = int(input(questao))
        if 0 <= idx < len(lista):
            return idx
        else:
            print(f"id inexistente. Tente de novo. Valores admitidos {0} - {len(lista)}")

def carrega_as_listas_dos_ficheiros():
    """ 
    Carrega os dados de espetáculos e utilizadores a partir de um ficheiro local
    :return: o conteúdo de ambos ficheiro (depende dos dados guardados)
    """

    lista_de_espetaculos = le_de_ficheiro(nome_ficheiro_lista_de_espetaculos)
    lista_de_clientes = le_de_ficheiro(nome_ficheiro_lista_de_clientes)
    return lista_de_espetaculos, lista_de_clientes


def guarda_as_listas_em_ficheiros(lista_de_espetaculos, lista_de_clientes):
    """
    Guarda os dados da sessão para carregar numa sessão futura.
    :param lista_de_espetaculos: lista de espetáculos da sessão
    :param lista_de_utilizadores: lista de utilizadores da sessão
    """

    op = input("Os dados nos ficheiros serão sobrepostos. Continuar (S/n)?")
    if op in ['s', 'S', '']:
        guarda_em_ficheiro(nome_ficheiro_lista_de_espetaculos, lista_de_espetaculos)
        guarda_em_ficheiro(nome_ficheiro_lista_de_clientes, lista_de_clientes)
    else:
        print("Cancelada.")

if __name__ == "__main__":
    menu()
"""Desenha o menu no terminal"""   
