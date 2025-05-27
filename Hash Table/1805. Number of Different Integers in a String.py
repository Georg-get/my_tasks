### Условие задачи:
# Вам дана строка word, состоящая из цифр и строчных английских букв.
# Вы замените каждый нецифровой символ пробелом. Например, "a123bc34d8ef34"станет " 123  34 8 34".
# Обратите внимание, что у вас остались целые числа, разделенные хотя бы одним пробелом: "123", "34", "8"и "34".
# Возвращает количество различных целых чисел после выполнения операций замены word.
# Два целых числа считаются разными, если их десятичные представления без ведущих нулей различны.

# Example 1:
# Input: word = "a123bc34d8ef34"
# Output: 3
# Explanation: The three different integers are "123", "34", and "8". Notice that "34" is only counted once.

# Example 2:
# Input: word = "leet1234code234"
# Output: 2

# Example 3:
# Input: word = "a1b01c001"
# Output: 1
# Explanation: The three integers "1", "01", and "001" all represent the same integer because
# the leading zeros are ignored when comparing their decimal values.

### Краткое условие:
# Необходимо заменить все буквы на пробелы, а затем подсчитать количество различных целых чисел, оставшихся в строке,
# игнорируя ведущие нули.

# Краткое объяснение решение задачи:
# 1. Заменяем все буквы на пробелы в строке word.
# 2. Добавляем все числа из строки word в множество dictSet.
# 3. Возвращаем длину множество dictSet.

# Полное объяснение решение задачи:
# 0) Проходимся циклом по строке word и заменянем все буквый на пробел.
# 1) Создавем массив listWord с элементами строки word и множество dictSet.
# 2) Проходимся циклом по массиву listWord и добавляем числа в dictSet.
# 3) Вернуть длину dictSet.

# Сложность:
# 1) Время O(n^2)
# 2) Память O(n)

word = "a123bc34d8ef34"

def numDifferentIntegers(word):

    for i in word:
        if not i.isdigit():
            word = word.replace(i, ' ')

    #  123  34 8  34
    listWord = word.split() # ['123', '34', '8', '34']

    dictSet = set()

    for j in listWord:
        dictSet.add(int(j))
    # dictSet = {8, 34, 123}
    return len(dictSet) # 3

numDifferentIntegers(word)

assert numDifferentIntegers(word="a123bc34d8ef34") == 3
assert numDifferentIntegers(word="leet1234code234") == 2
assert numDifferentIntegers(word="a1b01c001") == 1
# Доп юнитесты для проверки некоторых условий:
assert numDifferentIntegers(word="abc") == 0 # Тест с отсутствием чисел
assert numDifferentIntegers(word="") == 0 # Тест с пустой строкой
assert numDifferentIntegers(word="abc1234567890xyz") == 1 # Тест с большими числами

                ### Старое рабочие решение через хэш таблицу !!! ###
# Полное объяснение решение задачи:
# 0) Создаем массива listWord со значением символов строки word.
# 1) Проходимся циклом по диапазону длины массива listWord,
# 1.1) Если i это буква, то меняем ее на пробел в массиве listWord.
# 2) Преобразуем массив listWord в строку listWord и склеиваем все цифры.
# 3) Удаляем пробелы и табы в строке listWord.
# 4) Преобразовываем строку listWord в массив числе stringWord с целыми числами.
# 5) Вернуть длину множества массива stringWord.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

# word = "a123bc34d8ef34"
#
# def numDifferentIntegers(word):
#     listWord = list(word)
#     # ['a', '1', '2', '3', 'b', 'c', '3', '4', 'd', '8', 'e', 'f', '3', '4']
#     for i in range(len(listWord)): # завеняем буквы в массиве listWord на пробел
#         if listWord[i].isalpha():
#             listWord[i] = ' '
#     # [' ', '1', '2', '3', ' ', ' ', '3', '4', ' ', '8', ' ', ' ', '3', '4']
#     listWord = ''.join(listWord)
#     # 123  34 8  34
#     listWord.strip()  # удалили пробелы и табы в строке
#     stringWord = listWord.split()
#     # ['123', '34', '8', '34']
#     stringWord = list(map(int, stringWord))
#     # 1. Функция map(int, stringWord) применяет функцию int к каждому элементу итерируемого объекта stringWord.
#     # В данном случае, функция int используется для преобразования каждого элемента объекта stringWord в целое число.
#     # 2. Результатом выполнения map(int, stringWord) является итератор, содержащий целые числа.
#     # 3. Функция list() используется для преобразования итератора в список.
#     # Таким образом, переменная stringWord теперь содержит список целых чисел, полученных из исходного итерируемого объекта stringWord.
#     # [123, 34, 8, 34]
#     return len(set(stringWord))  # 3
#
# numDifferentIntegers(word)