### Условие задачи:
# Вам дана строка длины, 5 называемая time, представляющая текущее время на цифровых часах в формате "hh:mm".
# Самое раннее возможное время —, "00:00"а самое позднее возможное время — "23:59".
# В строке time цифры, представленные символом ?, неизвестны и должны быть заменены цифрой от 0 до 9.
# Возвращает целое число answer — количество допустимых значений времени, которые можно создать, заменив каждое ? на цифру от 0 до 9.

# Example 1:
# Input: time = "?5:00"
# Output: 2
# Explanation: We can replace the ? with either a 0 or 1, producing "05:00" or "15:00". Note that we cannot replace it with a 2, since the time "25:00" is invalid. In total, we have two choices.

# Example 2:
# Input: time = "0?:0?"
# Output: 100
# Explanation: Each ? can be replaced by any digit from 0 to 9, so we have 100 total choices.

# Example 3:
# Input: time = "??:??"
# Output: 1440
# Explanation: There are 24 possible choices for the hours, and 60 possible choices for the minutes. In total, we have 24 * 60 = 1440 choices.

### Краткое условие:
# Возвращает целое число answer — количество допустимых значений времени,
# которые можно создать, заменив каждое ? на цифру от 0 до 9.

# Полное объяснение решение задачи:
# 0) Создаем переменную ans со значением 1.
# 1) Если первый символ в строке time это "?",
# 1.1) Если второй символ в строке time это "?", то ans равно 24.
# 1.2) Если второй символ в строке time это "0" или "1" или "2" или "3" , то ans равно 3.
# 1.3) Иначе, ans равно 2.
# 2) Если второй символ в строке time это "?",
# 2.1) Если первый символ в строке time это "?", то ans равно 24.
# 2.2) Если первый символ в строке time это "2", то ans равно 4.
# 2.3) Иначе, ans равно 10.
# 3) Если четвертый символ в строке time это "?", то умнож ans на 6.
# 4) Если пятый символ в строке time это "?", то умнож ans на 10.
# 5) Верни ans.

# Сложность:
# 1) Время O(1)
# 2) Память O(1)

time = "?5:00"

def countTime(time):
    ans = 1

    if time[0] == '?':

        if time[1] == '?':
            ans = 24
        elif time[1] in '0123':
            ans = 3
        else:
            ans = 2

    elif time[1] == '?':

        if time[0] == '?':
            ans = 24
        elif time[0] == '2':
            ans = 4
        else:
            ans = 10

    if time[3] == '?':
        ans *= 6

    if time[4] == '?':
        ans *= 10

    return ans

countTime(time)

assert countTime(time="?5:00") == 2
assert countTime(time="0?:0?") == 100
assert countTime(time="??:??") == 1440