revenue = float(input('Введите выручку: '))
costs = float(input('Введите издержки: '))
profit = 0.00

if revenue > costs:
    profit = (revenue - costs) / revenue
    print(f'У вас в компании хорошие дела! Рентабельность составляет: {profit:.2f}')
    count_persons = int(input('Сколько сотрудников у вас в компании: '))
    profit_person = profit / count_persons
    print(f'Прибыль на одного сотрудника составляет: {profit_person:.2f}')

else:
    print('В вашей компании дела плохи(')
