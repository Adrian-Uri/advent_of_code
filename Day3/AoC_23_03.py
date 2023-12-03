import re

file_path = 'inputs/day3.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()


def comprobarPosi(x,y):

    mapa = []
    i=0
    for linea in lines:
        linea = linea.strip()
        mapa.append([])
        for char in linea:
            mapa[i].append(char)
        i = i + 1
    # candidatos = [mapa[x-1][y-1],mapa[x-1][y],mapa[x-1][y+1],mapa[x][y-1],mapa[x][y+1],mapa[x+1][y-1],mapa[x+1][y],mapa[x+1][y+1]]

    adjacent_elements = []

    for i_offset in range(-1, 2):
        for j_offset in range(-1, 2):
            new_row, new_col = x + i_offset, y + j_offset
            # Check if the new indices are within bounds
            if 0 <= new_row < len(mapa) and 0 <= new_col < len(mapa[0]):
                print(new_row,new_col)
                print(mapa)
                adjacent_elements.append(mapa[new_row][new_col])
    print(adjacent_elements)
    for elemento in adjacent_elements:
        if not elemento.isdigit() and not (elemento == '.'):
            return True






def part_one():
    x=-1
    y=-1
    numActual = ''
    posicionesQueCheckear=[]
    solu=0
    for linea in lines:
        x=x+1
        y=-1
        for elemento in linea:
            print(elemento)
            y=y+1
            if elemento.isdigit():
                print("entro en A")
                numActual= numActual + elemento
                posicionesQueCheckear.append([x,y])
                print("Numero actual es "+ numActual)
                print("las posicionesQueCheckear son "+ str(posicionesQueCheckear))
            elif numActual:
                print(("Entro en B"))
                for elemento in posicionesQueCheckear:
                    if (comprobarPosi(elemento[0],elemento[1])):
                        print("Efectivamente, pega con un elemento")
                        print("Aumento la solu de "+ str(solu) +" en "+ str(numActual))
                        solu= solu + int(numActual)
                        numActual=0
                print("Hago Reset del numero actual y de las posiciones a comprobar")
                numActual = ''
                posicionesQueCheckear = []

    print(solu)






part_one()