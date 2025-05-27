### Условие задачи:
# Вы участвуете в соревновании, и вам даны два положительных целых числа initialEnergy и, initialExperience
# обозначающие вашу начальную энергию и начальный опыт соответственно.
# Вам также даны два целочисленных массива с индексом 0energy и experience, оба длиной n.
# Вы столкнетесь с n противниками в порядке. Энергия и опыт противника обозначаются и соответственно.
# Когда вы сталкиваетесь с противником, вам нужно иметь как строго больший опыт, так и энергию,
# чтобы победить его и перейти к следующему противнику, если таковой имеется. ithenergy[i] experience[i]
# Победа над противником увеличивает ваш опыт на, но уменьшает вашу энергию на .ithexperience[i] energy[i]
# Перед началом соревнований вы можете тренироваться в течение некоторого количества часов.
# После каждого часа тренировки вы можете либо увеличить свой начальный опыт на единицу, либо увеличить свою начальную энергию на единицу.
# Верните минимальное количество часов тренировок, необходимое для победы над всем и n противниками.

# Example 1:
# Input: initialEnergy = 5, initialExperience = 3, energy = [1,4,3,2], experience = [2,6,3,1]
# Output: 8
# Explanation: You can increase your energy to 11 after 6 hours of training, and your experience to 5 after 2 hours of training.
# You face the opponents in the following order:
# - You have more energy and experience than the 0th opponent so you win.
#   Your energy becomes 11 - 1 = 10, and your experience becomes 5 + 2 = 7.
# - You have more energy and experience than the 1st opponent so you win.
#   Your energy becomes 10 - 4 = 6, and your experience becomes 7 + 6 = 13.
# - You have more energy and experience than the 2nd opponent so you win.
#   Your energy becomes 6 - 3 = 3, and your experience becomes 13 + 3 = 16.
# - You have more energy and experience than the 3rd opponent so you win.
#   Your energy becomes 3 - 2 = 1, and your experience becomes 16 + 1 = 17.
# You did a total of 6 + 2 = 8 hours of training before the competition, so we return 8.
# It can be proven that no smaller answer exists.

# Example 2:
# Input: initialEnergy = 2, initialExperience = 4, energy = [1], experience = [3]
# Output: 0
# Explanation: You do not need any additional energy or experience to win the competition, so we return 0.

### Краткое условие:
# Верните минимальное количество часов тренировок, необходимое для победы над всем и n противниками.

# Полное объяснение решение задачи:
# 0) Создаем переменные exdif и ensum со значение 0.
# 1) Проходимся циклом по индексам массива energy,
# 1.1) Если число initialExperience меньше или ранво числу из массива experience,
# 1.1.1) То exdif равно максимальному числу из ( 1, exdif, experience[i] + 1 - initialExperience ).
# 1.2) Увеличиваем initialExperience на число из массива experience.
# 1.3) Увеличиваем ensum на число из массива energy.
# 2) Верни максивум из ensum - initialEnergy + 1, 0 + exdif

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

initialEnergy = 5
initialExperience = 3
energy = [1, 4, 3, 2]
experience = [2, 6, 3, 1]

def minNumberOfHours(initialEnergy, initialExperience, energy, experience):
    exdif = 0
    ensum = 0

    for i in range(len(energy)):

        if initialExperience <= experience[i]:
            exdif = max(1, exdif, experience[i] + 1 - initialExperience)

        initialExperience += experience[i] # Защита от 1 юнитеста
        ensum += energy[i]

                #10                #5+1   0    # 2
    return max(ensum - initialEnergy + 1, 0) + exdif

minNumberOfHours(initialEnergy, initialExperience, energy, experience)

assert minNumberOfHours(initialEnergy=5, initialExperience=3, energy=[1, 4, 3, 2], experience=[2, 6, 3, 1]) == 8 # от него
assert minNumberOfHours(initialEnergy=2, initialExperience=4, energy=[1], experience=[3]) == 0