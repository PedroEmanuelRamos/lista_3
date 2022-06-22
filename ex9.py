nome = input("Digite um nome qualquer : ")
print(input("Digite o nome mais uma vez : "), sep="\n")
p = len(nome)+1
for e in range(p):
    print(nome[:e])