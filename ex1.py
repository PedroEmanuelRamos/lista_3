mediasAlunos = []
alunosAcimaDaMedia = 0

for aluno in range(10):
    somaDasNotas = 0

    print(aluno + 1, '- aluno ')
    for nota in range(4):
        somaDasNotas += float(input("Digite a nota do aluno: "))

    mediasAlunos.append(somaDasNotas / 4)

    if mediasAlunos[aluno] >= 7:
        alunosAcimaDaMedia += 1

print('O número de alunos que ficaram acima da média é de: ', alunosAcimaDaMedia)