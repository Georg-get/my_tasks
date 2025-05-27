### Условие задачи:
# Учитывая строку английских букв s, верните самую большую английскую букву, которая встречается как в нижнем,
# так и в верхнем регистре s. Возвращаемое письмо должно быть в верхнем регистре.
# Если такой буквы не существует, верните пустую строку.
# Английская буква b больше другой буквы, a если b она стоит после нее a в английском алфавите.

# Example 1:
# Input: s = "lEeTcOdE"
# Output: "E"
# Explanation:
# The letter 'E' is the only letter to appear in both lower and upper case.

# Example 2:
# Input: s = "arRAzFif"
# Output: "R"
# Explanation:
# The letter 'R' is the greatest letter to appear in both lower and upper case.
# Note that 'A' and 'F' also appear in both lower and upper case, but 'R' is greater than 'F' or 'A'.

# Example 3:
# Input: s = "AbCdEfGhIjK"
# Output: ""
# Explanation:
# There is no letter that appears in both lower and upper case.

### Краткое условие:
# Вернуть букву, которая есть в строке s в нижнем и верхнем регистре.

# Алгоритм решение задачи:
# 0) Создаем пустой словарь dictSet со значением set.
# 1) Проходимся циклом по строке s,
# 1.1) Eсли i заглавная буква,
# 1.1.1) Если i маленькая буква есть в строке s, то добавь i в словарь dictSet.
# 2) Если длина словаря dictSet больше 0, верни массив c большой буквой из словаря dictSet.
# 3) Если длина словаря dictSet НЕ больше 0, то верни пустую строку.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

s = "lEeTcOdE"

def greatestLetter(s):
    dictSet = set()

    for i in s:
        if i.isupper():
            if i.lower() in s:
                dictSet.add(i)
    # {'E'}
    if len(dictSet) > 0:
        return max(list(dictSet))
    else:
        return ''

greatestLetter(s)

assert greatestLetter(s="lEeTcOdE") == "E"
assert greatestLetter(s="arRAzFif") == "R"
assert greatestLetter(s="AbCdEfGhIjK") == ""