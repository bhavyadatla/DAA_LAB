def knapsack_greedy(wts, profit, capacity):
    n = len(wts)
    items = [(profit[i] / wts[i], wts[i], profit[i]) for i in range(n)]
    items.sort(reverse=True, key=lambda x: x[0])
    total_value = 0
    for ratio, wt, value in items:
        if capacity >= wt:
            capacity -= wt
            total_value += value
        else:
            total_value += ratio * capacity
            break

    return total_value

n = int(input("Enter number of items: "))
wts = list(map(int, input("Enter weights separated by space: ").split()))
values = list(map(int, input("Enter profits: ").split()))
capacity = int(input("Enter knapsack capacity: "))

max_profit = knapsack_greedy(wts, values, capacity)
print(f"Optimal profit: {max_profit}")

