### Условие задачи:
# Учитывая две строки ransomNoteи magazine, верните true if,
# который ransomNote может быть создан с использованием букв from magazineи false иначе .
# Каждую букву magazine можно использовать только один раз ransomNote.

# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true

### Краткое условие:
# Вернуть True если есть одинаковый символ в строке ransomNote и в строке magazine, если нету похожих символов вернуть false

# Алгоритм решение задачи:
# 0) Создаем словарь dict.
# 1) Проходимся циклом по стороке magazine,
# 1.1) Если ключ i есть в словаре dict, то увеличь значние ключа i на 1.
# 1.2) Если ключ i НЕТу в словаре dict, то добавь ключ i со значением 1 в словарь dict.
# 2) Проходимся циклом по стороке ransomNote,
# 2.1) Если ключа j нету в словаре dict, то верни False.
# 2.2) Если значение ключа j в словаре dict больше 0, уменьшь значение ключа j на 1.
# 2.3) Если ключа j ЕСТЬ в словаре dict, то верни False.
# 3) Верни True.

# Сложность:
# 1) Время O(m + n)
# 2) Память O(n) (k)

ransomNote = "bg"
magazine = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"

def canConstruct(ransomNote, magazine):
    dict = {}

    for i in magazine:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    # {'e': 2, 'f': 7, 'j': 5, 'b': 7, 'd': 7, 'g': 7, 'h': 5, 'a': 6, 'i': 4, 'c': 2}
    for j in ransomNote:
        if j not in dict:
            return False
        elif dict[j] > 0:
            dict[j] -= 1
        else:
            return False
    # {'e': 2, 'f': 7, 'j': 5, 'b': 6, 'd': 7, 'g': 6, 'h': 5, 'a': 6, 'i': 4, 'c': 2}
    return True

canConstruct(ransomNote, magazine)

assert canConstruct(ransomNote="a", magazine="b") == False
assert canConstruct(ransomNote="aa", magazine="ab") == False
assert canConstruct(ransomNote="aa", magazine="aab") == True
assert canConstruct(ransomNote="bg", magazine="efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj") == True