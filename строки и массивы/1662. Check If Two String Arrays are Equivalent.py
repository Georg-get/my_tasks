### Условие задачи:
# Учитывая два массива строк word1 и word2, возврат, если два массива представляют одну и ту же строку,
# и в противном случае. true false
# Строка представляется массивом, если элементы массива, объединенные по порядку, образуют строку.

# Example 1:
# Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
# Output: true
# Explanation:
# word1 represents string "ab" + "c" -> "abc"
# word2 represents string "a" + "bc" -> "abc"
# The strings are the same, so return true.

# Example 2:
# Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
# Output: false

# Example 3:
# Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
# Output: true

### Краткое условие:
# Если буквы в массивах word1 и word2 равны то верни true, если нет то верни false.

# Алгоритм решение задачи:
# 0) Если строка с буквами из массива word1 равна строке с буквами из массива word2, то верни True.
# 1) Если строка с буквами из массива word1 НЕ равна строке с буквами из массива word2, то верни False.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

word1 = ["ab", "c"]
word2 = ["a", "bc"]

def arrayStringsAreEqual(word1, word2):
        # "abc"                  "abc"
    if ''.join(word1) == ''.join(word2):
        return True
    else:
        return False

arrayStringsAreEqual(word1, word2)

assert arrayStringsAreEqual(word1=["ab", "c"], word2=["a", "bc"]) == True
assert arrayStringsAreEqual(word1=["a", "cb"], word2=["ab", "c"]) == False
assert arrayStringsAreEqual(word1=["abc", "d", "defg"], word2=["abcddefg"]) == True