import pytest
from desafio3 import calcular_raiz_quadrada

def test_raiz_quadrada_valida():
    assert calcular_raiz_quadrada(9) == 3

def test_raiz_quadrada_numero_negativo():
    with pytest.raises(ValueError, match="Não é possível calcular a raiz de número negativo"):
        calcular_raiz_quadrada(-4)

def test_raiz_quadrada_outro_negativo():
    with pytest.raises(ValueError) as erro:
        calcular_raiz_quadrada(-25)
    assert "-25" in str(erro.value)