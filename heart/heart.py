# Importa a biblioteca math e a biblioteca Turtle
import math
from turtle import * 

# Define a função para a coordenada x do coração
def hearta(k):
    return 12*math.sin(k)**3

# Define a função para a coordenada y do coração
def heartb(k):
    return 12*math.cos(k)-5*\
    math.cos(2*k)-2*\
                math.cos(3*k)-\
                math.cos(4*k)

# Define a velocidade da tartaruga como a mais rápida possível e a cor de fundo da tela como preto
speed(0)
bgcolor("black")

# Loop que percorre um determinado número de vezes (10000 neste caso)
for i in range(10000):

# Move a tartaruga para as coordenadas x e y calculadas pelas equações hearta() e heartb()
    goto(hearta(i)*20, heartb(i)*20)

# Define a cor da caneta e move a tartaruga de volta para o centro da tela
    for j in range(5):
        color("#660000")
    goto(0,0)

# Mantém a janela gráfica aberta até que o usuário a feche
done()


'''
As funções hearta() e heartb() são as equações paramétricas que calculam as coordenadas x e y do coração para um determinado valor de k.

O valor de k é incrementado em um loop for que percorre um determinado número de vezes (10000 neste caso), e a posição é atualizada a cada iteração.

A função speed(0) define a velocidade da tartaruga como a mais rápida possível, e bgcolor("") define a cor de fundo da tela.

O loop for desenha o coração movendo a tartaruga para as coordenadas x e y calculadas pelas equações hearta() e heartb(). Em seguida, ele define a cor da caneta com (color("")) e move a tartaruga de volta para o centro da tela (goto(0,0)).

A função done() é usada para manter a janela gráfica aberta até que o usuário a feche.

Em resumo, este código desenha um coração usando equações paramétricas e a biblioteca gráfica Turtle.
'''