'''
Faca um programa em Python que recebe tres
numeros e calcule sua media.
'''

# Recebe os numeros do teclado:
n1 = input ("Informe o primeiro numero: ")
n2 = input ("Informe o segundo numero: ")
n3 = input ("Informe o terceiro numero: ")

# Converte para numerico:
n1 = float (n1)
n2 = float (n2)
n3 = float (n3)

# Escreve a media na tela:
media = (n1 + n2 + n3) / 3.0
print (media)
