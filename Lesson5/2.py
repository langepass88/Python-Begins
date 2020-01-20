lines = 0
with open('text.txt') as f_obj:
    for line in f_obj:
        lines += 1
        print(f'Кол-во символов в строке {lines}: {len(line) - 1}\n')
print(f'Кол-во строк в файле: {lines}')
