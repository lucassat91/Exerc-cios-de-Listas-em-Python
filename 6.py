# 6. Maior sequência crescente contínua
 
def maior_sequencia_crescente(lista):
    if not lista:
        return []
 
    maior_seq = [lista[0]]
    seq_atual = [lista[0]]
 
    for i in range(1, len(lista)):
        if lista[i] > lista[i - 1]:
            seq_atual.append(lista[i])
        else:
            seq_atual = [lista[i]]
 
        if len(seq_atual) > len(maior_seq):
            maior_seq = seq_atual[:]  # copia a sequência atual
 
    return maior_seq
 
 
numeros_seq = [3, 5, 7, 2, 4, 6, 8, 1, 9]
resultado = maior_sequencia_crescente(numeros_seq)
print(resultado)  # [2, 4, 6, 8]
 
print(maior_sequencia_crescente([1, 2, 3, 4]))       # [1, 2, 3, 4]
print(maior_sequencia_crescente([5, 4, 3, 2]))       # [5]
print(maior_sequencia_crescente([1, 3, 5, 2, 4, 6]))  # [1, 3, 5]
print()
 
 
# --- Desafio extra: retornar também índice inicial, final e tamanho ---
def maior_sequencia_crescente_completa(lista):
    if not lista:
        return [], -1, -1, 0
 
    melhor_inicio = 0
    melhor_fim = 0
    melhor_tamanho = 1
 
    inicio_atual = 0
 
    for i in range(1, len(lista)):
        if lista[i] > lista[i - 1]:
            tamanho_atual = i - inicio_atual + 1
            if tamanho_atual > melhor_tamanho:
                melhor_tamanho = tamanho_atual
                melhor_inicio = inicio_atual
                melhor_fim = i
        else:
            inicio_atual = i
 
    sequencia = lista[melhor_inicio:melhor_fim + 1]
    return sequencia, melhor_inicio, melhor_fim, melhor_tamanho
 
 
print("Desafio extra:")
print(maior_sequencia_crescente_completa([3, 5, 7, 2, 4, 6, 8, 1, 9]))
# ([2, 4, 6, 8], 3, 6, 4)