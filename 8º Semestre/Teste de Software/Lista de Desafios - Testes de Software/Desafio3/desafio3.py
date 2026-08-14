def calcular_raiz_quadrada(numero):
    if not isinstance(numero, (int, float)):
        raise TypeError("A entrada deve ser um número.")
    if numero < 0:
        raise ValueError(f"Não é possível calcular a raiz de número negativo: {numero}")
    return numero ** (1/2)