def menu():
    """ Funcao menu cria o menu da aplicacao"""

  

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
        #to do: implementar novas features

if __name__ == "__main__":
    menu()
"""Desenha o menu no terminal"""            