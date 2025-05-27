### Условие задачи:
# Вам даны строки key и message, которые представляют собой ключ шифрования и секретное сообщение соответственно.
# Действия по декодированию message следующие:
# Используйте первое появление всех 26 строчных английских букв в key качестве порядка таблицы замен.
# Сопоставьте таблицу замен с обычным английским алфавитом.
# message Затем каждая буква заменяется с помощью таблицы.
# Пространства ' 'преобразуются сами в себя.
# Например, учитывая (фактический ключ будет содержать хотя бы один экземпляр каждой буквы алфавита),
# у нас есть таблица частичной замены ( , , , , , ).key = "happy boy"'h' -> 'a''a' -> 'b''p' -> 'c''y' -> 'd''b' -> 'e''o' -> 'f'
# Вернуть декодированное сообщение.

# Example 1:
# Input: key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv"
# Output: "this is a secret"
# Explanation: The diagram above shows the substitution table.
# It is obtained by taking the first appearance of each letter in "the quick brown fox jumps over the lazy dog".

# Example 2:
# Input: key = "eljuxhpwnyrdgtqkviszcfmabo", message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
# Output: "the five boxing wizards jump quickly"
# Explanation: The diagram above shows the substitution table.
# It is obtained by taking the first appearance of each letter in "eljuxhpwnyrdgtqkviszcfmabo".

### Краткое условие:
# Вернуть декодированное сообщение.

# Алгоритм решение задачи:
# 0) Создаем: пустой словарь dict, переменные count со значением 0 и пустую строку result,
# и строку со всеми буквами англиского алфавита alphabet.
# 1) Проходимся циклом по строке key,
# 1.1) Если ключа i нету в словаре dict, то добавь ключа i со значением буквы из строки alphabet где установлена count,
# 1.2) Увеличиваем переменную count на 1.
# 2) Проходимся циклом по строке message, увеличиваем переменную result на значение ключа j из словаря dict.
# 3) Вернуть строку result.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"

def decodeMessage(key, message):
    dict = {' ': ' '}
    count = 0
    result = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for i in key:
        if i not in dict:
            dict[i] = alphabet[count]
            count += 1
    # {' ': ' ', 't': 'a', 'h': 'b', 'e': 'c', 'q': 'd', 'u': 'e', 'i': 'f', 'c': 'g', 'k': 'h', 'b': 'i', 'r': 'j', 'o': 'k', 'w': 'l', 'n': 'm', 'f': 'n', 'x': 'o', 'j': 'p', 'm': 'q', 'p': 'r', 's': 's', 'v': 't', 'l': 'u', 'a': 'v', 'z': 'w', 'y': 'x', 'd': 'y', 'g': 'z'}
    for j in message:
        result += dict[j]
    # this is a secret
    return result  # this is a secret

decodeMessage(key, message)

assert decodeMessage(key="the quick brown fox jumps over the lazy dog",
                     message="vkbs bs t suepuv") == "this is a secret"
assert decodeMessage(key="eljuxhpwnyrdgtqkviszcfmabo",
                     message="zwx hnfx lqantp mnoeius ycgk vcnjrdb") == "the five boxing wizards jump quickly"