numero1 = []
quadrado = []
mulp = 0

for p in range(10):
        numero1.append(int(input("Digite um número que seja inteiro: ")))
for e in numero1:
        mulp = mulp + numero1[p] ** 2
        quadrado.append(mulp)

print('Os números da lista são: ', numero1)
print('A soma dos número elevados ao quadrado são: ', mulp)

