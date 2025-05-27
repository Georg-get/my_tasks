### Условие задачи:
# Вам дана строка s строчных английских букв и массив, widths обозначающий ширину каждой строчной английской буквы в пикселях.
# В частности, widths[0] это ширина 'a', widths[1]это ширина 'b'и так далее.
# Вы пытаетесь писать s в несколько строк, длина каждой строки не превышает 100 пикселей.
# Начиная с начала s, в первой строке напишите столько букв, чтобы общая ширина не превышала 100пикселей.
# Затем с того места, где вы остановились s, продолжайте писать как можно больше букв во второй строке.
# Продолжайте этот процесс, пока не запишите все файлы s.
#
# Вернуть массив result длиной 2, где:
# result[0]общее количество строк.
# result[1]— ширина последней строки в пикселях.


# Example 1:
# Input: widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "abcdefghijklmnopqrstuvwxyz"
# Output: [3,60]
# Explanation: You can write s as follows:
# abcdefghij  // 100 pixels wide
# klmnopqrst  // 100 pixels wide
# uvwxyz      // 60 pixels wide
# There are a total of 3 lines, and the last line is 60 pixels wide.

# Example 2:
# Input: widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "bbbcccdddaaa"
# Output: [2,4]
# Explanation: You can write s as follows:
# bbbcccdddaa  // 98 pixels wide
# a            // 4 pixels wide
# There are a total of 2 lines, and the last line is 4 pixels wide.

                                            ### Добавить в список !

### Краткое условие:
# Вернуть массив result длиной 2, где: result[0]общее количество строк и result[1]— ширина последней строки в пикселях.

# Алгоритм решение задачи:
# 0)

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

                ### Сложная задача !!!

widths = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
s = "abcdefghijklmnopqrstuvwxyz"

def numberOfLines(widths, s):
    dict = {}
    countI = 0
    countJ = 0
    line = 1

    for i in "abcdefghijklmnopqrstuvwxyz":
        dict[i] = widths[countI]
        countI += 1

    # {'a': 10, 'b': 10, 'c': 10, 'd': 10, 'e': 10, 'f': 10, 'g': 10, 'h': 10, 'i': 10, 'j': 10, 'k': 10, 'l': 10, 'm': 10, 'n': 10, 'o': 10, 'p': 10, 'q': 10, 'r': 10, 's': 10, 't': 10, 'u': 10, 'v': 10, 'w': 10, 'x': 10, 'y': 10, 'z': 10}

    for j in s:
        countJ += dict[j]
        if countJ > 100:
            line += 1
            countJ = dict[j]
    # countJ = 60
    # line = 3
    return [line, countJ]

numberOfLines(widths, s)

assert numberOfLines(
    widths=[10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    s="abcdefghijklmnopqrstuvwxyz") == [3, 60]
assert numberOfLines(
    widths=[4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    s="bbbcccdddaaa") == [2, 4]
