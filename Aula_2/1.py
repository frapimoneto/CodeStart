n= int(input("Digite a quantidade de números: "))#pede a quantidade de numeros para calcular a média
soma=0
media =0
for i in range(n): #cria um laço de repetição de 0 até o numero digitado de vezes
    num = int(input("Digite um número: ")) #pede umnúmero
    soma += num #realiza a soma dos números
media = soma/n #calcula a média
print("O valor da média é: ", media) #Mostra o valor calculado