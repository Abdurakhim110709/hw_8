import sqlite3



def get_cities(connection):
    try:
        sql = '''SELECT id, title FROM cities'''
        cursor = connection.cursor()
        cursor.execute(sql)
        cities = cursor.fetchall()
        return cities

    except sqlite3.Error as error:
        print(f'{error} in SELECT_ALL function')

def get_students(connection, city_id):
    try:
        sql = '''SELECT 
        students.first_name, students.last_name, 
        countries.title, 
        cities.title, cities.area 
        FROM students
        INNER JOIN cities ON students.city_id = cities.id
        INNER JOIN countries ON cities.country_id = countries.id
        WHERE cities.id = ?
        '''
        cursor = connection.cursor()
        cursor.execute(sql,(city_id,))
        students = cursor.fetchall()
        return students

    except sqlite3.Error as error:
        print(f'{error} in SELECT_ALL function')

my_connection = sqlite3.connect('hw.db')
if my_connection:
    a = get_cities(my_connection)
    print('Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:')

    for i in a:
        print(f'{i[0]}. {i[1]}')

    while True:
        c_id = int(input('ведите id города: '))
        if c_id == 0:
            print('Выход')
            break

        elif c_id > 7 or c_id < 1:
            print('нет такого города под таким id! ')

        else:
            s = get_students(my_connection, c_id)
            print('список студентов проживающих в этом городе')
            for i in s:
                print(f'FULL NAME: {i[0]} {i[1]}, Country: {i[2]}, City: {i[3]}, City area: {i[4]}')
