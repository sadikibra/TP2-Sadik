import time
from bilhetes import(
    imprime_lista_de_bilhetes
)
from io_terminal import (
    imprime_lista_de_dicionarios
)
from espetaculos import (
    cria_espetaculos,
    imprime_lista_de_espetaculos,
)
from clientes import (
    cria_novo_cliente,
    imprime_lista_de_clientes,
)
from lotacao import(
    lotacao_salas
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
        #to do: implementar novas features

def pergunta_id(questao, lista):
    """ ... ??to do??

    :param questao:
    :param lista:
    :return:
    """

    imprime_lista_de_dicionarios(lista)
    while True:
        idx = int(input(questao))
        if 0 <= idx < len(lista):
            return idx
        else:
            print(f"id inexistente. Tente de novo. Valores admitidos {0} - {len(lista)}")

if __name__ == "__main__":
    menu()
"""Desenha o menu no terminal"""   
