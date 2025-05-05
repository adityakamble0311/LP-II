def selection_sort(arr):
    # Loop through each element in the list
    for i in range(len(arr)):
        # Assume current element is the smallest
        min_index = i

        # Find the smallest element in remaining unsorted array
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum with current element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

arr = [29, 10, 14, 37, 13]
print("Original:", arr)
sorted_arr = selection_sort(arr)
print("Sorted:", sorted_arr)
