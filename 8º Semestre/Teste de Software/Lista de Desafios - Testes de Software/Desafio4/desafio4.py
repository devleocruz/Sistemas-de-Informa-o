def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "").strip()

    if len(cpf) != 11 or not cpf.isdigit():
        return False

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto

    if digito1 != int(cpf[9]):
        return False

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto

    if digito2 != int(cpf[10]):
        return False

    return True