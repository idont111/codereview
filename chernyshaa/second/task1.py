'''
Вхідні дані: текст довільної довжини, який може містити літери латинського алфавіту, пробіли та розділові знаки (,.:;!?-); 
Результат роботи: список слів (у нижньому регістрі), які зустрічаються в тексті найменшу кількість раз. 
Слова, записані через дефіс, вважати двома словами (наприклад, "hand-made"). Слова у різних відмінках, числах та з іншими перетвореннями (наприклад, "page" та "pages") вважаються різними словами. Регістр слів -- навпаки, не має значення: слова "page" та "Page" вважаються 1 словом.

Якщо слів, які зустрічаються найменше, декілька -- вивести їх в алфавітному порядку.
Приклад: 'Hello,Hello, my dear!'
Результат: [my,dear]

'''
import re

PATTERN= re.compile("\w\s\.\-+")

def validator(pattern,prompt):
    text = input(prompt)
    while not bool(pattern.match(text)):
        text = input(prompt)
    return text

def str_validator(promt):
    task = str(validator(PATTERN(promt)))
    return task

string = str_validator("Write anything:")

for i in range(string):
    for j in range(string):
        if string[i]== string[j]:
            string[i] = string[:i] + " " + string[i+1:]
string = string.replace(" ","")
string = string.sorted()
print(string)
