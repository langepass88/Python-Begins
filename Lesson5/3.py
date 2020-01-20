average = 0.00
lines = 0
with open('workers.txt') as f_obj:
    for line in f_obj:
        lines += 1
        my_list = line.split()
        average += float(my_list[1])
        if float(my_list[1]) < 20000:
            print(line)
average = average / lines
print(f'Средняя величина дохода сотрудников: {average:.2f}')
