### Условие задачи:
# Вам дан кольцевой массив строк с индексом 0 и строка. Кольцевой массив означает, что конец массива соединяется с началом массива.wordstarget
# Формально, следующий элемент words[i]равен words[(i + 1) % n], а предыдущий элемент words[i]равен words[(i - 1 + n) % n], где n — длина words.
# Начиная с startIndex, вы можете переходить либо к следующему, либо к предыдущему слову по 1одному шагу за раз.
# Верните кратчайшее расстояние, необходимое для достижения строки target .
# Если строка target не существует в words, верните -1.

# Example 1:
# Input: words = ["hello","i","am","leetcode","hello"], target = "hello", startIndex = 1
# Output: 1
# Explanation: We start from index 1 and can reach "hello" by
# - moving 3 units to the right to reach index 4.
# - moving 2 units to the left to reach index 4.
# - moving 4 units to the right to reach index 0.
# - moving 1 unit to the left to reach index 0.
# The shortest distance to reach "hello" is 1.

# Example 2:
# Input: words = ["a","b","leetcode"], target = "leetcode", startIndex = 0
# Output: 1
# Explanation: We start from index 0 and can reach "leetcode" by
# - moving 2 units to the right to reach index 3.
# - moving 1 unit to the left to reach index 3.
# The shortest distance to reach "leetcode" is 1.

# Example 3:
# Input: words = ["i","eat","leetcode"], target = "ate", startIndex = 0
# Output: -1
# Explanation: Since "ate" does not exist in words, we return -1.

### Краткое условие:
# Верните кратчайшее расстояние, необходимое для достижения строки target.
# Если строка target не существует в words, верните -1.

# Алгоритм решение задачи:
# 0) Создаем левый и правый указатель со значением startIndex, и distance со значением 0 и lenWords со значнеием длины массива words.
# 1) Проходим циклом ваилд пока distance не станет меньше lenWords,
# 1.1) Если элемент где стаит левый указатель равен target или элемент где стаит правый указатель равен target, то верни distance.
# 1.2) Увеличиваем правый указатель на (right + 1) % lenWords.
# 1.3) Увеличиваем левый указатель на (left - 1 + lenWords) % lenWords.
# 1.4) Увеличиваем distance на 1.
# 2) Верни -1.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

words = ["hello", "i", "am", "leetcode", "hello"]
target = "hello"
startIndex = 1

def closetTarget(words, target, startIndex):
    left = startIndex
    right = startIndex
    distance = 0
    lenWords = len(words)

    while distance < lenWords:
        if words[left] == target or words[right] == target:
            return distance

        right = (right + 1) % lenWords
        left = (left - 1 + lenWords) % lenWords

        distance += 1

    return -1

closetTarget(words, target, startIndex)

assert closetTarget(words=["hello", "i", "am", "leetcode", "hello"], target="hello", startIndex=1) == 1
assert closetTarget(words=["a", "b", "leetcode"], target="leetcode", startIndex=0) == 1
assert closetTarget(words=["i", "eat", "leetcode"], target="ate", startIndex=0) == -1