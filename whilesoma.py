print()

print("Digite uma sequência de valores quaisquer para somar, digite zero para parar e somar.")

print()

soma = 0

valor = 1

while valor != 0:
	
	valor = int(input("Digite um valor a ser somado: "))

	soma = soma + valor

print()

print("A soma dos valores digitados é", soma, ".")