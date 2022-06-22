matriz=[[0,0,0],[0,0,0],[0,0,0]]

for p in range(3):
       for e in range(3):
        matriz[p]= int(input('Digite o "elemento":  [' + str(p) + ']['+ str(e) +']: '))
        matriz[e] = int(input('Digite o "elemento":  [' + str(p) + '][' + str(e) + ']: '))
print('\n')
v=int(input('Digite um número para multiplicar os elementos da diagonal principal: '))
for p in range(3):
       for e in range(3):
          if p==e:
            matriz[p] = v*matriz[p]
            matriz[e] = v*matriz[e]
print(matriz)