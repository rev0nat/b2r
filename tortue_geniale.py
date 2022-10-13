import turtle
import re

t = turtle.Turtle()

def draw(inputt):
    input_list = inputt.split("\n")
    for i in input_list:
        if not i:
            continue
        nb = int(re.findall(r'\d+',i)[0])
        print(i, nb)
        if "gauche" in i:
                t.left(nb)
        elif "droite" in i:
                t.right(nb)
        elif "Avance" in i:
                t.forward(nb)
        elif "Recule" in i:
                t.backward(nb)

with open("text_tortue", 'r') as f:
    inputt = f.read()
    draw(inputt)
