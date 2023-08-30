######################################
# shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
# list_id_before = id(shopping_center[-1])
#
# shopping_center[-1].append("Uniqlo")
# list_id_after = id(shopping_center[-1])
#
# print(list_id_before == list_id_after)
#####################################
# random_matrix = [
#     [9, 2, 1],
#     [2, 5, 3],
#     [4, 8, 5]
# ]
# min_value_rows = []
# min_index_rows = []
# max_value_rows = []
# max_index_rows = []
# for row in random_matrix:
#     min_index = 0
#     min_value = row[min_index]
#     max_index = 0
#     max_value = row[max_index]
#     for index_col in range(len(row)):
#         if row[index_col] < min_value:
#             min_value = row[index_col]
#             min_index = index_col
#         if row[index_col] > max_value:
#             max_value = row[index_col]
#             max_index = index_col
#     min_value_rows.append(min_value)
#     min_index_rows.append(min_index)
#     max_value_rows.append(max_value)
#     max_index_rows.append(max_index)
# print("Minimal elements:", min_value_rows)  # минимальные элементы
# print("Their indices:", min_index_rows)  # их индексы
# print("Maximal elements:", max_value_rows)  # максимальные элементы
# print("Their indices:", max_index_rows)  # их индексы
#####################################
# Напишите цикл, который ищет наибольший элемент в матрице.
# test_matrix = [[1, 2, 3],
#                [7, -1, 2],
#                [123, 2, -1]]
# max = test_matrix[0][0]
# min = test_matrix[0][0]
# for row in test_matrix:
#     for col in range(len(row)):
#         if row[col] > max:
#             max = row[col]
#         if row[col] < min:
#             min = row[col]
# print(max)
# print(min)
#####################################
# Напишите код, который определяет, является ли матрица квадратной (то есть количество строк равно количеству столбцов).
# В конце программа должна выводить на экран значение True или False в зависимости от заданной матрицы.
# Используйте матрицу из предыдущей задачи.
# Помните, что количество элементов в каждой строке должно быть одинаковым.
# test_matrix = [[1, 2, 3],
#                [7, -1, 2],
#                [123, 2, -1]]
# print(test_matrix)
# rows = len(test_matrix)
# list_cols = []
# print(f'rows = {rows}')
# for row in test_matrix:
#     list_cols.append(len(row))
#     # print(list_cols)
# min_cols = min(list_cols)
# max_cols = max(list_cols)
# cols = min_cols == max_cols
# # print(cols)
# # print(f'min_cols = {min_cols}')
# # print(f'max_cols = {max_cols}')
# print('матрица является квадратной') if cols and rows == max_cols else print(
#       'матрица НЕ является квадратной')
#####################################
# Но, чтобы убить двух зайцев сразу, мы можем прибегнуть к функции
# enumerate. Она возвращает кортежи, где на первом месте стоит индекс
# элемента, а на втором — его значение.
# list_ = [-5, 2, 4, 8, 12, -7, 5]
# # Функция enumerate возвращает данные в виде кортежей,
# # где на первом месте стоит индекс, а затем значение
# # [(0, -5), (1, 2), (2, 4), ...]
# for i, value in enumerate(list_):
#     print("Индекс элемента: ", i)
#     # с помощью индекса получаем значение элемента
#     print("Значение элемента: ", value)
#     print("---")
# print("Конец цикла")

#####################################
# text = """
# У лукоморья дуб зелёный;
# Златая цепь на дубе том:
# И днём и ночью кот учёный
# Всё ходит по цепи кругом;
# Идёт направо -- песнь заводит,
# Налево -- сказку говорит.
# Там чудеса: там леший бродит,
# Русалка на ветвях сидит;
# Там на неведомых дорожках
# Следы невиданных зверей;
# Избушка там на курьих ножках
# Стоит без окон, без дверей;
# Там лес и дол видений полны;
# Там о заре прихлынут волны
# На брег песчаный и пустой,
# И тридцать витязей прекрасных
# Чредой из вод выходят ясных,
# И с ними дядька их морской;
# Там королевич мимоходом
# Пленяет грозного царя;
# Там в облаках перед народом
# Через леса, через моря
# Колдун несёт богатыря;
# В темнице там царевна тужит,
# А бурый волк ей верно служит;
# Там ступа с Бабою Ягой
# Идёт, бредёт сама собой,
# Там царь Кащей над златом чахнет;
# Там русский дух... там Русью пахнет!
# И там я был, и мёд я пил;
# У моря видел дуб зелёный;
# Под ним сидел, и кот учёный
# Свои мне сказки говорил.
# """
# text = text.lower()  # привели все к нижнему регистру
# text = text.replace("\n", " ")  # убрали символы перевода строки
# text = text.replace(".", " ")
# text = text.replace(",", " ")
# text = text.replace(";", " ")
# text = text.split()
# count = {}  # для подсчета символов и их количества
# for letter in text:
#     if letter in count:  # если символ уже встречался, то увеличиваем его количество на 1
#         count[letter] += 1
#     else:
#         count[letter] = 1
# for char, cnt in count.items():
#     print(f"Слово {char} встречается {cnt} раз")

#####################################
# heads = 35  # количество голов
# legs = 94  # количество ног
#
# for r in range(heads + 1):  # количество кроликов
#     for ph in range(heads + 1):  # количество фазанов
#         # если суммарное количество голов превышено или ног превышено, то
#         # переходим на следующий шаг цикла
#         if (r + ph) > heads or \
#                 (r * 4 + ph * 2) > legs:
#             continue
#         if (r + ph) == heads and (r * 4 + ph * 2) == legs:
#             print("Количество кроликов", r)
#             print("Количество фазанов", ph)
#             print("---")
#####################################
# Помните, в прошлом модуле мы с вами разбирали, как определить, содержит ли число цифры 5, 7 или 9:
# if ‘5’ in str(num):
# Напишите алгоритм, который делает то же самое, но работает только с
# числом, не приводя его в строку.
# num = 12230955723897265
# while num // 10 > 10:
#     rest = num % 10
#     num = num // 10
#     if rest in [5, 7, 9]:
#         print(f'Число содержит {rest}')

# декораторы
#####################################
# def my_decor(func):
#     def wrapper():
#         print("start")
#         func()
#         print("end")
#     return wrapper
#
#
# def my_func():
#     print("тут основная функция")
#
#
# my = my_decor(my_func)
# my()

######################################
# def my_decor(func):
#     def wrapper(n):
#         print("start")
#         func(n)
#         print("end")
#     return wrapper
#
#
# @my_decor
# def my_func(number):
#     print(number ** 2)
#
#
# my_func(10)

###################################
# a, b, c = [int(input()) for _ in range(3)]
# a, b, c = map(int, input().split())
# print(a, b, c, sep='-')


#####################################
# # Хорошо
# a is None
# # Плохо
# a == None
# # Хорошо
# if not seq:
# if seq:
# # Плохо
# if len(seq)
# if not len(seq)
# # Хорошо
# if greeting:
# # Плохо
# if greeting == True:
# # Совсем неверно
# if greeting is True:
# a <= b <= c
# a == b == c

###########################
# import re
#
# my_st = "Я\nучу; язык,программирования\nPython"
# print(re.split(";|,|\n", my_st))
#
#
# string = "This is\na\ttest"
# delimiters = r"[\n\t ]+"
# result = re.split(delimiters, string)
# print(result)
#
# string = "This is\na\ttest"
# delimiters = " \t"
# lines = string.splitlines()
# result = [item for line in lines for item in line.split(delimiters)]
# print(result)

# ######################################
# Разделение строки с несколькими разделителями на словарь
# import re
#
# string = "name:John,age:30,gender:Male"
# delimiters = r"[:, ]+"
# result = dict(zip(re.split(delimiters, string)[::2], re.split(delimiters, string)[1::2]))
# print(result)
# # разделение строки с несколькими разделителями и игнорирование пустых строк
# string = "This/ is\na\ttest\n"
# delimiters = " \n\t/ "
# result = [item for item in re.split("|".join(delimiters), string) if item]
# print(result)

################################
# Множества
# a = set([1, 2, 3, 4])
# b = set([3, 4, 5, 6])
# print(a & b)
# print(a | b)
# print(a.union(b))
# print(a.difference(b))
# print(b.difference(a))

# Задача 7. Человек берет кредит в банке на сумму `M` рублей.
# Процентная ставка `r%`. Сумма, которую человек ежегодно выплачивает,
# `K` рублей. Через сколько лет человек погасит кредит?
# M = 1000
# K = 70
# r = 6
# count = 0
# while M > 0:
#     count += 1
#     M += M * (r / 100)
#     M -= K
# print(count)

################################
# Функции
# def f(a, b=2):
#     return a + b
#
#
# print(f(3, 4))
# print(f(3))

################################
# def f2(*args):
#     res = 0
#     for i in args:
#         res += i
#     return res
#
# print(f2(3, 4))
# print(f2(3))
# print(f2(3, 4, 5, 6, 7, 8))

################################
# Рекурсия
# def F(n):
#     print(n)
#     if n < 10:
#         F(n + 1)
#     print(f"end {n}")
#
#
# F(1)

################################
# Задача 8. Дано натуральное число N.
# Выведите слово YES, если число N является точной степенью двойки,
# или слово NO в противном случае.
# N = 127
#
# def check(a):
#     if a % 2 == 0:
#         return check(a // 2)
#     else:
#         if a == 1:
#             return True
#         else:
#             return False
#
#
# print(check(N))


################################
# Декораторы
# Задача 9. Напишите декоратор, который печатает имя функции при ее вызове
# def my_decorator(fn):
#     def wrapper():
#         print(fn.__name__)
#         return fn()
#
#     return wrapper
#
#
# @my_decorator
# def myf():
#     return 1
#
#
# print(myf())
#
#
# def myf2():
#     return 2
#
#
# myf2 = my_decorator(myf2)
# print(myf2())

################################
# number = 111115222222222222225
# digitToFind = 5
# # медленно
# num = number
# while num > 0:
#     digit = num % 10
#     if digit == digitToFind:
#         print(f"{digitToFind} is in number {number}")
#         break
#     num = int(num / 10)
# # быстро
# if str(digitToFind) in str(number):
#    print(f"{digitToFind} is in number {number}")

################################
# x = 3
#
#
# def func():
#    global x # объявляем, что переменная является глобальной
#    print(x)
#    x = 5
#    x += 5
#    return x
#
#
# func()
# print(x),

################################
# def get_mul_func(m):
#     nonlocal_m = m
#
#     def local_mul(n):
#         return n * nonlocal_m
#
#     return local_mul
#
#
# two_mul = get_mul_func(3)  # возвращаем функцию, которая будет умножать числа на 2
# print(two_mul(10))  # 5 * 2

################################
# Запакованные переменные, или что такое *args и **kwargs
# a = [1, 2, 3]
# b = [a, 4, 5, 6]
# print(b)
# # [[1, 2, 3], 4, 5, 6]
#
# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)
# # [1, 2, 3, 4, 5, 6]
################################
# def my_func(*args, **kwargs):
#     print(type(args))
#     print(type(kwargs))
#
#
# my_func()
#
#
# # <class 'tuple'>
# # <class 'dict'>
#
# def adder(*nums):
#     sum_ = 0
#     for n in nums:
#         sum_ += n
#
#     return sum_
#
#
# print(adder())  # 0
# print(adder(1))  # 1
# print(adder(1, 2))  # 3
# print(adder(1, 2, 3))  # 6
################################
# def mul(*nums):
#     pr = 1
#     for n in nums:
#         pr *= n
#     return pr
#
#
# print(mul())
# print(mul(0))
# print(mul(1))
# print(mul(1, 3))
# print(mul(5, 15, 2))
# print(mul(1, 10, 100, 31))
#############################
# С помощью рекурсивной функции найдите сумму чисел от 1 до n.
# def sumn(n):
#     if n == 1:
#         return 1
#     return sumn(n - 1) + n
#
#
# print(sumn(25))
################################
# С помощью рекурсивной функции развернуть строку.
# def revstr(string):
#     if (len(string) == 0):
#         return ''
#     else:
#         return string[-1] + revstr(string[:-1])
#
#
# print(revstr("С помощью рекурсивной функции развернуть строку."))
################################
# Дано натуральное число N. Вычислите сумму его цифр.
# При решении этой задачи нельзя использовать строки, списки, массивы (ну и циклы, разумеется).
# def sum_digit(n):
#     if n < 10:
#         return n
#     else:
#         return n%10+sum_digit(n//10)
#
# print(sum_digit(333))
print(14252 + 3869)


################################
# функция-генератор для чисел Фибоначчи
# def fib():
#     a, b = 0, 1
#     yield a
#     yield b
#
#     while True:
#         a, b = b, a + b
#         yield b
# #
# # for num in fib():
# #     if num > 100000000:
# #         break
# #     print(num, end=" ")
# for i in fib():
#     print(i)

################################
# Создать функцию-генератор, возвращающую бесконечную последовательность натуральных чисел.
# По умолчанию, она начинается с единицы и шагом 1, но пользователь может указать
# любой шаг и любое число в качестве аргумента функции, с которого будет начинаться последовательность.
# def nat_gen(start=1,step=1):
#     counter = start
#     while True:
#         yield counter
#         counter += step
#
# for num in nat_gen(100,-1):
#     print(num, end=" ")
################################
# Создайте генератор, который по переданному списку создаёт последовательность, в которой элементы этого списка бесконечно циклично повторяются.
# Например, для списка [1, 2, 3] генератор создаст бесконечную последовательность 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, ... .
# def serial(list=None):
#     if list is None:
#         list = [' ']
#     list_copy = list.copy()
#     while True:
#         value = list_copy.pop(0)
#         list_copy.append(value)
#         yield value
#
#
# for i in serial([1, 2, 3]):
#     print(i, end=" ")
################################
# Итераторы
# для примера возьмём строку
# str_ = "my tst"
# str_iter = iter(str_)
#
# print(type(str_))  # строка
# print(type(str_iter))  # итератор строки
# # Получим первый элемент строки
# print(next(str_iter))  # m
#
# # Получим ещё несколько элементов последовательности
# print(next(str_iter))  # y
# print(next(str_iter))  #
# print(next(str_iter))  # t
# print(next(str_iter))  # s
# print(next(str_iter))  # t
# print(next(str_iter))
################################
# def last_gen():
#     for i in range(10):
#         yield i
#         if i == 5:
#             raise StopIteration
#
# my_last_gen = last_gen()
# my_last_gen2 = last_gen()
# for _ in range(4):
#     print(next(my_last_gen2))
# for _ in range(10):
#     print(next(my_last_gen))
################################
# def my_animal_generator():
#     yield 'корова'
#     print('___')
#     for aninmal in ['кот',"басяка", "ведмедь"]:
#         yield aninmal
#     print('___')
#     yield 'кит'
#
# a=my_animal_generator()
# print(next(a))
# print(next(a))
# for i in a:
#     print(i)
################################
# def make_adder(x):
#    def adder(n):
#        return x + n # захват переменной "x" из nonlocal области
#    return adder  # возвращение функции в качестве результата
# # функция, которая будет к любому числу прибавлять пятёрку
# add_5 = make_adder(5)
# print(add_5(10))  # 15
# print(add_5(100))  # 105
################################
#     # Здесь мы определяем новую функцию - «обертку». Она нам нужна, чтобы выполнять
# def my_decorator(a_function_to_decorate):
#         # здесь поместим код, которые будет выполняться до вызова, потом вызов
#     # каждый раз при вызове оригинальной функции, а не только один раз
#         # оригинальной функции, потом код после вызова
#     def wrapper():
#
#
#         print("Я буду выполнен до основного вызова!")
#         print("Я буду выполнен после основного вызова!")
#         result = a_function_to_decorate()  # не забываем вернуть значение исходной функции
#
#     return wrapper
#         return result
#
#
# def my_function():
#     return 0
#     print("Я - оборачиваемая функция!")
# print(my_function())
#
# # Я - оборачиваемая функция!
#
#
# decorated_function = my_decorator(my_function)  # декорирование функции
# # 0
# print(decorated_function())
# Я буду выполнен до основного вызова!
# Я - оборачиваемая функция!
# Я буду выполнен после основного вызова!
################################
# import time
#
# N = 10000
#
#
# def decorator_time(fn):
#     def wrapper():
#         # print(f"Запустилась функция {fn}")
#         t0 = time.time()
#         # print(f"Запустилась функция {t0}")
#         result = fn()
#         dt = time.time() - t0
#         # print(f"Запустилась функция {dt}")
#         # print(f"Функция выполнилась. Время: {dt:.10f}")
#         return dt  # задекорированная функция будет возвращать время работы
#     return wrapper
#
# def pow_2():
#     return 10000000 ** 2
#
#
# def in_build_pow():
#     return pow(10000000, 2)
#
#
# pow_2 = decorator_time(pow_2)
# in_build_pow = decorator_time(in_build_pow)
#
# # pow_2()
# # in_build_pow()
# mean_pow_2 = 0
# mean_in_build_pow = 0
# for _ in range(N):
#    mean_pow_2 += pow_2()
#    mean_in_build_pow += in_build_pow()
#
# print(f"Функция {pow_2} выполнялась {N} раз. Среднее время: {mean_pow_2 / N:.10f}")
# print(f"Функция {in_build_pow} выполнялась {N} раз. Среднее время: {mean_in_build_pow / N:.10f}")
################################

# def my_decorator(fn):
#    def wrapper():
#        fn()
#    return wrapper  # возвращается задекорированная функция, которая заменяет исходную
#
# # выведем незадекорированную функцию
# def my_function():
#    pass
# print(my_function)  # <function my_function at 0x7f938401ba60>
#
# # выведем задекорированную функцию
# @my_decorator
# def my_function():
#    pass
# print(my_function)  # <function my_decorator.<locals>.wrapper at 0x7f93837059d8>
################################
# Вот универсальный шаблон для декоратора:
# def my_decorator(fn):
#     print("Этот код будет выведен один раз в момент декорирования функции")
#
#     def wrapper(*args, **kwargs):
#         print('Этот код будет выполняться перед каждым вызовом функции')
#         result = fn(*args, **kwargs)
#         print('Этот код будет выполняться после каждого вызова функции')
#         return result
#
#     return wrapper


################################
# Напишите декоратор, который будет подсчитывать количество вызовов декорируемой функции.
# Для хранения переменной содержащей, количество вызовов, используйте nonlocal область декоратора.
# def counter(func):
#     count = 0
#
#     def wrapper(*args, **kwargs):
#         nonlocal count
#         func(*args, **kwargs)
#         count += 1
#         print(f"Функция {func} была вызвана {count} раз")
#
#     return wrapper
#
#
# @counter
# def say_word(word):
#     print(word)
#
#
# say_word('Oo!!!')
# say_word('Oo!!!')
# say_word('Oo!!!')


################################
# Напишите декоратор, который будет сохранять результаты выполнения декорируемой функции в словаре.
# Словарь должен находиться в nonlocal области в следующем формате: по ключу располагается аргумент функции,
# по значению результат работы функции, например, {n: f(n)}.
# И при повторном вызове функции будет брать значение из словаря, а не вычислять заново.
# То есть словарь можно считать промежуточной памятью на время работы программы,
# где будут храниться ранее вычисленные значения. Исходная функция,
# которую нужно задекорировать имеет следующий вид и выполняет простое умножение на число 123456789.:
# def f(n):
#    return n * 123456789

def cache(func):
    cache_dict = {}

    def wrapper(num):
        nonlocal cache_dict
        if num not in cache_dict:
            cache_dict[num] = func(num)
            print(f"Добавление результата в кеш: {cache_dict[num]}")
        else:
            print(f"Получение результата из кеша:{cache_dict[num]}")
        print(f"Кеш {cache_dict}")
        return cache_dict[num]

    return wrapper


@cache
def f(n):
    return n * 123456789


print(f(33))
print(f(33))
print(f(44))
print(f(44))
print(f(55))
print(f(55))
print(f(77))
print(f(77))
print(f(88))
print(f(88))
################################
################################
################################
################################
################################
################################
