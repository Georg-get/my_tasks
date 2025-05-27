### Условие задачи:
# Учитывая строку s и символ letter, верните процент символов в s этом значении,
# округленный до ближайшего целого процента.letter

# Example 1:
# Input: s = "foobar", letter = "o"
# Output: 33
# Explanation:
# The percentage of characters in s that equal the letter 'o' is 2 / 6 * 100% = 33% when rounded down, so we return 33.

# Example 2:
# Input: s = "jjjj", letter = "k"
# Output: 0
# Explanation:
# The percentage of characters in s that equal the letter 'k' is 0%, so we return 0.

### Краткое условие:
# Если буква из строки letter нету в строке s, то верни 0.
# А если эта буква есть то верни процент сколько раз она повторяется в строке s.

# Алгоритм решение задачи:
# 0) Если буква из строки letter есть в строке s,
# 0.1) Создай переменную result со значением 0.
# 0.2) Пройдись циклом по строке s, если i равна букве в строке letter, то увеличь result на 1.
# 0.3) Верни целое число result деленое на длину строки s умноженое на 100.
# 1) Если буква из строки letter НЕТУ в строке s, то верни 0.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

s = "foobar"
letter = "o"

def percentageLetter(s, letter):
    if letter in s:
        result = 0

        for i in s:
            if i == letter:
                result += 1

        return int(result / len(s) * 100)
    else:
        return 0

percentageLetter(s, letter)

assert percentageLetter(s="foobar", letter="o") == 33
assert percentageLetter(s="jjjj", letter="k") == 0