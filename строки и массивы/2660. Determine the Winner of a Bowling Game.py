### Условие задачи:
# Вам даны два целочисленных массива с индексом 0 player1 и player2, представляющие количество кеглей,
# сбитых игроком 1 и игроком 2 в боулинге соответственно.
# Игра в боулинг состоит из n ходов, и количество кеглей за каждый ход равно ровно 10.
# Предположим, что игрок сбивает кегли в i-м ходу. Значение i -го хода для игрока:xi
# 2xi если игрок сбивает 10 кеглей в (i - 1)-й или (i - 2) -й ход .
# В противном случае это .xi
# Результат игрока представляет собой сумму очков его n ходов.
# Возвращаться 1, если счет игрока 1 больше счета игрока 2, 2 если счет игрока 2 больше счета игрока 1, и 0 в случае ничьей.

# Example 1:
# Input: player1 = [5,10,3,2], player2 = [6,5,7,3]
# Output: 1
# Explanation:
# The score of player 1 is 5 + 10 + 2*3 + 2*2 = 25.
# The score of player 2 is 6 + 5 + 7 + 3 = 21.

# Example 2:
# Input: player1 = [3,5,7,6], player2 = [8,10,10,2]
# Output: 2
# Explanation:
# The score of player 1 is 3 + 5 + 7 + 6 = 21.
# The score of player 2 is 8 + 10 + 2*10 + 2*2 = 42.

# Example 3:
# Input: player1 = [2,3], player2 = [4,1]
# Output: 0
# Explanation:
# The score of player1 is 2 + 3 = 5.
# The score of player2 is 4 + 1 = 5.

# Example 4:
# Input: player1 = [1,1,1,10,10,10,10], player2 = [10,10,10,10,1,1,1]
# Output: 2
# Explanation:
# The score of player1 is 1 + 1 + 1 + 10 + 2*10 + 2*10 + 2*10 = 73.
# The score of player2 is 10 + 2*10 + 2*10 + 2*10 + 2*1 + 2*1 + 1 = 75.

### Краткое условие:
# Возвращаться 1, если счет игрока 1 больше счета игрока 2, 2, если счет игрока 2 больше счета игрока 1, и 0 в случае ничьей.

# Полное объяснение решение задачи:
# 0) Создаем функцию getTotalScore которая берет массив,
# 0.1) Создаем переменную count созначение 0,
# 0.2) Проходимся циклом по индексам массива,
# 0.2.1) Создаем переменную score в которой хранится число которое мы вызываем по индексу из массива p.
# 0.2.2) Если индекс (idx) больше 0 и преведущее число равно 10 или индекс (idx) больше 1 и переведушие превердушие число равно 10,
# 0.2.2.1) То увеличиваем count на 2 умноженое на score.
# 0.2.3) Иначе, увеличиваем count на score.
# 0.3) Вернуть count.
# 1) score1 равно результату функции getTotalScore в которую мы передали массив player1.
# 2) score2 равно результату функции getTotalScore в которую мы передали массив player2.
# 3) Если score1 больше score2, то верни 1.
# 4) Если score1 меньше score2, то верни 2.
# 5) Если score1 ранво score2, то верни 0.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

player1 = [5, 10, 3, 2]
player2 = [6, 5, 7, 3]

def isWinner(player1, player2):
    def getTotalScore(p):
        count = 0 # массив player1 = > 5 => 15 => 21 => 25
                  # массив player2 = > 6 => 11 => 18 => 21

        for idx in range(len(p)): # range(0, 4)
            score = p[idx]
            if idx > 0 and (p[idx - 1] == 10 or (idx > 1 and p[idx - 2] == 10)):
                count += 2 * score  # массив player1 сюда попадает 3 и 2
                                    # массив player2 сюда попадает не чего
            else:
                count += score # массив player1 сюда попадает 5 и 10
                                # массив player2 сюда попадает 6 и 11, 7, 3
        return count

    score1 = getTotalScore(player1) # 25
    score2 = getTotalScore(player2) # 21
        # 25  > 21
    if score1 > score2:
        return 1
    elif score1 < score2:
        return 2
    elif score1 == score2:
        return 0

isWinner(player1, player2)

assert isWinner(player1=[5, 10, 3, 2], player2=[6, 5, 7, 3]) == 1
assert isWinner(player1=[3, 5, 7, 6], player2=[8, 10, 10, 2]) == 2
assert isWinner(player1=[2, 3], player2=[4, 1]) == 0
assert isWinner(player1=[1, 1, 1, 10, 10, 10, 10], player2=[10, 10, 10, 10, 1, 1, 1]) == 2