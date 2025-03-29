def merge(a, b):
    res = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    res.extend(a[i:])
    res.extend(b[j:])
    return res

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

if __name__ == "__main__":
    while True:
        inp = input("Enter numbers separated by spaces: ").strip()
        lst = list(map(int, inp.split()))  
        print("Original List:", lst)
        sorted_lst = merge_sort(lst)
        print("Sorted List:", sorted_lst)
        break
