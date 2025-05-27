### Условие задачи:
# Дана строка s, верните строку после замены каждой заглавной буквы на такую же строчную букву.

# Example 1:
# Input: s = "Hello"
# Output: "hello"

# Example 2:
# Input: s = "here"
# Output: "here"

# Example 3:
# Input: s = "LOVELY"
# Output: "lovely"

### Краткое условие:
# Надо заменить все заглавные буквы на маленькие.

# Алгоритм решение задачи:
# 0) Создаем пустой словарь dict,
# 1) Проходимся циклом по строке s,
# 1.1) Если ключ i есть в словаре dict, то увеличь строку result на значение ключа i из словаря dict.
# 1.2) Если ключ i НЕТУ в словаре dict, то увеличь строку result на i.
# 2) Верни строку result.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

s = "Hello"

def toLowerCase(s):
    # alphabet_dict = {chr(65 + i): chr(97 + i) for i in range(26)} # итератор который генерит словарь с алфовитом англиским.
    dict = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g', 'H': 'h', 'I': 'i', 'J': 'j',
            'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n', 'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r', 'S': 's', 'T': 't',
            'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x', 'Y': 'y', 'Z': 'z'}
    result = ""

    for i in s:
        if i in dict:
            result += dict[i]
        else:
            result += i
    # hello
    return result

toLowerCase(s)

assert toLowerCase(s="Hello") == "hello"
assert toLowerCase(s="here") == "here"
assert toLowerCase(s="LOVELY") == "lovely"