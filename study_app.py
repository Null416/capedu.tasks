import random
import time
import threading
#Счетчик правильных ответов
score = 0
#register
reg_Name = input('Создайте имя пользователя: ')
reg_Password = input('Создайте пороль (Должен быть только на латиннице и не менее 5 символов): ')
while True:
    if reg_Password.isascii() and reg_Password.isalnum():
        print("Пароль принят")
        break
    else:
        print("Ошибка: пароль должен быть только на латинице")
    reg_Password = input("Введите пороль ТОЛЬКО на латиннице: ")
check = len(reg_Password)
if check >= 5:
    print('Ваш пороль соответсвует всем критериям')
else:
    print('Ваш пороль меньше 5 символов!')
# log in
log_Name = input('введите логин что бы войти в аккаунт: ')
log_Password = input('введите пороль что бы войти в аккаунт: ')
while True:
    if log_Name == reg_Name and log_Password == reg_Password:
        print('ВЫ УСПЕШНО ВОШЛИ НА АККАУНТ')
        break
    else:
        print('Извините, Логин или пороль был не правильно введен. Попробуйте снова')
        log_Name = input('введите логин что бы войти в аккаунт: ')
        log_Password = input('введите пороль что бы войти в аккаунт: ')
#Учебные карточки
cards_q =['2+2=?','1+1']
cards_a = ['4','2']
mode = input('ВЫБЕРИТЕ РЕЖИМ \n1-добавить карточку \n2-получить случайную карту \n3-остановить приложение \nВыбор: ')
while True:
    while True:
#Режим добавления вопрсов
        if mode == '1':
            vopros = input('Введите вопрос: ') 
            otvet = input('Введите ответ на вопрос: ') 
            cards_q.append(vopros) 
            cards_a.append(otvet)





        elif mode == '2':
            while True:

                index = random.randrange(len(cards_q))
                rm = cards_q[index]
                answer = cards_a[index]

                print("\nВопрос:", rm)

                result = [None]  # используем список вместо переменной

                def get_input():
                    result[0] = input('Введите ответ на вопрос: ')

                t = threading.Thread(target=get_input)
                t.start()

                t.join(timeout=30)

                if result[0] is None:
                    print("\n⏰ Время вышло!")
            
            

                if result[0] == answer:
                    print('ОТВЕТ ПРАВИЛЬНЫЙ')
                    score += 1
                    print('Вы ответили правильно', score, 'раз(а)')
                    break
                else:
                    print('ПОПРОБУЙТЕ В СЛЕДУЮЩИЙ РАЗ')
        elif mode == '3':
            break

        mode = input('ВЫБЕРИТЕ РЕЖИМ ЕЩЕ РАЗ \n1-добавить карточку \n2-получить случайную карту \n3-остановить приложение \nВыбор: ')