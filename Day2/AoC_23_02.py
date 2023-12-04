import re

file_path = 'inputs/day2.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()

def part_one():
    def separar_juegos (cadena):
        games = cadena.split(';')
        return games
    ngame=0
    sumatorio = 0
    for game in lines:
        topRed=0
        topGreen=0
        topBlue=0

        ngame=ngame+1
        #print(ngame)
        rondas = separar_juegos(game)
        for ronda in rondas:
            ronda = ronda.strip()
            ronda = (re.sub(".*: ",'',ronda))
            turnos = ronda.split(', ')
            for cubo in turnos:
                splited = cubo.split()
                if splited [1] == 'blue' and int(splited[0]) > int(topBlue):
                    topBlue = int(splited[0])
                if splited [1] == 'red' and int(splited[0]) > int(topRed):
                    topRed = int(splited[0])
                if splited [1] == 'green' and int(splited[0]) > int(topGreen):
                    topGreen = int(splited[0])
        if int(topRed) <= 12 and int(topGreen) <= 13 and int(topBlue) <= 14:
            sumatorio = sumatorio + ngame

    return (sumatorio)


def part_two():
    def separar_juegos (cadena):
        games = cadena.split(';')
        return games
    ngame=0
    sumatorio = 0
    for game in lines:
        topRed=0
        topGreen=0
        topBlue=0

        ngame=ngame+1
        #print(ngame)
        rondas = separar_juegos(game)
        for ronda in rondas:
            #print(ronda)
            ronda = ronda.strip()
            ronda = (re.sub(".*: ",'',ronda))
            turnos = ronda.split(', ')
            for cubo in turnos:
                splited = cubo.split()
                if splited [1] == 'blue' and int(splited[0]) > int(topBlue):
                    topBlue = int(splited[0])
                if splited [1] == 'red' and int(splited[0]) > int(topRed):
                    topRed = int(splited[0])
                if splited [1] == 'green' and int(splited[0]) > int(topGreen):
                    topGreen = int(splited[0])


        #print(topRed,topBlue,topGreen)
        power = topRed*topBlue*topGreen
        sumatorio = sumatorio +power
    return sumatorio

print("La solución de la parte uno es "+str(part_one()))
print("La solución de la parte dos es "+str(part_two()))