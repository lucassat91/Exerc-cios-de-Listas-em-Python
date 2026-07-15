# 4. Médias e classificação de alunos

alunos = [
    ["Lucas", [10, 8, 9]],
    ["Rafael", [4, 7, 9]],
    ["Carlos", [10, 10, 9]],
]
 
aprovados = []
recuperacao = []
reprovados = []
 
for aluno in alunos:
    nome = aluno[0]
    notas = aluno[1]
    media = sum(notas) / len(notas)
    media = round(media, 1)
 
    if media >= 7:
        aprovados.append([nome, media])
    elif media >= 5:
        recuperacao.append([nome, media])
    else:
        reprovados.append([nome, media])
 
print(f"Aprovados: {aprovados}")
print(f"Recuperação: {recuperacao}")
print(f"Reprovados: {reprovados}")
print()
 