

def user_info(user_name, user_surname, user_city, user_year, user_mail, user_number):
    return f'Привет, {user_name} {user_surname}. ' \
           f'Ты живешь в г.{user_city}. ' \
           f'Ты {user_year} года рождения. ' \
           f'Твой e-mail: {user_mail}. ' \
           f'Номер телефона: {user_number}'


print(user_info(user_name='Сергей',
                user_surname='Романов',
                user_city='Вологда',
                user_year='1988',
                user_mail='blog.langepass@gmail.com',
                user_number='+79315006244'))
