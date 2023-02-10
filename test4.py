# Проверка текущих знаний
#1. [print]  Ваша задача вывести строку в форматирование "x больше y"
# ,след строка "и больше z" - где x - переменная натурального числа
# , y - переменная с плавающей точкой, z - строковое число.

#ответ: print(f"{int(x)} больше {float(y)} и больше {str(z)}")

#2. [Типы данных] Перевод входящих данных в input - можно перевести с помощью команды:
#- в число =
#- в строку =
#- в логическую переменную =
#- в число с плавающей точкой =

#ответ:
#- в число = int()
#- в строку = str()
#- в логическую переменную = bool()
#- в число с плавающей точкой = float()

#3. [input]Вывод диалога для input можно ли произвести в input? Продемонстрируйте пример:

#ответ: ДА, input("Пример диалога!  Будешь яблоко?")

#4. [Арифметика] Есть число 123987 - ваша задача вывести это число в виде:
#- сотни тысяч = 123987 // 100000
#- десятки тысяч = (123987 // 10000) % 10
#- тысячи = (123987 // 1000) % 10
#- сотни = (123987 // 100) % 10
#- десятки = (123987 // 10) % 10
#- единицы = 123987 % 10

#5. [условные операторы] Сколько вариантов конструкций If else elif - есть? Подсказка(их 4)
# Приведите примеры каждого из вариантов:
# 1.if x ==0:
#    print(x)
#else:
#    print(x)
# 2. if x ==0:
# #    print(x)
# 3. if x ==0:
#    print(x)
#elif x ==1:
#    print(x)
#else:
#    print(x)
# 4. if x ==0:
#    print(x)
#elif x ==1:
#    print(x)

#6. [условные операторы] Какие связки для сложных условий вы знаете? Приведите пример буквенного и символьного ввода
# and &&
# or ||

#7. [условные операторы] Продолжите код так, чтобы на выходе получился вывод 1;
#x = 4
#if x > 0:
#    x = x - 1
#elif x == 1:
#    print("Единица")
#else:
#    print(1)

#8.[Циклы] Какие циклы вы знаете?
# for while

#9. [Циклы] Чем они отличаются? В Чем преимущество каждого из циклов
#for - цикл с заданным количеством итераций, лушче всего подходит для перечислений списков
#while - цикл с неявно заданным кол-вом итераций, бесконечные диалоги

#10. [Циклы] Напишите вывод функции степени (как буд-то её не существует) через цикл.
# На вход подается число степеней и начальное число
#     x = int(input())
#     for i in range(x):
#         i= i*i
#         print(i)

#11. [Циклы] Какие две функции регламентируют работу цикла while? Опишите эти две функции(зачем нужны и где применяются)
# и продемонстрируйте простой пример
# break continue
# while x==0:
#     print(x)
#     break
# if x==0:
#     continue

#12. [Циклы] Какие бывают варианты работы с циклом For в качестве входного количества итераций? (Приведите 3 варианта)
# Задание поясняется устно
# for i in range(x)
#          string
#          array

#13. [Списки] Что такое списки - для чего они нужны? Приведите пример списка
    # Список нужен для хранения данных
    # x = []

#14. [Списки] Какие виды списков бывают? Приведите пример хотя бы 3х вариантов списка
    # Списки бывают:
    # пустые x = []
    # заданные x = [1, 2]
    # индексированные x = [one:1,
    #                      two:2]

#15. [Строки] На вход подается строка, ваша задача узнать и вывести информацию об этой строке:
#- Только числовая строка:
#- Есть ли в строке числа:
#- Сколько символов в строке:
#- Начинается ли строка с заглавной буквы:
#- Выведите на экран срез от 2 до 5 символа:

x = input()
first = x.isdigit()
for i in x:
    if i.isdigit():
        second = True
third = len(x)
four = x.istitle()
print(x[2:5])