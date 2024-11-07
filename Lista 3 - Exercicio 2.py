# Solicita o número N do usuário
N = int(input("Digite um número inteiro N: "))

# Função para verificar se um número é primo
def eh_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Lista para armazenar os números primos
primos = []

# Itera de 1 até N e adiciona os números primos à lista
for num in range(1, N + 1):
    if eh_primo(num):
        primos.append(num)

# Exibe os números primos encontrados
print(f"Números primos entre 1 e {N}: {primos}")
