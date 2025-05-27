### Условие задачи:
# Учитывая строку paragraphи массив строк запрещенных слов banned, верните наиболее часто встречающееся незапрещенное слово .
# Гарантируется, что есть хотя бы одно незапрещённое слово и что ответ уникален.
# Слова в paragraph не чувствительны к регистру, и ответ должен быть возвращен в нижнем регистре.

# Example 1:
# Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
# Output: "ball"
# Explanation:
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"),
# and that "hit" isn't the answer even though it occurs more because it is banned.

# Example 2:
# Input: paragraph = "a.", banned = []
# Output: "a"

### Краткое условие:
# Необходимо вернуть самое частое слово в строке paragraph, которое не является забаненным (нет в массиве banned).

# Краткое объяснение решение задачи:
# 1. Избавляемся от знаков препинания и делаем все большие буквы маленькими в строке paragraph.
# 2. Создаёт словарь, где ключами являются слова, а значениями — количество их вхождений, кроме забаненного слова.
# 3. Находит слово с наибольшим количеством вхождений и возвращает его.

# Полное объяснение решение задачи:
# 0) Создаем пустой словарь dict, переменную maxCount = 0 и пустую строку result.
# 1) Создаем массив words с значением без запятых и точек, и все заглавные буквы становяться маленькими.
# 2) Проходимся циклом по массиву words,
# 2.1) Если i нету в массиве banned, то добавлю ключ i со значенм i увеличеного на 1.
# 3) Проходимся циклом значением и ключам словаря dict,
# 3.1) Если count больше чем maxCount, то maxCount равно count и result равно word.
# 4) Верни строку result.

# Сложность:
# 1) Время O (L + n + m)
# где L — длина исходной строки paragraph, n — количество слов в listParagraph, а m — количество уникальных слов в словаре dict.
# 2) Память O (n + m)

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

def mostCommonWord(paragraph, banned):
    dict = {}
    listParagraph = paragraph.replace('!', ' ').replace('?', ' ')\
                            .replace("'", " ").replace(',', ' ')\
                            .replace(';', ' ').replace('.', ' ')\
                            .lower().split()
    # ['bob', 'hit', 'a', 'ball', 'the', 'hit', 'ball', 'flew', 'far', 'after', 'it', 'was', 'hit']
    for i in listParagraph:
        if i in dict and i not in banned:
            dict[i] += 1
        elif i not in dict and i not in banned:
            dict[i] = 1
    # dict = {'bob': 1, 'a': 1, 'ball': 2, 'the': 1, 'flew': 1, 'far': 1, 'after': 1, 'it': 1, 'was': 1}
                # 'ball'
    return max(dict, key=dict.get)

mostCommonWord(paragraph, banned)

assert mostCommonWord(paragraph="Bob hit a ball, the hit BALL flew far after it was hit.", banned=["hit"]) == "ball"
assert mostCommonWord(paragraph="a.", banned=[]) == "a"
assert mostCommonWord(
    paragraph="j. t? T. z! R, v, F' x! L; l! W. M; S. y? r! n; O. q; I? h; w. t; y; X? y, p. k! k, h, J, r? w! U! V; j' u; R! z. s. T' k. P? M' I' j! y. P, T! e; X. w? M! Y, X; G; d, X? S' F, K? V, r' v, v, D, w, K! S? Q! N. n. V. v. t? t' x! u. j; m; n! F, V' Y! h; c! V, v, X' X' t? n; N' r; x. W' P? W; p' q, S' X, J; R. x; z; z! G, U; m. P; o. P! Y; I, I' l' J? h; Q; s? U, q, x. J, T! o. z, N, L; u, w! u, S. Y! V; S? y' E! O; p' X, w. p' M, h! R; t? K? Y' z? T? w; u. q' R, q, T. R? I. R! t, X, s? u; z. u, Y, n' U; m; p? g' P? y' v, o? K? R. Q? I! c, X, x. r' u! m' y. t. W; x! K? B. v; m, k; k' x; Z! U! p. U? Q, t, u' E' n? S' w. y; W, x? r. p! Y? q, Y. t, Z' V, S. q; W. Z, z? x! k, I. n; x? z; V? s! g, U; E' m! Z? y' x? V! t, F. Z? Y' S! z, Y' T? x? v? o! l; d; G' L. L, Z? q. w' r? U! E, H. C, Q! O? w! s? w' D. R, Y? u. w, N. Z? h. M? o, B, g, Z! t! l, W? z, o? z, q! O? u, N; o' o? V; S! z; q! q. o, t! q! w! Z? Z? w, F? O' N' U' p? r' J' L; S. M; g' V. i, P, v, v, f; W? L, y! i' z; L? w. v, s! P?",
    banned=["m", "q", "e", "l", "c", "i", "z", "j", "g", "t", "w", "v", "h", "p", "d", "b", "a", "r", "x",
            "n"]) == "y"  # .replace("'", " ") нужен для этого юнитеста !!!
# Доп юнитесты для проверки некоторых условий:
assert mostCommonWord(paragraph="word word word word", banned=[]) == "word"  # Тест с одинаковыми словами
assert mostCommonWord(paragraph="a A a a b B b", banned=[]) == "a"  # Тест с разными регистрами

                        ### Старая рабочая версия,через хэш таблицу !!! ###
#
# import re
#
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
#
# def mostCommonWord(paragraph, banned):
#     dict = {}
#     maxCount = 0
#     result = ''
#     words = re.findall(r'\w+', paragraph.lower())
#     # ['bob', 'hit', 'a', 'ball', 'the', 'hit', 'ball', 'flew', 'far', 'after', 'it', 'was', 'hit']
#     for i in words:
#         if i not in banned:
#             dict[i] = dict.get(i, 0) + 1
#     # {'bob': 1, 'a': 1, 'ball': 2, 'the': 1, 'flew': 1, 'far': 1, 'after': 1, 'it': 1, 'was': 1}
#     for word, count in dict.items():
#         if count > maxCount:
#             maxCount = count
#             result = word
#
#     return result  # ball
#
# mostCommonWord(paragraph, banned)
