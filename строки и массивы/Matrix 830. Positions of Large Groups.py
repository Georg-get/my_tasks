### Условие задачи:
# В строке s строчных букв эти буквы образуют последовательные группы одного и того же символа.
# Например, строка типа s = "abbxxxxzyy" имеет группы "a", "bb", "xxxx", "z", и  "yy".
# Группа идентифицируется интервалом  [start, end], где start и end обозначают начальный и конечный индексы (включительно) группы.
# В приведенном выше примере "xxxx" имеет интервал  [3,6].
# Группа считается большой, если в ней 3 и более персонажей.
# Верните интервалы каждой большой группы, отсортированные в порядке возрастания начального индекса.

# Example 1:
# Input: s = "abbxxxxzzy"
# Output: [[3,6]]
# Explanation: "xxxx" is the only large group with start index 3 and end index 6.

# Example 2:
# Input: s = "abc"
# Output: []
# Explanation: We have groups "a", "b", and "c", none of which are large groups.

# Example 3:
# Input: s = "abcdddeeeeaabbbcd"
# Output: [[3,5],[6,9],[12,14]]
# Explanation: The large groups are "ddd", "eeee", and "bbb".

### Краткое условие:
# Верните интервалы каждой большой группы, отсортированные в порядке возрастания начального индекса.

# Полное объяснение решение задачи:
# 0) Задаем левый и правый указать. Создаем счетчик и пустой массив.
# 1) Если длина строки s меньше трех, то возвращаем пустой массив.
# 2) Проходимся циклом ваилд пока правый указатель не дойдет до конца строки s,
# 2.1) Если правый указатель меньше длины строки s и буквы из строки s где установлен левый и правый указатель равны, то увеличь на 1 счетчик и правый указатель.
# 2.2) Иначе,
# 2.2.1) Если count больше или равен 2, в массив result добавь [left, right - 1].
# 2.2.2) count = 0.
# 2.2.3) Если right - left <= 1, то увеличь right на 1.
# 2.2.4) left = right - 1.
# 3) Верни массив result.


# Сложность:
# 1) Время O(n)
# 2) Память O(1)

s = "abbxxxxzzy"

def largeGroupPositions(s):
    left = 0
    right = 1
    count = 0
    result = []

    if len(s) < 3:
        return result

    while right <= len(s):

        if right < len(s) and s[left] == s[right]:
            count += 1
            right += 1

        else:
            if count >= 2:
                result.append([left, right - 1])
            count = 0

            if right - left <= 1:
                right += 1
            left = right - 1

    return result # [[3, 6]]

largeGroupPositions(s)

assert largeGroupPositions(s="abbxxxxzzy") == [[3, 6]]
assert largeGroupPositions(s="abc") == []
assert largeGroupPositions(s="abcdddeeeeaabbbcd") == [[3, 5], [6, 9], [12, 14]]