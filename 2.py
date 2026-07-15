# 2. Pedir 3 nomes ao usuário e armazenar em uma lista

nomes = []
for i in range(3):
    nome = input(f"Digite o nome {i + 1}: ")
    nomes.append(nome)
 
print(f"Nomes armazenados: {nomes}")
print()