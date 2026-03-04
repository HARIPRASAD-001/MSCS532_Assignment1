def insertion_sort_desc(arr):
    """
    Sorts an array in monotonically decreasing order
    using the Insertion Sort algorithm.
    """
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1

        # Modify comparison for decreasing order
        while i >= 0 and arr[i] < key:
            arr[i + 1] = arr[i]
            i -= 1

        arr[i + 1] = key

    return arr
if __name__ == "__main__":
    sample_array = [5, 2, 9, 1, 7, 6]
    print("Original Array:", sample_array)

    sorted_array = insertion_sort_desc(sample_array)
    print("Sorted Array (Decreasing Order):", sorted_array)
