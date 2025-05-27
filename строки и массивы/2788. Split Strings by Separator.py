### Условие задачи:
# Учитывая массив строк words и символ separator, разделите каждую строку words на separator.
# Возвращает массив строк, содержащий новые строки, образовавшиеся после разделения, за исключением пустых строк.
# Примечания
# separator используется для определения места разделения, но не включается в результирующие строки.
# Разделение может привести к появлению более двух строк.
# Результирующие строки должны сохранять тот же порядок, в котором они были заданы изначально.

# Example 1:
# Input: words = ["one.two.three","four.five","six"], separator = "."
# Output: ["one","two","three","four","five","six"]
# Explanation: In this example we split as follows:
# "one.two.three" splits into "one", "two", "three"
# "four.five" splits into "four", "five"
# "six" splits into "six"
# Hence, the resulting array is ["one","two","three","four","five","six"].

# Example 2:
# Input: words = ["$easy$","$problem$"], separator = "$"
# Output: ["easy","problem"]
# Explanation: In this example we split as follows:
# "$easy$" splits into "easy" (excluding empty strings)
# "$problem$" splits into "problem" (excluding empty strings)
# Hence, the resulting array is ["easy","problem"].

# Example 3:
# Input: words = ["|||"], separator = "|"
# Output: []
# Explanation: In this example the resulting split of "|||" will contain only empty strings, so we return an empty array [].

### Краткое условие:
# Надо вернуть массив words, где слова разделены согласно переменной separator.

# Алгоритм решение задачи:
# 0) Создаем пустой массив result.
# 1) Проходимся циклом по массиву words,
# 1.1) Создаем массив word со значением строки из массива words разделеная согласно условию separator,
# 1.2) Проходимся циклом по массиву word, если длина слова j больше 0, то добавляем j в массив result.
# 2) Вернуть массив result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

words = ["one.two.three", "four.five", "six"]
separator = "."

def splitWordsBySeparator(words, separator):
    result = []

    for i in words:
        word = i.split(separator)  # ['one', 'two', 'three'] # ['four', 'five'] # ['six']
        for j in word:
            if len(j) > 0:
                result.append(j)

    return result

splitWordsBySeparator(words, separator)

assert splitWordsBySeparator(words=["one.two.three", "four.five", "six"], separator=".") == ["one", "two", "three",
                                                                                             "four", "five", "six"]
assert splitWordsBySeparator(words=["$easy$", "$problem$"], separator="$") == ["easy", "problem"]
assert splitWordsBySeparator(words=["|||"], separator="|") == []