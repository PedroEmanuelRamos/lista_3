def funcao(n):
    for p in range(1, n + 1):
        cont = 1
        while True:
            print(p, end=' ')
            if cont == p:
                break
            cont += 1
        print()
n = int(input('Digite um número: '))
funcao(n)