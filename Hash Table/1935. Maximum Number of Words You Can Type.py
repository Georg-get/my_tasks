### Условие задачи:
# Неисправна клавиатура, некоторые буквенные клавиши не работают. Все остальные клавиши на клавиатуре работают корректно.
# Дана строка text слов, разделенных одним пробелом (без начальных и конечных пробелов), а также строка,
# brokenLetters состоящая из всех отдельных буквенных клавиш, которые не работают, и возвращает количество слов,
# которые text вы можете полностью набрать с помощью этой клавиатуры.

# Example 1:
# Input: text = "hello world", brokenLetters = "ad"
# Output: 1
# Explanation: We cannot type "world" because the 'd' key is broken.

# Example 2:
# Input: text = "leet code", brokenLetters = "lt"
# Output: 1
# Explanation: We cannot type "leet" because the 'l' and 't' keys are broken.

# Example 3:
# Input: text = "leet code", brokenLetters = "e"
# Output: 0
# Explanation: We cannot type either word because the 'e' key is broken.

### Краткое условие:
# Вывести посчитать количество слов из строки text, в которых нету букв из строки brokenLetters.

# Алгоритм решение задачи:
# 0) Создаем:
# 0.1) Словарь setBrokenLetters со значением set(brokenLetters),
# 0.2) Преобразовываем строку text в массив со строками,
# 0.3) Переменную result со значением = 0.
# 1) Проходимся цикломи по массиву text,
# 1.1) Проходимся цикломи по слову внутри массива text,
# 1.1.1) Если j есть в словаре setBrokenLetters, то увеличь значение переменной result на 1 и выйди из циклов.
# 2) Верни длину массива - переменная result.

# Сложность:
# 1) Время O(n) (n * m)
# 2) Память O(n)

text = "hello world"
brokenLetters = "ad"

def canBeTypedWords(text, brokenLetters):
    setBrokenLetters = set(brokenLetters)  # {'d', 'a'}
    text = text.split()  # ['hello', 'world']
    result = 0

    for i in text:
        for j in i:
            if j in setBrokenLetters:
                result += 1
                break
    #             2  - 1
    return len(text) - result  # 1

canBeTypedWords(text, brokenLetters)

assert canBeTypedWords(text="hello world", brokenLetters="ad") == 1
assert canBeTypedWords(text="leet code", brokenLetters="lt") == 1
assert canBeTypedWords(text="leet code", brokenLetters="e") == 0