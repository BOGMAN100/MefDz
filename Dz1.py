# Задача 1
# Напишите функцию print_hello, которая принимает
#  имя пользователя и выводит приветствие

def print_hello(name):
    name = str(name) # на всякий случай
    print(f"Hello, {name}!")
    return 0

# Задание 2
# Напишите функцию gcd, которая принимает 
# два натуральных числа и возвращает их наибольший общий делитель.

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

# Задание 3
# Разработайте функцию month, которая принимает 
# номер месяца и обозначение языка ("ru", "en") и возвращает
# название заданного месяца в заданном языке с заглавной буквы.

ruMonth = [
    'январь', 
    'февраль',
    'март',
    'апрель',
    'май',
    'июнь',
    'июль',
    'август',
    'сентябрь',
    'октябрь',
    'ноябрь',
    'декабрь']

enMonth = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

monthMain = {"ru" : ruMonth,
             "en" : enMonth}

def month(numMonth, lang):
    if (numMonth < 1 or numMonth >= 12) or (lang not in monthMain):
        return 0
    return (monthMain.get(lang)[numMonth-1]).capitalize()


# Задание 4
# Разработайте функцию modern_print, которая принимает
# строку и выводит её, если она не была выведена ранее.

modern_print_list = []
def modern_print(st):
    if st not in modern_print_list:
        print(st)
        modern_print_list.append(st)
    return 0

# Задание 5 
# Напишите функцию is_palindrome, которая принимает
#  натуральное число, строку, кортеж или список,
#  а возвращает логическое значение:
#  True — если передан палиндром, а в противном случае — False.

def is_palindrome(x):
    if isinstance(x, (list, tuple)): #это список или кортеж?
        st = ''.join(map(str, x))               #сделаем строкой 
        # (join не переваривает числа, поэтому map делает каждый элемент типом str)
    else:
        st = str(x)
    return st == st[::-1]