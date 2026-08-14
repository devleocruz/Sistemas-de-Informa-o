from datetime import datetime


def esta_em_horario_comercial(relógio=datetime):
    hora = relógio.now().hour

    return 7 <= hora < 17