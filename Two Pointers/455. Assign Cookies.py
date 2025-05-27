### Условие задачи:
# Предположим, вы отличный родитель и хотите подарить своим детям печенье. Но вы должны дать каждому ребенку не более одного печенья.
# У каждого ребенка iесть коэффициент жадности g[i], который представляет собой минимальный размер файла cookie,
# которым ребенок будет довольствоваться; и каждый файл cookie jимеет размер s[j]. Если s[j] >= g[i],
# мы можем назначить файл cookie jдочернему элементу i, и дочерний элемент iбудет доволен.
# Ваша цель — максимизировать количество дочерних элементов контента и вывести максимальное количество.

# Example 1:
# Input: g = [1,2,3], s = [1,1]
# Output: 1
# Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3.
# And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
# You need to output 1.

# Example 2:
# Input: g = [1,2], s = [1,2,3]
# Output: 2
# Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2.
# You have 3 cookies and their sizes are big enough to gratify all of the children,
# You need to output 2.

### Краткое условие:
# Ваша цель — максимизировать количество дочерних элементов контента и вывести максимальное количество.

# Алгоритм решение задачи:
# 0) Сортируем массивы g и s по возрастанию. Создаем пустые переменные left и right, result.
# 1) Проходимся циклом ваилд пока left не станет меньше размера длины массива g и right не станет меньше размера длины массива s,
# 1.1) Если число на которе установлн правый указатель на строке s больше или равно число на которе установлн левый указатель на строке s,
# 1.1.1) То увеличь переменную result на 1, и увеличь переменную left на 1 и увеличь переменную right на 1.
# 1.2) Иначе, увеличь переменную right на 1.
# 2) Верни переменную result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

g = [1, 2, 3]
s = [1, 1]

def findContentChildren(g, s):
    g.sort() # надо сортировать две строки иначе будет падать третий юнитест !!!
    s.sort()
    left = 0
    right = 0
    result = 0

    while left < len(g) and right < len(s): # пока левый и правый указатель не дойдут до конца своих строк
        if s[right] >= g[left]:
            result += 1
            left += 1
            right += 1
        else:
            right += 1

    return result

findContentChildren(g, s)

assert findContentChildren(g=[1, 2, 3], s=[1, 1]) == 1
assert findContentChildren(g=[1, 2], s=[1, 2, 3]) == 2
assert findContentChildren(g=[10, 9, 8, 7], s=[5, 6, 7, 8]) == 2