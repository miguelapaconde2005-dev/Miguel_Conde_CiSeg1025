notas = []
for i in range(10):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    notas.append(nota)

media = sum(notas) / 10
acima_media = sum(1 for n in notas if n >= media)

print(f"Média da turma: {media:.2f}")
print(f"Alunos com nota igual ou acima da média: {acima_media}")
