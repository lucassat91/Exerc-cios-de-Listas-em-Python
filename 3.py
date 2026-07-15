# 3. Lista de 1 a 10, mostrar apenas os pares (list comprehension)

numeros_1_a_10 = list(range(1, 11))
pares = [n for n in numeros_1_a_10 if n % 2 == 0]
 
print(f"Lista original: {numeros_1_a_10}")
print(f"Números pares: {pares}")
print()