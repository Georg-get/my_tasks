### Условие задачи:
# Вам дана строка с нулевым индексом, четные s индексы которой содержат строчные английские буквы, а нечетные цифры.
# Существует функция shift(c, x), где c— символ, а x — цифра, которая возвращает символ после .xthc
# Например, shift('a', 5) = 'f'и shift('x', 0) = 'x'.
# Для каждого нечетного индекса i вы хотите заменить цифру s[i]на shift(s[i-1], s[i]).
# Возврат s после замены всех цифр. Гарантируется , что shift(s[i-1], s[i])никогда не превысит 'z' .

# Example 1:
# Input: s = "a1c1e1"
# Output: "abcdef"
# Explanation: The digits are replaced as follows:
# - s[1] -> shift('a',1) = 'b'
# - s[3] -> shift('c',1) = 'd'
# - s[5] -> shift('e',1) = 'f'

# Example 2:
# Input: s = "a1b2c3d4e"
# Output: "abbdcfdhe"
# Explanation: The digits are replaced as follows:
# - s[1] -> shift('a',1) = 'b'
# - s[3] -> shift('b',2) = 'd'
# - s[5] -> shift('c',3) = 'f'
# - s[7] -> shift('d',4) = 'h'

### Краткое условие:
# Надо заменить цифры в строке на буквы сдвигом s[i-1].

# Алгоритм решение задачи:
# 0) Создаем дву пустые строки result и curr, и словарь dict со значением от 0 до 9.
# 1) Проходимся циклом по строке s,
# 1.1) Если ключа i есть в словаре dict, то увеличь переменную result на ASCII-код = ASCII-коду curr + число i, и сбрось строку curr
# 1.2) Если ключа i НЕТУ в словаре dict, то увеличь переменную result на i и curr равно i.
# 2) Верни строку result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

                                        ### Хэш таблицы ###

s = "a1c1e1"

def replaceDigits(s):
    result = ""
    curr = ""
    dict = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

    for i in s:
        if i in dict:
            result += chr(ord(curr) + int(i)) # ord метод который возращает ASCII-коду (номер буквы в таблице) буквы
            curr = ""                          # chr метод который возращает буквы по ее ASCII-коду (номер буквы в таблице)
        else:
            result += i
            curr = i

    return result

replaceDigits(s)

assert replaceDigits(s="a1c1e1") == "abcdef"
assert replaceDigits(s="a1b2c3d4e") == "abbdcfdhe"