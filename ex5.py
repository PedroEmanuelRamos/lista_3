nVetor = []
jVetor = []
rVetor = []

for p in range(10):
     nVetor.append(input("Digite o número da " + str(p + 1) + "ª posição do 1ª vetor: "))
print('-----'*20)
for o in range(10):
     jVetor.append(input("Digite o número da " + str(o + 1) + "ª posição do 2ª vetor: "))
print('-----'*20)
for d in range(10):
     rVetor.append(nVetor[d])
     rVetor.append(jVetor[d])
print('-----'*20)
print(rVetor)
