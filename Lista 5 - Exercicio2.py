# Definindo os conjuntos de clientes
clientes_A = {"Ana", "Bruno", "Carla", "Diana", "João"}
clientes_B = {"Andressa", "Eduardo", "Fernanda", "Gustavo", "Helena"}

# Identificar os clientes que estão em ambos os conjuntos
clientes_em_ambos = clientes_A.intersection(clientes_B)
print("Clientes em ambos os conjuntos:", clientes_em_ambos)

# Identificar os clientes que estão apenas em clientes_A
clientes_somente_A = clientes_A.difference(clientes_B)
print("Clientes apenas em clientes_A:", clientes_somente_A)

# Identificar os clientes que estão em apenas um dos conjuntos
clientes_apenas_um = clientes_A.symmetric_difference(clientes_B)
print("Clientes em apenas um dos conjuntos:", clientes_apenas_um)

# Calcular a porcentagem de clientes únicos
total_clientes = len(clientes_A.union(clientes_B))
clientes_unicos = len(clientes_A.union(clientes_B)) - len(clientes_em_ambos)
porcentagem_unicos = (clientes_unicos / total_clientes) * 100
print(f"Porcentagem de clientes únicos: {porcentagem_unicos:.2f}%")