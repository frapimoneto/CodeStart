def fatorial(x): #cria uma função chamada fatorial
    if x<=1: #caso o numero digitado for menor ou igual a 1
        return 1 retorna 1
    else: #senao
        return x * fatorial(x-1) #retorna o resultado da função recursiva