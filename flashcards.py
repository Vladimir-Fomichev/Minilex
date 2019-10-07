import psycopg2
import random

# Нужно заполнить данные в скобках (название базы данных, имя пользователя, пароль, путь к серверу.
conn = psycopg2.connect(dbname='database_name', user='user_name', 
                        password='password', host='localhost')
cursor = conn.cursor()

i = 1
while 2 > i:
    tip = random.randint(1, 1000)
    cursor.execute('SELECT id, eng, score FROM top1000 WHERE id = %s', (tip,))
    result = cursor.fetchone()
    # После знака < можно задать количество правильных ответов, после которого слова уже не будут появляться.
    if result[2] < 1:
        print(result[1].upper())
        print ('-------')
            

        input('What is your answer? Press Enter to continue.')
        cursor.execute('SELECT id, rus FROM top1000 WHERE id = %s', (tip,))
        records = cursor.fetchone()
        print()
        print(records[1].upper())
        print ('-------')
        russ = input('Is your answer right? Yes - Enter, no - 1, for exit - 0: ')
        if russ == '0':
            i = 2
        elif russ == '1':
            i = 1
        else:
            cursor.execute('UPDATE top1000 SET score = score + 1 WHERE id = %s', (tip,))
            conn.commit()
        print()

cursor.close()
conn.close()
