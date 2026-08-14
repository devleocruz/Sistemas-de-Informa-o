import pytest
from desafio4 import validar_cpf


@pytest.mark.parametrize(
    "cpf, esperado",
    [
        ("529.982.247-25", True),
        ("52998224725", True),
        ("111.111.111-11", True),
        ("123.456.789-09", True),

        ("123.456.789-00", False),
        ("123456789", False),
        ("5299822472", False),
        ("abc.def.ghi-jk", False),
    ],
)
def test_validar_cpf(cpf, esperado):
    assert validar_cpf(cpf) == esperado

#A entrada 111.111.111-11 passa no teste porque os dígitos verificadores estão matematicamente corretos.
# Porém, esse CPF é um exemplo de sequência repetida e pode ser considerado inválido para uma aplicação real.
# Isso mostra que um teste passar não significa que o sistema não possui defeitos: os testes verificam apenas os casos que foram definidos.
# Se não testarmos regras adicionais, como rejeitar números repetidos, um problema pode permanecer oculto.