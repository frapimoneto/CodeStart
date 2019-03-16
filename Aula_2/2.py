numeros = [] #cria uma lista vazia chamada numeros
num = 0;
while num != (-1): #enquanto o numero digitado for menor que -1
    num=int(input("Digite um número: ")) #salva o numero digitado
    numeros.append(num) #adiciona o numero digitado na lista
numeros.pop(-1) #retira o valor -1 da lista
print("Maior valor:",max(numeros)) #mostra o maior valor
print("Menor valor:",min(numeros)) #mostra o menor valor