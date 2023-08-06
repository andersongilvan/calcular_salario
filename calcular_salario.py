# Programa que lê o salário de um funcionario e mostra o seu salário com aumento #

salario = float(input("Digite o seu salário!\n"))

aumento = (10 / 100) * salario
s = aumento + salario

aumento2 = (15 / 100) * salario
s2 = aumento2 + salario


if salario >= 1250:
    print(
        "Seu salário que era de {} RS teve um aumende 10% ! E agora é de {} RS".format(
            salario, s
        )
    )


else:
    print(
        "Seu salário que era de {} RS teve um aumento de 15% ! E agora é de {} RS".format(
            salario, s2
        )
    )
