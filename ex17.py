def funcao(a, b):
    if a > 20:
        a = 20
    if b > 20:
        b = 20
    print('-=-'*a)
    c =0
    while c < a:
        x = '|'
        print(f'{x}{x:>{(a*3 - 1)}}')
        c += 1
    print('-=-' * a)

a= int(input("Sua largura é: "))
b= int(input("Sua altura é: "))
funcao(a, b)