### Условие задачи:
# Даны две строки first и second, рассмотрим вхождения в текст формы "first second third",
# где second следует сразу после first, а third следует сразу после second.
# Возвращает массив всех слов third для каждого вхождения "first second third" .

# Example 1:
# Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
# Output: ["girl","student"]

# Example 2:
# Input: text = "we will we will rock you", first = "we", second = "will"
# Output: ["we","rock"]

### Краткое условие:
# Возвращает массив всех слов third для каждого вхождения "first second third" .

# Алгоритм решение задачи:
# 0) Создаем массив textList созначение строки text и пустой масси result.
# 1) Проходимся циклом по диапазоны от 0 до длины массив textList-2,
# 1.1) Если элемент массива textList равен first и следующий элемент массива равен second,
# 1.1.1) Добавляем элемент массива textList+2 в массив result.
# 2) Вернуть массив result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

text = "alice is a good girl she is a good student"
first = "a"
second = "good"

def findOcurrences(text, first, second):
    textList = text.split()
    result = []

    for i in range(len(textList) - 2):
        if textList[i] == first and textList[i + 1] == second:
            result.append(textList[i + 2])

    return result

findOcurrences(text, first, second)

assert findOcurrences(text="alice is a good girl she is a good student", first="a", second="good") == ["girl",
                                                                                                       "student"]
assert findOcurrences(text="we will we will rock you", first="we", second="will") == ["we", "rock"]