def Calcular_IMC(peso, altura):
    valor = peso/(altura**2)

    match valor:
        case valor if valor < 18.5:
            return "Abaixo do Peso"
        case v if 18.5 <= v < 24.99:
            return "Peso normal (ideal)"
        case v if 25.0 <= v < 29.99:
            return "Sobrepeso"
        case v if 30.0 <= v < 34.99:
            return "Obesidade grau I"
        case v if 35.0 <= v < 39.99:
            return "Obesidade grau II"
        case _:
            return "Obesidade grau III (grave)"