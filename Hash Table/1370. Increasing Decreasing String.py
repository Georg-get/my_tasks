### Условие задачи:
# Вам дана строка s. Измените порядок строки, используя следующий алгоритм:
# 1) Выберите самый маленький символ sи добавьте его к результату.
# 2) Выберите наименьший символ, s который больше, чем последний добавленный символ к результату, и добавьте его.
# 3) Повторяйте шаг 2, пока не сможете выбрать больше персонажей.
# 4) Выберите самый большой символ s и добавьте его к результату.
# 5) Выберите самый большой символ, s который меньше последнего добавленного символа к результату, и добавьте его.
# 6) Повторяйте шаг 5, пока не сможете выбрать больше символов.
# 7) Повторяйте шаги с 1 по 6, пока не выберете все символы из s.
# 8) На каждом этапе, если самый маленький или самый большой символ появляется более одного раза,
# вы можете выбрать любое вхождение и добавить его к результату.
# Верните строку результата после сортировки sс помощью этого алгоритма.

# Example 1:
# Input: s = "aaaabbbbcccc"
# Output: "abccbaabccba"
# Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
# After steps 4, 5 and 6 of the first iteration, result = "abccba"
# First iteration is done. Now s = "aabbcc" and we go back to step 1
# After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
# After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"

# Example 2:
# Input: s = "rat"
# Output: "art"
# Explanation: The word "rat" becomes "art" after re-ordering it with the mentioned algorithm.

### Краткое условие:
# Верните строку результата после сортировки s с помощью этого алгоритма.

# Алгоритм решение задачи:
# 0) Создаем массив stringInList с элементами строки s и пустую строку result.
# 1) Проходимся циклом по массиву stringInList,
# 1.1) Проходимся циклом по отсортированому по алфавиту (без повторяюмщеся элементами) массиву stringInList,
# 1.1.1) Удаляем элемент i из массива stringInList и увеличисваем переменную result на значение i.
# 1.2) Проходимся циклом по отсортированому по алфавиту (без повторяюмщеся элементами) массиву stringInList первернутому на обород,
# 1.2.1) Удаляем элемент j из массива stringInList и увеличисваем переменную result на значение j.
# 2) Вернуть переменную result.

# Сложность:
# 1) Время O(n^2)
# 2) Память O(n)

s = "aaaabbbcccc"

def sortString(s):
    stringInList = list(s)  # ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c']
    result = ''

    while stringInList:

        for i in sorted(set(stringInList)):  # ['a', 'b', 'c']
            stringInList.remove(i)
            result += i

        for j in sorted(set(stringInList), reverse=True):  # ['c', 'b', 'a']
            stringInList.remove(j)
            result += j
    # abccbaabcca
    return result

sortString(s)

assert sortString(s="aaaabbbbcccc") == "abccbaabccba"
assert sortString(s="rat") == "art"