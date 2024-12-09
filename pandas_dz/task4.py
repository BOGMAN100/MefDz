import pandas as pd

def best(journal):
    
    filtered = journal[
        (journal['maths'].isin([4, 5])) & 
        (journal['physics'].isin([4, 5])) & 
        (journal['computer science'].isin([4, 5]))
    ]
    
    return filtered


columns = ['name', 'maths', 'physics', 'computer science']
data = {
    'name': ['Иванов', 'Петров', 'Сидоров', 'Васечкин', 'Николаев'],
    'maths': [5, 4, 5, 2, 4],
    'physics': [4, 4, 4, 5, 5],
    'computer science': [5, 2, 5, 4, 3]
}
journal = pd.DataFrame(data, columns=columns)

# Фильтруем отличников
filtered = best(journal)

# Выводим результаты
print("Полный журнал:")
print(journal)
print("\\nОтличники:")
print(filtered)