# Leitura e declaração das variáveis:
# "salario", que representa o salário;
# "reajustePercentual", que representa o reajuste percentual.
salario = float(input("Digite o valor do sálario: "))
reajustePercentual = float(input("Digite o valor do reajuste: "))

# Cálculo e declaração da variável "salarioFinal", que representa o salário final
salarioFinal = ((salario * reajustePercentual)/100 + salario)

# Imprimir a variável "salarioFinal"
print("O sálario final é: R$", salarioFinal)
