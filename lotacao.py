def lotacao_salas():
    numsala = int(input("introduza o numero da sala a qual deseja ver a lotação"))
    listaLotacao = [120,320,170,300,436]
    if numsala < 1 or numsala > 5:
        print("Introduza de 1 a 5 o numero da sala.")
    else:
        print("A sala numero", numsala,"tem este número de lugares disponiveis:",listaLotacao[numsala-1])
    pass