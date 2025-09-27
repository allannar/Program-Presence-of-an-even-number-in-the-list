import random

list_numbers = [
    random.randint(1, 100),
    random.randint(1, 100),
    random.randint(1, 100),
    random.randint(1, 100),
    random.randint(1, 100),
    random.randint(1, 100),
    random.randint(1, 100),
    random.randint(1, 100),
    random.randint(1, 100),
    random.randint(1, 100),
]
print(list_numbers)
print('')
# Выводим только чётные числа
even_numbers = [num for num in list_numbers if num % 2 == 0]
print("Чётные числа в списке:", even_numbers)

#if any(num % 2 == 0 for num in list_numbers) Это означает: "Если хотя бы один элемент в списке делится на 2 без остатка (то есть, является чётным), тогда условие выполняется" 
