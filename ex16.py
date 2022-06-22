def somaImposto(taxaImposto, Custo):
    return (1 + taxaImposto/100)*Custo
t = float(input('Digite a taxa do imposto: '))
c = float(input('Digite o custo: '))
print('Valor com imposto é igual a :', somaImposto(t, c))