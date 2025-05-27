### Условие задачи:
# В чужом языке, как ни удивительно, также используются английские строчные буквы, но, возможно, в другом формате order.
# Алфавит order представляет собой некоторую перестановку строчных букв.
# Дана последовательность words написанных на инопланетном языке и order алфавите, возврат true тогда и только тогда,
# когда данные words отсортированы лексикографически на этом инопланетном языке.

# Example 1:
# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

# Example 2:
# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

# Example 3:
# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).

                                        ### Добавить в список !

### Краткое условие:
# Дана последовательность words написанных на инопланетном языке и order алфавите, возврат true тогда и только тогда,
# когда данные words отсортированы лексикографически на этом инопланетном языке.

# Алгоритм решение задачи:
# 0) Создаем строку alp со сзачением всех англиских букв и пустой словарь dict.
# 1) Проходимся циклом по диапазону от 0 до 26,
# 1.1) Добавляем в словарь ключ order[i] (это буква из строки order) со значением буквы из строки англиского алфавита.
# 2) Пишем функцию которая преобразовывает букву в значение из словаря dict.
# 3) Проходимся циклом по диапазону (длины массива words -1),
# 3.1) Если слова из массива words которое будет преобразовано через функцию f больше чем слова из массива words которое будет преобразовано через функцию f -1.
# 3.1.1) То верни False.
# 4) Вернуть True.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

### Сложная задача !!!
words = ["hello", "leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"

def isAlienSorted(words, order):
    alp = 'abcdefghijklmnopqrstuvwxyz'
    dict = {}

    for i in range(26):
        dict[order[i]] = alp[i]
    # {'h': 'a', 'l': 'b', 'a': 'c', 'b': 'd', 'c': 'e', 'd': 'f', 'e': 'g', 'f': 'h', 'g': 'i', 'i': 'j', 'j': 'k', 'k': 'l', 'm': 'm', 'n': 'n', 'o': 'o', 'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't', 'u': 'u', 'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z'}
    def f(st: str) -> str:
        normal = ''
        for i in st:
            normal += dict[i]
        return normal
    # print(f("abc")) => cde это значение ключей из словаря dict
    for j in range(len(words) - 1):
        # j = hello в функции f будет agbbo > j -1 =leetcode в функции f будет bggteofg
        if f(words[j]) > f(words[j + 1]):
            return False

    return True

isAlienSorted(words, order)

assert isAlienSorted(words=["hello", "leetcode"], order="hlabcdefgijkmnopqrstuvwxyz") == True
assert isAlienSorted(words=["word", "world", "row"], order="worldabcefghijkmnpqstuvxyz") == False
assert isAlienSorted(words=["apple", "app"], order="abcdefghijklmnopqrstuvwxyz") == False