# Solicita os dois números do usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Solicita o operador
operador = input("Digite o operador (+, -, *, /): ")

# Realiza a operação com base no operador fornecido
if operador == '+':
    resultado = num1 + num2

elif operador == '-':
    resultado = num1 - num2

elif operador == '*':
    resultado = num1 * num2
    
elif operador == '/':
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: Divisão por zero!"
else:
    resultado = "Operador inválido!"

# Exibe o resultado
print(f"O resultado é: {resultado}")