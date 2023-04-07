def error(s):
    print(s)
    exit(1)


def decode(arr):
    if (len(arr) != 12):
        return "Invalid input"
    for i in range(12):
        if (len(arr[i]) != 11):
            return "Invalid input"
    for i in range(12):
        for j in range(11):
            if (arr[i][j] != "0" and arr[i][j] != "1"):
                return "Invalid input"
    (arr)
    integers = [int(i, 2) for i in arr]
    (integers)
    words = []
    for integer in integers:
        if (integer == 0 or integer > 2048):
            return "Invalid input"
        with open('word_list.txt', 'r') as f:
            lines_in_file = open("word_list.txt", 'r').readlines()
            if (len(lines_in_file) == 0):
                error("Errore: file vuoto")
            if (len(lines_in_file) > 2048):
                error("Errore: file con più di 2048 righe")
            count = 1
            for line in lines_in_file:
                line = line.strip()
                if (count == integer):
                    words.append(line)
                count += 1
    (words)