import pandas as pd
import string

def length_stats(text):
 text = text.lower()
 
 # Убираем знаки препинания и цифры
#  markettrans(что заменяем, на что заменяем, что удаляем - на None)
 translator = str.maketrans('', '', string.punctuation + string.digits)
#  Применяем это
 text = text.translate(translator)
 
 # Разбиваем текст на слова
 words = text.split()
 
 # Сортировка и удаление дупликатов
 unique_words = sorted(set(words))
 
 # Создаем Series(значения, индексы)
 lengths = pd.Series([len(word) for word in unique_words], index=unique_words)
 
 return lengths

print(length_stats('Мама мыла раму'))
print(length_stats('Лес, опушка, странный домик. Лес, опушка и зверушка.'))