
def selection_sort(arr):
    for i in range(len(arr)):
        min_in = i

        for j in range(i+1,len(arr)):
            if arr[j]< arr[min_in]:
                min_in = j

        arr[i],arr[min_in]=arr[min_in],arr[i]

arr=[12,13,11,20,30,19,18]
print("orignal arr :",arr)
selection_sort(arr)
print("Sorted arr :",arr)
