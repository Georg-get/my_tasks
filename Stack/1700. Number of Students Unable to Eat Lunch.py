### Условие задачи:
# В школьной столовой во время обеденного перерыва предлагаются круглые и квадратные бутерброды, обозначенные цифрами 0 и 1 соответственно.
# Все студенты стоят в очереди. Каждый студент предпочитает квадратные или круглые бутерброды.
# Количество бутербродов в столовой равно количеству студентов. Бутерброды складываются в стопку. На каждом этапе:
# Если студент, стоящий в начале очереди, предпочитает бутерброд, лежащий наверху стопки, он возьмет его и покинет очередь.
# В противном случае они покинут ее и перейдут в конец очереди.
# Это продолжается до тех пор, пока ни один из студентов в очереди не захочет взять верхний бутерброд и, следовательно, не сможет есть.
# Вам даны два целочисленных массива students, где sandwiches — sandwiches[i] тип сэндвича в стеке
# (это вершина стека) и — предпочтение студента в начальной очереди (это начало очереди).
# Возвращает количество студентов, которые не могут есть.i thi = 0students[j]j thj = 0

# Example 1:
# Input: students = [1,1,0,0], sandwiches = [0,1,0,1]
# Output: 0
# Explanation:
# - Front student leaves the top sandwich and returns to the end of the line making students = [1,0,0,1].
# - Front student leaves the top sandwich and returns to the end of the line making students = [0,0,1,1].
# - Front student takes the top sandwich and leaves the line making students = [0,1,1] and sandwiches = [1,0,1].
# - Front student leaves the top sandwich and returns to the end of the line making students = [1,1,0].
# - Front student takes the top sandwich and leaves the line making students = [1,0] and sandwiches = [0,1].
# - Front student leaves the top sandwich and returns to the end of the line making students = [0,1].
# - Front student takes the top sandwich and leaves the line making students = [1] and sandwiches = [1].
# - Front student takes the top sandwich and leaves the line making students = [] and sandwiches = [].
# Hence all students are able to eat.

# Example 2:
# Input: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
# Output: 3

### Краткое условие:
# Возвращает количество студентов, которые не могут есть.

# Алгоритм решение задачи:
# 0) Проходимся циклом ваилд пока длина массива sandwiches нестанет больше 0 и первый элемент массива sandwiches не будет в массиве students,
# 0.1) Удаляем из массива students первый элемент массива sandwiches,
# 0.2) Удаляем из массива sandwiches первый элемент.
# 1) Вернуть длину массива students.

# Сложность:
# 1) Время O(n^2)
# 2) Память O(1)

students = [1, 1, 0, 0]
sandwiches = [0, 1, 0, 1]

def countStudents(students, sandwiches):
    while len(sandwiches) > 0 and sandwiches[0] in students:
        students.remove(sandwiches[0])
        sandwiches.pop(0)
    # []
    return len(students) # 0

countStudents(students, sandwiches)

assert countStudents(students=[1, 1, 0, 0], sandwiches=[0, 1, 0, 1]) == 0
assert countStudents(students=[1, 1, 1, 0, 0, 1], sandwiches=[1, 0, 0, 0, 1, 1]) == 3