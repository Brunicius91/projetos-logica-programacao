from re import A

num1 = int(input("Digite o primeiro número: ")) # Recebe o valor do primeiro número e convertendo em int

operacao = (input("Escolha a operação desejada (+ - * /): ")) # Usuário escolhe qual tipo de operação deseja efetuar

num2 = int(input("Digite o segundo número: ")) # Recebe o valor do segundo número e convertendo em int

if operacao == '+': #
	adi = num1 + num2
	print("Resultado: ",adi)
elif operacao == '-':
	sub = num1 - num2
	print("Resultado: ",sub)
elif operacao == '*':
	mul = num1 * num2
	print("Resultado: ", mul)
elif operacao == '/':
	div = num1 / num2
	print("Resultado: ",div)
