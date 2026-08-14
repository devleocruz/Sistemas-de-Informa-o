from desafio1 import ePar

def testa_ePar():
    assert ePar(100) == True

def testa_eImpar():
    assert ePar(45) == False

def testa_eImpar_negativo():
    assert ePar(-5) == False

def testa_0_ePar():
    assert ePar(0) == True