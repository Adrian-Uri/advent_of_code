import re

file_path = 'inputs/day4.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()

def part_one(lines):
    solu=0
    for tarjeta in lines:
        print(tarjeta)
        cadenaNumeros = tarjeta.strip().split(":")[1].split("|")
        numerosJugador= cadenaNumeros[1].split()
        numerosPremiados = cadenaNumeros[0].split()

        elementosComunes= set(numerosJugador) & set(numerosPremiados)
        if len (elementosComunes) != 0:
            solu=solu +  pow(2,(len(elementosComunes)-1))
    return solu

def part_two(lines):
    solu = 0
    poolRestantes=[]
    for tarjeta in lines:
        print(tarjeta)
        cadenaNumeros = tarjeta.strip().split(":")[1].split("|")
        numerosJugador = cadenaNumeros[1].split()
        numerosPremiados = cadenaNumeros[0].split()

        elementosComunes = set(numerosJugador) & set(numerosPremiados)
        poolRestantes.append(elementosComunes)
        print(listelementosComunes)
        print(poolRestantes)

#print(part_one(lines))
part_two(lines)