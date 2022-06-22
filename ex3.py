idade = []
altura = []
p = 0

for p in range(5):
    print(p+1, ' - Pessoa')
    altura.append(float(input("Qual é a altura da pessoa? ")))
    idade.append(int(input('Qual é a idade da pessoa? ')))

print('idade normal', idade)
print('idade iversa', (idade[:-1]))
print('altura normal', altura)
print('altura inversa', (altura[:-1]))