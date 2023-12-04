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
                adjacent_elements.append(mapa[new_row][new_col])
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
            y=y+1
            if elemento.isdigit():
                numActual= numActual + elemento
                posicionesQueCheckear.append([x,y])
            elif numActual:
                for elemento in posicionesQueCheckear:
                    if (comprobarPosi(elemento[0],elemento[1])):
                        solu= solu + int(numActual)
                        numActual=0
                numActual = ''
                posicionesQueCheckear = []

    return solu


def encontrar_numero_completo(matriz, fila, col):
    if 0 <= fila < len(matriz) and 0 <= col < len(matriz[0]):
        numero_actual = matriz[fila][col]

        # Caso base: Parar en el .
        if not numero_actual.isdigit():
            return "", None  # Devolvemos una tupla con la cadena vacía y la posición inicial

        # Marcar como visitada
        matriz[fila][col] = "."

        izquierda, pos_inicial_izquierda = encontrar_numero_completo(matriz, fila, col - 1)
        derecha, pos_inicial_derecha = encontrar_numero_completo(matriz, fila, col + 1)

        # Revertir cambios
        matriz[fila][col] = numero_actual

        # Devolver el número completo expandiéndose a la izquierda y derecha
        numero_completo = izquierda + str(numero_actual) + derecha

        # Devolver la cadena y la posición inicial
        if pos_inicial_izquierda is not None:
            return numero_completo, pos_inicial_izquierda
        elif pos_inicial_derecha is not None:
            return numero_completo, pos_inicial_derecha
        else:
            return numero_completo, (fila, col)

    # Devolver una cadena vacía y None si la posición está fuera de los límites
    return "", None



# def obtenerPrimeraPosicion(tuplas):
#     print (tuplas)
#     combinaciones_mas_bajas = {}
#
#     for numero_completo, posicion in tuplas:
#         if numero_completo not in combinaciones_mas_bajas or posicion < combinaciones_mas_bajas[numero_completo][1]:
#             combinaciones_mas_bajas[numero_completo] = (numero_completo, posicion)
#
#     # Filtrar duplicados basados en el número completo
#     combinaciones_unicas = {v[0]: v for v in combinaciones_mas_bajas.values()}
#
#     return list(combinaciones_unicas.values())


def obtenerPrimeraPosicion(tuplas):
    valores_mas_bajos = {}

    for identificador, posicion in tuplas:
        valor_y = posicion[1]
        valor_x = posicion[0]

        if identificador not in valores_mas_bajos or (
                valor_y < valores_mas_bajos[identificador][1] and valor_x != valores_mas_bajos[identificador][0]):
            valores_mas_bajos[identificador] = (valor_x, valor_y)
    #print(valores_mas_bajos)
    return list(valores_mas_bajos.items())





def multiplicarGear(x,y):
    mapa = []
    i=0
    for linea in lines:
        linea = linea.strip()
        mapa.append([])
        for char in linea:
            mapa[i].append(char)
        i = i + 1
    numerosActuales =[]
    for i_offset in range(-1, 2):
        for j_offset in range(-1, 2):
            new_row, new_col = x + i_offset, y + j_offset
            # Check if the new indices are within bounds
            if 0 <= new_row < len(mapa) and 0 <= new_col < len(mapa[0]):
                if mapa[new_row][new_col].isdigit():
                    numerosActuales.append(encontrar_numero_completo(mapa,new_row,new_col))

    #print(numerosActuales)
    numerosGear=(obtenerPrimeraPosicion(numerosActuales))
    solu=1
    if len(numerosGear) == 2:
        for elemento in numerosGear:
            solu = solu*int(elemento[0])
    else:
        solu=0
    return (solu)

def part_two():
    x = -1
    y = -1
    numActual = ''
    posicionesQueCheckear = []

    solu = 0
    for linea in lines:
        x = x + 1
        y = -1
        for elemento in linea:
            y = y + 1
            if elemento == "*":
                #print(x,y)
                solu = solu + multiplicarGear(x,y)

    return solu


print("La solución de la parte uno es "+str(part_one()))
print("La solución de la parte dos es "+str(part_two()))