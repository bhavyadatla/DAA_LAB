def find_min_max(arr, low, high):
    if low == high:
        return arr[low], arr[low]
    if high == low + 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]
    mid = (low + high) // 2
    min1, max1 = find_min_max(arr, low, mid)
    min2, max2 = find_min_max(arr, mid + 1, high)
    return min(min1, min2), max(max1, max2)
if __name__ == "__main__":
    user_input = input("Enter a list of numbers separated by spaces: ")
    arr = list(map(int, user_input.split()))
    min_element, max_element = find_min_max(arr, 0, len(arr) - 1)
    print(f"Minimum element: {min_element}")
    print(f"Maximum element: {max_element}")