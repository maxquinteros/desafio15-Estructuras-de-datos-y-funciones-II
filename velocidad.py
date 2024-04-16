def promedio_lista (lista: list) -> float:
    """_summary_
        Calcular el promedio de una lista
        
    Args:
        lista (list): _Una lista con valores numéricos_

    Returns:
        float: _Promedio calculado de la lista_
    """
    suma = sum(lista)
    numero_total = len(lista)
    
    return suma / numero_total

def posiciones_mayores (lista: list, numero_comparar: float) -> list:
    """_summary_
        Verifica que elementos de una lista es mayor a otro numero y guarda su posicion en una lista
    Args:
        lista (list): _Una lista con valores numéricos_
        numero_comparar (float): _Numero al cual se le comparara, puede ser calculado o un valor arbitrario_

    Returns:
        list: _Lista de las posiciones cuyos valores son mayores al numero a comparar_
    """
    lista_mayores = []
    index = 0
    
    for elemento in lista:
        if elemento > numero_comparar:
            lista_mayores.append(index)
            
        index += 1
            
    return lista_mayores

velocidad = [25, 12, 19, 16, 11, 11, 24, 1,
14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2,
14, 23, 19, 23, 9, 18, 20, 22, 14, 1,
10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5,
11, 10, 18, 10, 14, 5, 23, 20, 23, 21]

promedio_velocidad = promedio_lista(velocidad)
print(posiciones_mayores(velocidad, promedio_velocidad))