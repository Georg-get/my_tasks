### Условие задачи:
# Вам дан целочисленный массив prices, где prices[i] указана цена товара в магазине.ith
# На товары в магазине действуют специальные скидки. Если вы купите товар, вы получите скидку,
# эквивалентную где минимальный индекс такой, что и.
# В противном случае вы вообще не получите никакой скидки.i th prices[j]jj > i prices[j] <= prices[i]
# Возвращает целочисленный массив, answer где answer[i]— окончательная цена,
# которую вы заплатите за товар в магазине с учетом специальной скидки.ith

# Example 1:
# Input: prices = [8,4,6,2,3]
# Output: [4,2,4,2,3]
#   Explanation:
#   For item 0 with price[0]=8 you will receive a discount equivalent to prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4.
#   For item 1 with price[1]=4 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2.
#   For item 2 with price[2]=6 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4.
#   For items 3 and 4 you will not receive any discount at all.

# Example 2:
# Input: prices = [1,2,3,4,5]
# Output: [1,2,3,4,5]

# Example 3:
# Input: prices = [10,1,1,6]
# Output: [9,0,1,6]

### Краткое условие:
# Пройтись по массиву, если i (первый элемент) больше j (второй элемент) то вычесть эти числа и записать в стек,
# если нет пропустить

# Алгоритм решение задачи:
# 0) Создать пустой массив stack
# 1) Пройтись циклом по массиву prices:
# 1.1) если i больше j (следуюшего элемента массиву prices), то i вычесть элемент массиву prices и это число добавить в массив stack
# 1.2) если i меньше j (следуюшего элемента массиву prices), то взять следуюший элемент массива и проверить больше ли он i,
# 1.2.1) если да, то i вычесть элемент массиву prices и это число добавить в массив stack
# 1.2.2) если нет, то добавь i в массив stack
# 2) вернуть return stack.

# Сложность:
# 1) Время O(n^2)
# 2) Память O(n)

prices = [8, 4, 6, 2, 3]

def finalPrices(prices):
    stack = []

    for i in range(len(prices)): # range(0, 5)
        for j in range(i + 1, len(prices)): # range(1, 5) range(2, 5) range(3, 5) range(4, 5) range(5, 5)

            if prices[i] >= prices[j]:
                stack.append(prices[i] - prices[j])
                break
        else: # для того чтобы добавить последнию цифру из массива prices в stack без измениений !!!
            stack.append(prices[i])
    # [4, 2, 4, 2, 3]
    return stack

finalPrices(prices)

assert finalPrices(prices=[8, 4, 6, 2, 3]) == [4, 2, 4, 2, 3]
assert finalPrices(prices=[1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert finalPrices(prices=[10, 1, 1, 6]) == [9, 0, 1, 6]