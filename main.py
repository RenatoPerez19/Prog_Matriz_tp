def multiplicar_matrices(mat_1: list [list [int] ] , mat_2:list [list [int] ])-> list [list [int] ] :
    """ Multiplicar matrices dadas , mientras que sea posible segun sus filas
    y columnas. Recibe dos matrices y las multiplica


    returns: 
        Lista de listas que representa la multiplicacion de las matrices
    Args:
        mat_1 (list[list [int] ]): _description_
        mat_2 (list[list [int] ]): _description_

    Returns:
        list [list [int] ]: _description_
    """
    if len(mat_1[0]) != len(mat_2):
        return None
    tercer_matriz= [[0] * len(mat_2[0]) for _ in range(len(mat_1))]
    for columna in range(len(mat_1)):
        for suma in range(len(mat_2[0])):
            suma_actual=0
            for fila in range(len(mat_2)):
                suma_actual +=mat_1[columna][fila] * mat_2[columna][fila]
                tercer_matriz[columna][suma] = suma_actual
    
    return tercer_matriz
    

matriz_uno=[
    [3 , 7, 5],
    [12 , 2 ,11]
    ]

matriz_dos=[
    [3 , 16],
    [1 , 4],
    [4 , 22]
    ]


print(multiplicar_matrices(matriz_uno, matriz_dos))