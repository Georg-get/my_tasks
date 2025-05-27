### Условие задачи:
# В лаборатории проводится эксперимент. Для обеспечения точности два датчика собирают данные одновременно.
# Вам даны два массива sensor1 и sensor2, где sensor1[i] и sensor2[i] — это i-е точки данных, собранные двумя датчиками.
# Однако этот тип датчика может оказаться неисправным, что приведет к удалению ровно одной точки данных.
# После удаления данных все точки данных справа от удаленных данных сдвигаются на одну позицию влево, а последняя точка данных заменяется некоторым случайным значением.
# Гарантируется, что это случайное значение не будет равно удаленному значению.
# Например, если правильными данными являются [1,2,3,4,5] и удалено 3, датчик может вернуть [1,2,4,5,7] (последняя позиция может быть любым значением, а не только 7).
# Мы знаем, что есть дефект не более чем в одном из датчиков. Верните номер датчика (1 или 2) с дефектом.
# Если ни один из датчиков не имеет дефекта или невозможно определить неисправный датчик, вернуть -1.

# Example 1:
# Input: sensor1 = [2,3,4,5], sensor2 = [2,1,3,4]
# Output: 1
# Explanation: Sensor 2 has the correct values.
# The second data point from sensor 2 is dropped, and the last value of sensor 1 is replaced by a 5.

# Example 2:
# Input: sensor1 = [2,2,2,2,2], sensor2 = [2,2,2,2,5]
# Output: -1
# Explanation: It is impossible to determine which sensor has a defect.
# Dropping the last value for either sensor could produce the output for the other sensor.

# Example 3:
# Input: sensor1 = [2,3,2,2,3,2], sensor2 = [2,3,2,3,2,7]
# Output: 2
# Explanation: Sensor 1 has the correct values.
# The fourth data point from sensor 1 is dropped, and the last value of sensor 1 is replaced by a 7.

### Краткое условие:
# Необходимо определить, какой из датчиков (1 или 2) неисправен.
# Если оба датчика работают корректно или невозможно определить неисправный, вернуть -1.

# Алгоритм решение задачи:
# 0) Ставим левый указатель в начало строки, а правый указатель в конец строки sensor1.
# 1) Проходимся циклом ваилд пока левый указать не встретися с правым,
# 1.1) Если левый указатель установленый на массив sensor1 не равен sensor2, то выйди из цикла !
# 1.2) Двигаем левый указатель на 1.
# 2) Проходимся циклом ваилд пока левый указать не встретися с правым,
# 2.1) Если число из массива sensor1 где установлен левый указатель +1 не равна числу из массива sensor2 где левый указатель, верни 1.
# 2.2) Если число из массива sensor1 где установлен левый указатель не равна числу из массива sensor2 где левый указатель +1, верни 2.
# 2.3) Двигаем левый указатель на 1.
# 3) Верни -1.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

sensor1 = [2, 3, 4, 5]
sensor2 = [2, 1, 3, 4]

def badSensor(sensor1, sensor2):
    left = 0
    right = len(sensor1)

    while left < right - 1:
        if sensor1[left] != sensor2[left]:
            break
        left += 1

    while left < right - 1:

        if sensor1[left + 1] != sensor2[left]:
            return 1

        elif sensor1[left] != sensor2[left + 1]:
            return 2

        left += 1

    return -1

badSensor(sensor1, sensor2)

assert badSensor(sensor1=[2, 3, 4, 5], sensor2=[2, 1, 3, 4]) == 1
assert badSensor(sensor1=[2, 2, 2, 2, 2], sensor2=[2, 2, 2, 2, 5]) == -1
assert badSensor(sensor1=[2, 3, 2, 2, 3, 2], sensor2=[2, 3, 2, 3, 2, 7]) == 2

### Оригинал решение ####
# class Solution:
#     def badSensor(self, sensor1: List[int], sensor2: List[int]) -> int:
#         i, n = 0, len(sensor1)
#         while i < n - 1:
#             if sensor1[i] != sensor2[i]:
#                 break
#             i += 1
#         while i < n - 1:
#             if sensor1[i + 1] != sensor2[i]:
#                 return 1
#             if sensor1[i] != sensor2[i + 1]:
#                 return 2
#             i += 1
#         return -1

### Старое решение через два указателя !!!

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

# sensor1 = [2, 3, 4, 5]
# sensor2 = [2, 1, 3, 4]
#
# def badSensor(sensor1, sensor2):
#     def canReplace(listOne, listTwo):
#         left = 0
#         right = 0
#         droppedValue = -1
#
#         while left < len(listOne):
#             if listOne[left] == listTwo[right]:
#                 left += 1
#                 right += 1
#             else:
#                 droppedValue = listOne[left]
#                 left += 1
#
#         if right == len(listTwo) - 1 and listTwo[-1] != droppedValue:
#             return True
#         else:
#             return False
#
#     oneDefect = canReplace(sensor2, sensor1) # True
#     twoDefect = canReplace(sensor1, sensor2) # False
#
#     if oneDefect == True and twoDefect ==True:
#         return -1
#
#     elif oneDefect == False and twoDefect == False:
#         return -1
#
#     else:
#         if oneDefect == True: # для первого юнитеста !!!
#             return 1
#         else:
#             return 2
#
# badSensor(sensor1, sensor2)

### Оригинал решение (Старое решение через два указателя !!!) ####
# class Solution:
#   def badSensor(self, sensor1: list[int], sensor2: list[int]) -> int:
#     # A -> B, so B is defect
#     def canReplace(A, B):
#       i = 0  # A's index
#       j = 0  # B's index
#       droppedValue = -1
#
#       while i < len(A):
#         if A[i] == B[j]:
#           i += 1
#           j += 1
#         else:
#           droppedValue = A[i]
#           i += 1
#
#       return j == len(B) - 1 and B[-1] != droppedValue
#
#     oneDefect = canReplace(sensor2, sensor1)
#     twoDefect = canReplace(sensor1, sensor2)
#     if oneDefect and twoDefect:
#       return -1
#     if not oneDefect and not twoDefect:
#       return -1
#     return 1 if oneDefect else 2
