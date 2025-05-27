### Условие задачи:
# Учитывая строку с индексом 0 s, несколько раз выполните следующую операцию любое количество раз:
# Выберите индекс i в строке и пусть это c будет символ в позиции i.
# Удалите ближайшее вхождение c слева от (если есть) и ближайшее вхождение справа (если есть) i c i
# Ваша задача — минимизировать длину, s выполнив описанную выше операцию любое количество раз.
# Возвращает целое число, обозначающее длину минимизированной строки.

# Example 1:
# Input: s = "aaabc"
# Output: 3
# Explanation: In this example, s is "aaabc". We can start by selecting the character 'a' at index 1. We then remove the closest 'a' to the left of index 1, which is at index 0, and the closest 'a' to the right of index 1, which is at index 2. After this operation, the string becomes "abc". Any further operation we perform on the string will leave it unchanged. Therefore, the length of the minimized string is 3.

# Example 2:
# Input: s = "cbbd"
# Output: 3
# Explanation: For this we can start with character 'b' at index 1. There is no occurrence of 'b' to the left of index 1, but there is one to the right at index 2, so we delete the 'b' at index 2. The string becomes "cbd" and further operations will leave it unchanged. Hence, the minimized length is 3.

# Example 3:
# Input: s = "dddaaa"
# Output: 2
# Explanation: For this, we can start with the character 'd' at index 1. The closest occurrence of a 'd' to its left is at index 0, and the closest occurrence of a 'd' to its right is at index 2. We delete both index 0 and 2, so the string becomes "daaa". In the new string, we can select the character 'a' at index 2. The closest occurrence of an 'a' to its left is at index 1, and the closest occurrence of an 'a' to its right is at index 3. We delete both of them, and the string becomes "da". We cannot minimize this further, so the minimized length is 2.

### Краткое условие:
# Вернуть количество букв, которые повторяются в строке s.

# Алгоритм решение задачи:
# 0) Создаем пустой словарь dict.
# 1) Проходимся циклом по строке s,
# 1.1) Если i есть в словаре dict, то увеличь значение ключа i на 1.
# 1.2) Если i НЕТу в словаре dict, то добавь i как ключ со значением 0 в словарь dict.
# 2) Верни длину словаря dict.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

s = "aaabc"

def minimizedStringLength(s):
    dict = {}

    for i in s:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 0
    # {'a': 2, 'b': 0, 'c': 0}
    return len(dict)  # 3

minimizedStringLength(s)

assert minimizedStringLength(s="aaabc") == 3
assert minimizedStringLength(s="cbbd") == 3
assert minimizedStringLength(s="dddaaa") == 2