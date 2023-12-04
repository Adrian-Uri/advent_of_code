file_path = 'inputs/day4.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()

def part_one(lines = lines):
    solu=0
    for tarjeta in lines:
        #print(tarjeta)
        cadenaNumeros = tarjeta.strip().split(":")[1].split("|")
        numerosJugador= cadenaNumeros[1].split()
        numerosPremiados = cadenaNumeros[0].split()

        elementosComunes= set(numerosJugador) & set(numerosPremiados)
        if len (elementosComunes) != 0:
            solu=solu +  pow(2,(len(elementosComunes)-1))
    return solu

def part_two(lines = lines):
    solu = 0
    i=0
    tarjetasIndividuales = []
    for tarjeta in lines:
        cadenaNumeros = tarjeta.strip().split(":")[1].split("|")
        tarjetasIndividuales.append(cadenaNumeros)
        i = i+1
    poolRestantes= {}
    for i in range(0,len(tarjetasIndividuales)):
        poolRestantes[i] = 1

    posTarjeta=0
    for tarjeta in tarjetasIndividuales:
        numerosJugador = tarjeta[1].split()
        numerosPremiados = tarjeta[0].split()
        elementosComunes = set(numerosJugador) & set(numerosPremiados)
        premios = len(elementosComunes)
        for n in range(1,premios+1):
            poolRestantes[posTarjeta+n] = poolRestantes[posTarjeta+n] + poolRestantes[posTarjeta]


        posTarjeta=posTarjeta+1
    #print(poolRestantes)
    for tarjeta in poolRestantes:
        solu = solu + poolRestantes[tarjeta]

    return solu




print("La solución de la parte uno es "+str(part_one()))
print("La solución de la parte dos es "+str(part_two()))