import math


def conquer_combine(prices, left_max_profit, left_buy, left_sell, right_max_profit, right_buy,
                    right_sell, start, stop, mid):
    """

    :param prices:  list of prices where index represent day and value represent share value
    :param left_max_profit: max profit from left sub tree in recursion
    :param left_buy: index of prices array for best buy from left sub tree in recursion
    :param left_sell: index of prices array for best sell from left sub tree in recursion
    :param right_max_profit:  max profit from right sub tree in recursion
    :param right_buy: index of prices array for best buy from right sub tree in recursion
    :param right_sell: index of prices array for best sell from right sub tree in recursion
    :param start: starting index
    :param stop: ending index
    :param mid: split index
    :return: max profit, buy index (i), sell index(j)
    """
    max_buy_idx = start
    max_buy_val = prices[start]
    max_sell_idx = mid
    max_sell_val = prices[mid]

    for k in range(start + 1, mid+1):
        if prices[k] < max_buy_val:
            max_buy_val = prices[k]
            max_buy_idx = k

    for k in range(mid + 1, stop + 1):
        if prices[k] > max_sell_val:
            max_sell_val = prices[k]
            max_sell_idx = k

    # find the profit between two sub problems
    max_profit_between_sub_problems = max_sell_val - max_buy_val

    if right_max_profit > left_max_profit:
        if max_profit_between_sub_problems > right_max_profit:
            return max_profit_between_sub_problems, max_buy_idx, max_sell_idx
        else:
            return right_max_profit, right_buy, right_sell
    else:
        if max_profit_between_sub_problems > left_max_profit:
            return max_profit_between_sub_problems, max_buy_idx, max_sell_idx
        else:
            return left_max_profit, left_buy, left_sell


def max_investment_return(prices, start, end):
    """
    :param prices: array of prices with index (0, 1, n-1) where value represent the price
    :param start: starting index of array
    :param end: end index of array
    :return: return max_profit, buy_index (i) and sell_index(j)
    """
    n = end - start
    if n == 0:
        return 0, start, start
    if n == 1:
        return prices[end] - prices[start], start, end

    mid = math.floor(end / 2)
    max_profit1, buy1, sell1 = max_investment_return(prices, start, mid)
    max_profit2, buy2, sell2 = max_investment_return(prices, mid + 1, end)
    return conquer_combine(prices, max_profit1, buy1, sell1, max_profit2, buy2, sell2, start, end, mid)


A = [9, 1, 5]
A1 = [2, 6, 1, 14, 7]
print("Max Profit: %d, i: %d, j: %d" % max_investment_return(A, 0, len(A)-1))
print("Max Profit: %d, i: %d, j: %d" % max_investment_return(A1, 0, len(A1)-1))
