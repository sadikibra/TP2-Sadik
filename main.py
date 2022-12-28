
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
        #to do: implementar novas features

if __name__ == "__main__":
    menu()
"""Desenha o menu no terminal"""            