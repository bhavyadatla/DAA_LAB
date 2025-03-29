def find_subsets(arr, target):
    def list_subsets(index, total, subset):
        if total == target:
            results.append(subset[:])
            return
        if index >= len(arr) or total > target:
            return
        subset.append(arr[index])
        list_subsets(index + 1, total + arr[index], subset)
        subset.pop()
        list_subsets(index + 1, total, subset)

    results = []
    list_subsets(0, 0, [])
    print("Subsets with the given sum:" if results else "No subset found with the given sum.")
    for subset in results:
        print(subset)

if __name__ == "__main__":
    arr = list(map(int, input("Enter the elements: ").split()))
    find_subsets(arr, int(input("Enter the target sum: ")))
