### Условие задачи:
# Панграмма – это предложение, в котором каждая буква английского алфавита встречается хотя бы один раз.
# Учитывая строку sentence, содержащую только строчные английские буквы,
# верните if is pangram или в противном случае. true sentence false.

# Example 1:
# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.

# Example 2:
# Input: sentence = "leetcode"
# Output: false

### Краткое условие:
# Надо почитать количество разных букв в строке и если их меньше 26 вернуть False, если их 26 вернуть True.

# Алгоритм решение задачи:
# 0) Создаем пустой словарь dict и переменную result = 0 для подсчета хороших пар.
# 1) Пройтись циклом по массиву nums.
# 1.1) Если ключ со значением i есть в словаре dict, то увеличь значение ключа на 1.
# 1.2) Если такого ключа НЕТу, то добавь ключ i со значением 1.
# 2) Если размер словаря dict равен 26, то вернуть True.
# 2.1) Если размер словаря dict НЕ равен 26, то вернуть False.

# Сложность:
# 1) Время O(n)
# 2) Память O(1) (n)

sentence = "thequickbrownfoxjumpsoverthelazydog"

def checkIfPangram(sentence):
    dict = {}

    for i in sentence:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    # {'t': 2, 'h': 2, 'e': 3, 'q': 1, 'u': 2, 'i': 1, 'c': 1, 'k': 1, 'b': 1, 'r': 2, 'o': 4, 'w': 1, 'n': 1, 'f': 1, 'x': 1, 'j': 1, 'm': 1, 'p': 1, 's': 1, 'v': 1, 'l': 1, 'a': 1, 'z': 1, 'y': 1, 'd': 1, 'g': 1}
    if len(dict) == 26:
        return True
    else:
        return False

checkIfPangram(sentence)

assert checkIfPangram(sentence="thequickbrownfoxjumpsoverthelazydog") == True
assert checkIfPangram(sentence = "leetcode") == False