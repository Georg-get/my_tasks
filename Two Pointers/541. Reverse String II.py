### Условие задачи:
# Учитывая строку s и целое число k, поменяйте местами первые k символы для каждого 2k символа, считая от начала строки.
# Если символов осталось меньше k, поменяйте их все местами. Если количество символов меньше 2k, но больше или равно k,
# поменяйте местами первые k символы, а остальные оставьте исходными.

# Example 1:
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"

# Example 2:
# Input: s = "abcd", k = 2
# Output: "bacd"

### Краткое условие:
# Поменять местами буквы в строке s равное k.

# Алгоритм решение задачи:
# 0) Если k рано длине строке s, то верни перевенрую строку s.
# 1) Создаем пременные left со значением 0 и переменную right со значением k, и массива s со значением строки s.
# 2) Проходимся циклом ваилд пока right не станет меньше или равно длины массива s,
# 2.1) Меняем местами числа где установлен левый и правый указатель метами,
# 2.2) Увеличиваем значение переменной left на 2 умноженое на k.
# 2.3) Увеличиваем значение переменной right на 2 умноженое на k.
# 2.4) Если переменна right больше длины массива s, то поменяй местами букву где установен левый указатель с буквой которой рядом.
# 3) Верни строку из массива s.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

s = "abcdefg"
k = 2

def reverseStr(s, k):
    if k > len(s):  # без этого куска не проходит четвертый юнитест !!!
        return s[::-1]

    left = 0
    right = k
    s = list(s)                                 # ['a', 'b', 'c', 'd', 'e', 'f', 'g']

    while right <= len(s):                      # |    |
        s[left:right] = s[left:right][::-1]     # 1) ['b', 'a', 'c', 'd', 'e', 'f', 'g']
        left += 2 * k                           #                          |    |
        right += 2 * k                          # 2) ['b', 'a', 'c', 'd', 'f', 'e', 'g']

        if right > len(s):  # без этого куска не проходит третий юнитест !!!
            s[left:] = s[left:][::-1]
    # ['b', 'a', 'c', 'd', 'f', 'e', 'g']
    return ''.join(s)  # bacdfeg

reverseStr(s, k)

assert reverseStr(s="abcdefg", k=2) == "bacdfeg"
assert reverseStr(s="abcd", k=2) == "bacd"
assert reverseStr(  # этот тест нужен для предпоследней строички !!!
    s="hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl",
    k=39) == "fdcqkmxwholhytmhafpesaentdvxginrjlyqzyhehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqllgsqddebemjanqcqnfkjmi"
assert reverseStr(s="abcdefg", k=8) == "gfedcba"  # этот тест нужен для первой строички !!!