### Условие задачи:
# Учитывая строку s, измените порядок символов в каждом слове в предложении,
# сохраняя при этом пробелы и первоначальный порядок слов.

# Example 1:
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

# Example 2:
# Input: s = "Mr Ding"
# Output: "rM gniD"

### Краткое условие:
# Вернуть строку s, где все слова будут перевернутые.

# Алгоритм решение задачи:
# 0) Преобразовываем строку s в массив и создаем пустой массив result.
# 1) Проходимся циклом по массиву s,
# 1.1) Создаем два указателя: где левый указатель ставим на начало слова, а правый на конец слова.
# 1.2) Проходимся циклом ваилд пока левый и правый указатель пересекутся.
# 1.3) Преобразовываем i в массив, и меняем буквы местами, двигаем левый и правый указатель.
# 1.4) Преобразовываем массив i в строку stingI и добавляем строку stingI в массив result.
# 2) Вернуть строку преобразованую из массива result

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

s = "Let's take LeetCode contest"

def reverseis(s):
    s = s.strip().split()  # ["Let's", 'take', 'LeetCode', 'contest']
    result = []

    for i in s:

        left = 0
        right = (len(i) - 1)  # 5-1=4

        while left < right:
            i = list(i)  # ['L', 'e', 't', "'", 's']
            i[left], i[right] = i[right], i[left]
            left += 1
            right -= 1
        # ['s', "'", 't', 'e', 'L']
        stingI = ''.join(i)  # s'teL
        result.append(stingI)
    # ["s'teL", 'ekat', 'edoCteeL', 'tsetnoc']
    return ' '.join(result)

reverseis(s)

assert reverseis(s="Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
assert reverseis(s="Mr Ding") == "rM gniD"