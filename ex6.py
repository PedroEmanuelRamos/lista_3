string1 = str(input('Digite uma frase: ')).strip()
string2 = str(input('Digite mais uma frase: ')).strip()

print("A 1ª frase tem {} letras." .format(len(string1)))
print("A 2ª frase tem {} letras." .format(len(string2)))

if len(string1) != len(string2):
     print("As duas frases são de tamanhos diferentes.")
else:
     print("As duas frases são do mesmo tamanho.")
if string1 != string2:
     print("As duas strings possuem conteúdos difentes.")
else:
     print("As duas frases possuem o mesmo conteúdo.")