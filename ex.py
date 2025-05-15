import pandas as pd

class BANANA:
    def __init__(self):
        self.name = pd.read_csv('var10.csv')


filename = 'var10.csv'
try:
    with open(filename, encoding='utf-8') as file:
        contents = file.read()
except FileNotFoundError:
    print(f"Запрашиваемый файл {filename } не найден")

class BUBLIK:
    def __init__(self):
        self.name = pd.read_csv('var11.csv')


filename = 'var11.csv'
try:
    with open(filename, encoding='utf-8') as file:
        contents = file.read()
except EmptyDataError:
    print(f"Запрашиваемый файл {filename } не найден")
    