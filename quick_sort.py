def quicksort(ar, lb, ub):
    if lb < ub:
        p = partition(ar, lb, ub)
        quicksort(ar, lb, p - 1)
        quicksort(ar, p + 1, ub)
def partition(ar, lb, ub):
    pivot = ar[lb]
    l = lb
    r = ub
    while l < r:
        while ar[l] <= pivot and l < r:
            l += 1
        while ar[r] > pivot:
            r -= 1
        if l < r:
            ar[l], ar[r] = ar[r], ar[l]
    ar[lb], ar[r] = ar[r], ar[lb]
    return r
if __name__ == "__main__":
    l = input("Enter a list of numbers separated by spaces: ")
    a = list(map(int, l.split()))
    print("List before sorting:")
    print(a)
    quicksort(a, 0, len(a) - 1)
    print("List after sorting:")
    print(a)