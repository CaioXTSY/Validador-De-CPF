def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11:
        return False
    
    if cpf == cpf[0] * 11:
        return False
    
    # Primeiro digito
    total = 0
    for i in range(9):
        total += int(cpf[i]) * (10 - i)
    resto = total % 11
    d1 = 0 if resto < 2 else 11 - resto

    # Segundo digito
    total = 0
    for i in range(10):
        total += int(cpf[i]) * (11 - i)
    resto = total % 11
    d2 = 0 if resto < 2 else 11 - resto

    return cpf[-2:] == f"{d1}{d2}"