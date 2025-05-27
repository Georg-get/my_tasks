### Условие задачи:
# Учитывая массив символов chars, сжимаем его, используя следующий алгоритм:
# Начните с пустой строки s. Для каждой группы последовательных повторяющихся символов в chars:
# Если длина группы равна 1, добавьте символ к s.
# В противном случае добавьте символ, за которым следует длина группы.
# Сжатая строка s не должна возвращаться отдельно, а храниться во входном массиве символов chars.
# Обратите внимание, что длина группы, равная 10 или превышающая ее, будет разбита на несколько символов в формате chars.
# После завершения изменения входного массива верните новую длину массива.
# Вы должны написать алгоритм, который использует только постоянное дополнительное пространство.

# Example 1:
# Input: chars = ["a","a","b","b","c","c","c"]
# Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
# Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

# Example 2:
# Input: chars = ["a"]
# Output: Return 1, and the first character of the input array should be: ["a"]
# Explanation: The only group is "a", which remains uncompressed since it's a single character.

# Example 3:
# Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
# Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".

### Краткое условие:
# Вернуть число букв которые повторяются.

# Алгоритм решение задачи:
# 0) Создаем переменные left и right со значением 0.
# 1) Проходимся циклом ваилд пока left не станет меньше длины массива chars,
# 1.1) Создаем переменные: char со значением буквы куда установлен левый указатель left, count со значением 0, 
# и chars[right] = char, увеличивает значение правого указателя на 1.
# 1.2.1) Проходимся циклом ваилд пока left не станет меньше длины массива chars и бука из массива chars где устанолен левый указатель не станет равна char,
# 1.2.1.1) Двикаем левый указатель на 1 и увеличиваем значение переменой count на 1.
# 1.3) Если count больше 1, 
# 1.3.1) То проходимся циклом по строке count,
# 1.3.1.1) Буква из массива chars где установлен правый указатель равна i,
# 1.3.1.2) Двигаем правый указатель на 1.
# 2) Вернуть right.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

chars = ["a", "a", "b", "b", "c", "c", "c"]

def compress(chars):
    left = 0
    right = 0
    
    while left < len(chars):
        char = chars[left]
        count = 0
        chars[right] = char
        right += 1

        while left < len(chars) and chars[left] == char:
            left += 1
            count += 1

        if count > 1:
            for i in str(count):
                chars[right] = i
                right += 1
                
    return right

compress(chars)