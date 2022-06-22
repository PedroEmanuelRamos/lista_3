vetor = []
mult = 1
soma = 0

for e in range(5):
    vetor.append(int(input('Digite os números: ')))

for p in vetor:
     soma += p
     mult *= p

print('A soma de todos os números é: ', soma)
print('A multiplicação de todos os números é: ', mult)
print(vetor)