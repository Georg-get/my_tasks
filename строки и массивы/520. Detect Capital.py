### Условие задачи:
# Мы определяем употребление заглавных букв в слове как правильное, когда имеет место один из следующих случаев:
# Все буквы в этом слове заглавные, например "USA".
# Все буквы в этом слове не заглавные, например "leetcode".
# Только первая буква в этом слове заглавная, например "Google".
# Учитывая строку word, верните значение true, если использование заглавных букв в ней правильное.

# Example 1:
# Input: word = "USA"
# Output: true

# Example 2:
# Input: word = "FlaG"
# Output: false

### Краткое условие:
# Вернуть True если в строке word все буквы большие или все буквы маленькие,
# или первая буква в слове word большая а все остальные маленькие.

# Алгоритм решение задачи:
# 0) Если все буквы  встроке заклавные или все буквы в строке маленькие или в строке есть одна заглавная буква, то верни True
# 1) Иначе False.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

word = "USA"

def detectCapitalUse(word):

    if word.isupper() or word.islower() or word.title() == word:
                                            # isupper(): Возвращает True, если все буквы в строке являются заглавными
                                            # islower(): Возвращает True, если все буквы в строке являются строчными
                                            # title(): Возвращает True, если строка начинается с заглавной буквы,
                                            # за которой следует только строчные буквы, иначе возвращает False.

        return True
    else:
        return False

detectCapitalUse(word)

assert detectCapitalUse(word="USA") == True
assert detectCapitalUse(word="Google") == True
assert detectCapitalUse(word="leetcode") == True
assert detectCapitalUse(word="FlaG") == False