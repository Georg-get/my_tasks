### Условие задачи:
# Вам дан целочисленный массив ranks и массив символов suits. У вас есть 5 карты,
# у которых ранг и масть карты равны .ith ranks[i] suits[i]
# Ниже приведены типы покерных комбинаций, от лучших к худшим:
# "Flush": Пять карт одной масти.
# "Three of a Kind": Три карты одного ранга.
# "Pair": Две карты одного ранга.
# "High Card": любая отдельная карта.
# Возвращает строку, представляющую лучший тип покерной комбинации, которую вы можете собрать с данными картами.
# Обратите внимание, что возвращаемые значения чувствительны к регистру.

# Example 1:
# Input: ranks = [13,2,3,1,9], suits = ["a","a","a","a","a"]
# Output: "Flush"
# Explanation: The hand with all the cards consists of 5 cards with the same suit, so we have a "Flush".

# Example 2:
# Input: ranks = [4,4,2,4,4], suits = ["d","a","a","b","c"]
# Output: "Three of a Kind"
# Explanation: The hand with the first, second, and fourth card consists of 3 cards with the same rank, so we have a "Three of a Kind".
# Note that we could also make a "Pair" hand but "Three of a Kind" is a better hand.
# Also note that other cards could be used to make the "Three of a Kind" hand.

# Example 3:
# Input: ranks = [10,10,2,12,9], suits = ["a","b","c","a","d"]
# Output: "Pair"
# Explanation: The hand with the first and second card consists of 2 cards with the same rank, so we have a "Pair".
# Note that we cannot make a "Flush" or a "Three of a Kind".

### Краткое условие:
# Вернуть комбинацию из покера.

# Алгоритм решение задачи:
# 0) Создаем два пустых словаря dictSuits и dictRanks.
# 1) Проходимся циклом по диапазону массива suits,
# 1.1) Если значение массив suits i есть как ключ в словаре dictSuits, то увеличь значние ключа i на 1.
# 1.2) Если значение массив suits i НЕТу как ключ в словаре dictSuits, то добавь ключ i со значением 1 в словарь dictSuits.
# 1.3) Если 5 есть значение в словаре dictSuits, то верни "Flush".
# 2) Проходимся циклом по диапазону массива ranks,
# 2.1) Если значение массив ranks j есть как ключ в словаре dictRanks, то увеличь значние ключа j на 1.
# 2.2) Если значение массив ranks j НЕТу как ключ в словаре dictRanks, то добавь ключ j со значением 1 в словарь dictRanks.
# 2.3) Если 3 есть значение в словаре dictRanks, то верни "Three of a Kind".
# 3) Если 2 есть значение в словаре dictRanks, то верни "Pair".
# 4) Вернуть "High Card".

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

ranks = [13, 2, 3, 1, 9]
suits = ["a", "a", "a", "a", "a"]

def bestHand(ranks, suits):
    dictSuits = {}
    dictRanks = {}

    for i in range(len(suits)):

        if suits[i] in dictSuits.keys():
            dictSuits[suits[i]] += 1
        else:
            dictSuits[suits[i]] = 1
        # {'a': 5}  это со первым тест кейсом данные
        if 5 in dictSuits.values():
            return "Flush"

    for j in range(len(ranks)):

        if ranks[j] in dictRanks.keys():
            dictRanks[ranks[j]] += 1
        else:
            dictRanks[ranks[j]] = 1
        # {4: 3, 2: 1}   это со вторым тест кейсом данные
        if 3 in dictRanks.values():
            return "Three of a Kind"
    # {10: 2, 2: 1, 12: 1, 9: 1} это со третим тест кейсом данные
    if 2 in dictRanks.values():
        return "Pair"

    return "High Card"

bestHand(ranks, suits)

assert bestHand(ranks=[13, 2, 3, 1, 9], suits=["a", "a", "a", "a", "a"]) == "Flush"
assert bestHand(ranks=[4, 4, 2, 4, 4], suits=["d", "a", "a", "b", "c"]) == "Three of a Kind"
assert bestHand(ranks=[10, 10, 2, 12, 9], suits=["a", "b", "c", "a", "d"]) == "Pair"