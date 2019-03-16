import turtle #Importa a biblioteca Turtle
t = turtle.Pen() #Inicializa a caneta
turtle.bgcolor('gray') #Altera a cor do fundo
turtle.title("Titulo") #Coloca o título da janela
sides = 6 #Seleciona o número de lados da figura
colors = ['red', 'yellow', 'blue', 'orange', 'purple', 'black'] #Passa a lista de cores que serão usadas
for x in range(360): #Estrutura de repetição
    t.pencolor(colors[x%sides])  # Alterna entre 6 cores
    t.forward(x * 3/sides + x) # Aumenta raio do desenho
    t.left (360/sides + 1) # Gira 360/sides e adiciona p/ espiral
    t.width (x*sides/200) # Aumenta a largura do traço