# 5. Remover duplicados mantendo a ordem
 
def remover_duplicados(lista):
    vistos = []  # usado como registro, não como set()
    resultado = []
 
    for item in lista:
        if item not in vistos:
            vistos.append(item)
            resultado.append(item)
 
    return resultado
 
 
entrada = [4, 2, 7, 2, 9, 4, 1, 7]
saida = remover_duplicados(entrada)
print(saida)  # [4, 2, 7, 9, 1]
 
print(remover_duplicados([1, 1, 1, 1]))       # [1]
print(remover_duplicados([5, 3, 5, 2, 3]))    # [5, 3, 2]
print()
 