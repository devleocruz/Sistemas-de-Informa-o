from desafio2 import Calcular_IMC

def test_abaixo_do_peso():
    assert Calcular_IMC(30,1.60) == "Abaixo do Peso"

def test_peso_normal():
    assert Calcular_IMC(64,1.77) == "Peso normal (ideal)"

def test_sobrepeso():
    assert Calcular_IMC(70,1.60) == "Sobrepeso"

def test_obesidade_grau_I():
    assert Calcular_IMC(99,1.70) == "Obesidade grau I"

def test_obesidade_grau_II():
    assert Calcular_IMC(110,1.70) == "Obesidade grau II"

def test_obesidade_grau_III():
    assert Calcular_IMC(120,1.70) == "Obesidade grau III (grave)"    