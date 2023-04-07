import sys
import draw

def error(s):
    print(s)
    exit(1)

bip_word = []

with open('word_list.txt', 'r') as f:
    lines_in_file = open("word_list.txt", 'r').readlines()
    if (len(lines_in_file) == 0):
        error("Errore: file vuoto")
    if (len(lines_in_file) > 2048):
        error("Errore: file con più di 2048 righe")
    for line in lines_in_file:
        line = line.strip()
        bip_word.append(line)

if __name__ == "__main__":
    argv = sys.argv[1:]
    argc = len(argv)
    if (argc != 12):
        error("Errore: numero di argomenti non valido")
    index_of_words = []
    binary_of_index = []
    word_list = argv
    for word in word_list:
        index_of_words.append(bip_word.index(word) + 1)
        last = len(index_of_words) - 1
        binary = bin(int(index_of_words[last])).replace("0b", "")
        if (len(binary) < 11):
            binary = binary.zfill(11)
        binary_of_index.append(binary)
    draw.draw(binary_of_index)