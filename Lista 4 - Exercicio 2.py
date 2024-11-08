def imprimir_piramide(N, crescente=True):
    for i in range(1, N + 1):
        # Calcular os espaços para o alinhamento da pirâmide
        espacos = " " * (N - i)
        
        # Criar a lista de números para a linha
        if crescente:
            # Números crescentes
            numeros = list(range(1, i + 1))
        else:
            # Números decrescentes
            numeros = list(range(i, 0, -1))
        
        # Imprimir a linha com os espaços e os números
        print(espacos + " ".join(map(str, numeros)))

# Solicitar o número N ao usuário
N = int(input("Digite o número N (altura da pirâmide): "))
crescente = input("Deseja uma pirâmide crescente (sim ou não)? ").strip().lower() == "sim"

# Imprimir a pirâmide com o parâmetro crescente
imprimir_piramide(N, crescente)
