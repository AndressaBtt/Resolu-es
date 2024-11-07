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

# Função para exibir a pirâmide de números primos
def piramide_primos(N, crescente=True):
    # Lista para armazenar os números primos
    primos = [num for num in range(1, N + 1) if eh_primo(num)]
    
    # Ordena os números primos em ordem crescente ou decrescente
    if not crescente:
        primos = primos[::-1]

    # Construção da pirâmide
    linhas = 1
    index = 0
    while index < len(primos):
        # Exibe a linha atual da pirâmide
        print(" ".join(map(str, primos[index:index + linhas])))
        index += linhas
        linhas += 1

# Chama a função para exibir a pirâmide de números primos
piramide_primos(N, crescente=True)  
