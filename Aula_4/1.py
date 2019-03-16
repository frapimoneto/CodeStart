import turtle #Importa a biblioteca Turtle
t = turtle.Pen() #Inicializa a caneta
turtle.bgcolor('black') #Altera a cor do fundo
turtle.title("Titulo") #Coloca o título da janela
circulos = 4 #Seleciona o número de circulos
colors = ['red', 'yellow', 'blue', 'orange'] #Passa a lista de cores que serão usadas
for x in range(360): #Estrutura de repetição
    t.pencolor(colors[x%circulos])  # Alterna entre 6 cores
    t.circle(x * 3/circulos + x) # Aumenta raio do desenho
    t.left (360/circulos + 1) # Gira 360/circulos e adiciona p/ espiral
    t.width (x*circulos/200) # Aumenta a largura do traço