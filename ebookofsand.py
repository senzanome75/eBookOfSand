import random

simbols_of_ebook = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'z', ',', '.', ' ']
numbers_of_simbols = len(simbols_of_ebook)

row = ''


for i in range(40):
    for j in range(80):
        row += simbols_of_ebook[random.randrange(0, numbers_of_simbols - 1)]
    row += '\n'

print(row)
