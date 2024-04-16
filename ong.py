def factorial (numero: int) -> int:
    """_summary_
        Calcula el factorial el numero que sea ingresado
    Args:
        numero (int): _Numero ingresado al que se le quiere calcular el factorial_

    Returns:
        int: _Valor resultado del numero ingresado_
    """
    resultado = 1
    
    operacion = numero
    
    for i in range(numero):
        resultado *= operacion
        operacion -= 1
    
    return resultado
    
def productoria (lista: list) -> int:
    """_summary_
        Calcula la productoria de la lista que sea ingresada
    Args:
        lista (list): _Lista de valores numéricos_

    Returns:
        int: _Valor resultado de la multiplicacion de los elementos de la lista_
    """
    
    resultado = 1
    
    for i in lista:
        resultado *= i
    
    return resultado

def calcular(**operaciones):
    for operacion, valor in operaciones.items():
        if "fact" in operacion:
            print(f"El factorial de {valor} es {factorial(valor)}")
        elif "prod" in operacion:
            print(f"La productoria de {valor} es {productoria(valor)}")
        
calcular(fact_1 = 5, prod_1 = [4,6,7,4,3], fact_2 = 6)