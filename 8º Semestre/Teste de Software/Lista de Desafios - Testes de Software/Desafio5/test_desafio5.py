import pytest
from unittest.mock import Mock
from desafio5 import esta_em_horario_comercial


@pytest.fixture
def relogio():
    return Mock()


@pytest.mark.parametrize(
    "hora, esperado",
    [
        (7, True),
        (8, True),
        (12, True),
        (17, False),
        (18, False),
        (23, False),
    ],
)
def test_horario_comercial(relogio, hora, esperado):
    relogio.now.return_value.hour = hora

    assert esta_em_horario_comercial(relogio) == esperado