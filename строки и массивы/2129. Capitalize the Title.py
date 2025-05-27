### Условие задачи:
# Вам дана строка title, состоящая из одного или нескольких слов, разделенных одним пробелом, где каждое слово состоит из английских букв.
# Сделайте строку заглавной, изменив заглавные буквы каждого слова так, чтобы:
# Если длина слова составляет 1 или 2 букв, измените все буквы на строчные.
# В противном случае измените первую букву на прописную, а остальные буквы на строчные.
# Верните заглавные буквы title.

# Example 1:
# Input: title = "capiTalIze tHe titLe"
# Output: "Capitalize The Title"
# Explanation:
# Since all the words have a length of at least 3, the first letter of each word is uppercase, and the remaining letters are lowercase.

# Example 2:
# Input: title = "First leTTeR of EACH Word"
# Output: "First Letter of Each Word"
# Explanation:
# The word "of" has length 2, so it is all lowercase.
# The remaining words have a length of at least 3, so the first letter of each remaining word is uppercase, and the remaining letters are lowercase.

# Example 3:
# Input: title = "i lOve leetcode"
# Output: "i Love Leetcode"
# Explanation:
# The word "i" has length 1, so it is lowercase.
# The remaining words have a length of at least 3, so the first letter of each remaining word is uppercase, and the remaining letters are lowercase.

### Краткое условие:
# Верните заглавные буквы title.

# Алгоритм решение задачи:
# 0) Создаем пустой массив result.
# 1) Проходимся циклом по массиву title,
# 1.1) Если длина i меньше 3, то добавть в массив result i с маленьких букв.
# 1.2) Если длина i НЕ меньше 3, то добавть в массив result i с большой буквы в начале строки.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

title = "capiTalIze tHe titLe"

def capitalizeTitle(title):
    result = []

    for i in title.split():
        if len(i) < 3:
            result.append(i.lower())
        else:
            result.append(i.capitalize())

    return ' '.join(result)

capitalizeTitle(title)

assert capitalizeTitle(title="capiTalIze tHe titLe") == "Capitalize The Title"
assert capitalizeTitle(title="First leTTeR of EACH Word") == "First Letter of Each Word"
assert capitalizeTitle(title="i lOve leetcode") == "i Love Leetcode"
assert capitalizeTitle(title="L hV") == "l hv"