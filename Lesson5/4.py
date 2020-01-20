rus_numbers = ['Один', 'Два', 'Три', 'Четыре']
i = 0
out_f = open('out.txt', 'w')
with open('text1.txt') as f_obj:
    for line in f_obj:
        new_line = line.split('-')
        new_line[0] = rus_numbers[i]
        out_f.write(' -'.join(new_line))
        i += 1
out_f.close()
