def funcao1 (n):
    for i in range(n):
        i += 1
        print(str(i) * i)

n = int(input('Digite um número: '))
funcao1(n)
