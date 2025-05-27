### Условие задачи:
# Учитывая строку text, вы хотите использовать символы для формирования
# как можно text большего количества экземпляров слова «воздушный шар».
# Вы можете использовать каждый символ text не более одного раза.
# Возвращает максимальное количество экземпляров, которые можно сформировать.

# Example 1:
# Input: text = "nlaebolko"
# Output: 1

# Example 2:
# Input: text = "loonbalxballpoon"
# Output: 2

# Example 3:
# Input: text = "leetcode"
# Output: 0

### Краткое условие:
# Вернуть число сколько раз можем сформировать слова "balloon" в строке text.

# Алгоритм решение задачи:
# 0) Создаем словарь dict, где ключ это буква в слове "balloon", а значение ключа 0.
# 1) Проходимся циклом по строке text,
# 1.1) Если ключ i есть в словаре dict, то увеличь значение ключа i на 1.
# 2) Делим на 2 значение ключей "l" и "o".
# 3) Вернуть самый минималое значение в словаре dict.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

text = "nlaebolko"

def maxNumberOfBalloons(text):
    dict = {"b": 0, "a": 0, "l": 0, "o": 0, "n": 0}

    for i in text:
        if i in dict:
            dict[i] += 1
    # {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}
    dict["l"] //= 2  # Делим значение ключ "l" на 2, потому что в слове "balloon" две буквы "l"
    dict["o"] //= 2  # Делим значение ключ "o" на 2, потому что в слове "balloon" две буквы "o"
    # {'b': 1, 'a': 1, 'l': 1, 'o': 1, 'n': 1}
    return int(min(dict.values()))

maxNumberOfBalloons(text)

assert maxNumberOfBalloons(text="nlaebolko") == 1
assert maxNumberOfBalloons(text="loonbalxballpoon") == 2
assert maxNumberOfBalloons(text="leetcode") == 0