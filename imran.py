Time = []
while True:
    command = input('Выберите команду \n'
                    '1 - time \n'
                    '2 - add and average\n'
                    '3 - step \n')
    if command == 'exit':
        print('Программа завершена!')
        break
    elif command == '2':
        command1 = input('1 - Добавить \n'
                         '2 - Средняя оценка \n''')
        if command1 == '1':
            grade = int(input("Введите оценку - "))
            Time.append(grade)
            print(Time)
        elif command1 == '2':
            sum1 = sum(Time)
            average = len(Time)
            print(f'Средняя оценка: {sum1 / average}')
        else:
            print('Вы не правильно написали функцию')

    elif command == '1':
        lesson = input('Введите урок - ')
        if lesson == '1':
            print('1 урок заканчивается в 8:45 ')
        elif lesson == '2':
            print('2 урок заканчивается в 9:35 ')
        elif lesson == '3':
            print('3 урок заканчивается в 10:25 ')
        elif lesson == '4':
            print('4 урок заканчивается в 11:25 ')
        elif lesson == '5':
            print('5 урок заканчивается в 12:15 ')
        elif lesson == '6':
            print('6 урок заканчивается в 13:05 ')
        elif lesson == '7':
            print('7 урок заканчивается в 14:05 ')
        elif lesson == '8':
            print('8 урок заканчивается в 14:55 ')
        elif lesson == '9':
            print('9 урок заканчивается в 15:45 ')
        elif lesson == '10':
            print('10 урок заканчивается в 16:45 ')
        else:
            print('от 1 до 10')

    elif command == '3':
        m = int(input('сколько метров до следущего кабинета'))
        st = m * 2
        print(f'до следущего кабинета - {st} шагов')
    else:
        print('Такой команды не существует')