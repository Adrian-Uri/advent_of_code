file_path = 'inputs/day1.txt'

def find_and_convert_numbers(input_str):
    # Define a mapping from words to numerical values
    number_mapping = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10}

    # Split the input string into words
    words = input_str.split()

    # Iterate through the words and replace written numbers with numerical values
    for i in range(len(words)):
        word = words[i].lower()  # Convert to lowercase for case-insensitivity
        if word in number_mapping:
            words[i] = str(number_mapping[word])

    # Join the words back into a string
    converted_str = ' '.join(words)
    return converted_str


def part_one():
    lineas = []

    with open(file_path, 'r') as file:
        lines = file.readlines()
        i = -1
        for line in lines:
            line2 = find_and_convert_numbers(line)
            i = i + 1
            lineas.append([])
            for char in line:
                lineas[i].append(char)

    res = []
    i = -1
    for linea in lineas:
        res.append([])
        i = i + 1
        for char in linea:
            if str(char).isnumeric():
                res[i].append(char)

    final = 0
    for cadena in res:
        parcial = int(cadena[0] + cadena[-1])
        final = final + parcial

    return final

def part_two():
    res = 0
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    with open('inputs/day1.txt', 'r') as f:
        for line in f:
            first_digit, last_digit = -1, -1
            line = line.strip()
            for i in range(len(line)):
                if line[i].isdigit():
                    if first_digit == -1:
                        first_digit = int(line[i])
                    last_digit = int(line[i])
                else:
                    for w in range(len(words)):
                        word_length = len(words[w]) - 1
                        if i - word_length >= 0 and line[i - word_length:i + 1] == words[w]:
                            if first_digit == -1:
                                first_digit = w + 1
                            last_digit = w + 1
            res += (first_digit * 10) + last_digit
    return res


print("La solución de la parte uno es "+str(part_one()))
print("La solución de la parte dos es "+str(part_two()))
