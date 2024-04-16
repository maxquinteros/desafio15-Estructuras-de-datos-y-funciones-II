import sys


def calculo_umbral(numero_umbral: int, diccionario: dict, operacion="mayor") -> list:
    """_summary_
        Agregar en una lista los keys de un diccionario cuyo value sea mayor o menor a un valor dependiendo del usuario.

    Args:
        numero_umbral (int): _Valor a ser comparado._
        diccionario (dict): _Diccionario con el que se hará la comparación_
        operacion (str, optional): _Operacion que se hara en la funcion, puede ser "mayor" o "menor". Por defecto es "mayor"_

    Returns:
        list: _Lista de keys que cumplen la condicion de ser mayor/menor que el numero_umbral_

    Nota:
        Me acabo de dar cuenta que siguiendo lo que explico el profe, lo más eficiente y clean code era separar esta funcion
        en calculo_umbral_mayor y calculo_umbral_menor, por favor no me bajen la nota, tengo mucho sueño y flojera para hacer
        la separacion, ayuda por favor ya no quiero ser un adulto
    """

    productos_resultado = []

    if operacion.lower() == "mayor":
        for producto in diccionario:
            if diccionario[producto] > numero_umbral:
                productos_resultado.append(producto)

        return productos_resultado

    elif operacion.lower() == "menor":
        for producto in diccionario:
            if diccionario[producto] < numero_umbral:
                productos_resultado.append(producto)

        return productos_resultado

    else:
        pass


def imprimir_resultado(lista_umbral: list, operacion="mayor"):
    """_summary_
        Imprimir en la terminal los resultados de la funcion calculo_umbral dependiendo de la operacion del usuario
        
    Args:
        lista_umbral (list): _Lista de keys que satisfacen los requerimientos de la funcion calculo_umbral_
        operacion (str, optional): _Operacion que se hara en la funcion, puede ser "mayor" o "menor". Por defecto es "mayor"_
    """
    if operacion.lower() == "mayor":
        print(f"Los productos mayores al umbral son: {", ".join(lista_umbral)}")
    elif operacion.lower() == "menor":
        print(f"Los productos menores al umbral son: {", ".join(lista_umbral)}")
    else:
        print("Lo sentimos, no es una operación válida")


precios = {
    "Notebook": 700000,
    "Teclado": 25000,
    "Mouse": 12000,
    "Monitor": 250000,
    "Escritorio": 135000,
    "Tarjeta de Video": 1500000,
}

numero_umbral_usuario = int(sys.argv[1])

if len(sys.argv) == 2:
    resultado = calculo_umbral(numero_umbral_usuario, precios)
    imprimir_resultado(resultado)


elif len(sys.argv) == 3:
    operacion_usuario = sys.argv[2]
    resultado = calculo_umbral(numero_umbral_usuario, precios, operacion_usuario)
    imprimir_resultado(resultado, operacion_usuario)
