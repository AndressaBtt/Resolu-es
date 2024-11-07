# Solicita o peso e a altura do usuário
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# Calcula o IMC
imc = peso / (altura * 2)

# Exibe o resultado
print(f"Seu IMC é: {imc}")