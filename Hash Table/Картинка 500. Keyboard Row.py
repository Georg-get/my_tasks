### Условие задачи:
# Учитывая массив строк words, верните слова, которые можно набрать с использованием букв алфавита только в одной строке американской клавиатуры,
# как показано на рисунке ниже.
# На американской клавиатуре:
# первая строка состоит из символов "qwertyuiop",
# вторая строка состоит из символов "asdfghjkl", и
# третья строка состоит из символов "zxcvbnm".

# Example 1:
# Input: words = ["Hello","Alaska","Dad","Peace"]
# Output: ["Alaska","Dad"]

# Example 2:
# Input: words = ["omk"]
# Output: []

# Example 3:
# Input: words = ["adsdf","sfd"]
# Output: ["adsdf","sfd"]

### Краткое условие:
# Вернуть массив слов из массива words которые можно набрать с одной строки с клавиатуры.

# Алгоритм решение задачи:
# 0) Создаем 3 словаря: topDict с ключами верхней части клавы, midDict с ключами средней части клавы,
# botDict с ключами нижней части клавы, и пустой массив result.
# 1) Проходимся циклом по массиву words,
# 1.1) Создаем словарь dict со значением set(в котором у нас будут только маленькие буквы).
# 1.2) Если словаре dict есть похожие ключи на topDict или midDict или botDict, то добавь i в массив result.
# 2) Вернуть массив result.

# Сложность:
# 1) Время O(n) (n * k)
# 2) Память O(n) (k + m)

words = ["Hello", "Alaska", "Dad", "Peace"]

def findWords(words):
    topDict = {'w', 'e', 'y', 'r', 'p', 'u', 't', 'i', 'o', 'q'}
    midDict = {'a', 'h', 'j', 'k', 'l', 's', 'f', 'g', 'd'}
    botDict = {'v', 'b', 'z', 'c', 'm', 'n', 'x'}
    result = []

    for i in words:
        dict = set(i.lower())  # {'h', 'e', 'o', 'l'}                    lower - большие буквы в маленькие
        if dict.issubset(topDict) or dict.issubset(midDict) or dict.issubset(
                botDict):  # есть проверка на совпадение ключей issubset
            result.append(i)
    # ['Alaska', 'Dad']
    return result

findWords(words)

assert findWords(words=["Hello", "Alaska", "Dad", "Peace"]) == ["Alaska", "Dad"]
assert findWords(words=["omk"]) == []
assert findWords(words=["adsdf", "sfd"]) == ["adsdf", "sfd"]