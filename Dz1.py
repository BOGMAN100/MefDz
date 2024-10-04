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

