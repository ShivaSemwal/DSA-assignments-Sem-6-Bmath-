import random  # for sampling random no.s uniformly



def quicksort(arr, first, last):
    if first < last:


        pivot_value = arr[last]      # choose last element as pivot
        i = first              # position where next element <= pivot should be placed



        # partition into two groups: <= pivot and > pivot
        # we rearrange elements within the same array; pivot will later divide the array into these two groups (left ie <= pivot and right ie > pivot)
        j = first
        while j < last:
            if arr[j] <= pivot_value:                   # seeing if element belongs to the left group
                arr[i], arr[j] = arr[j], arr[i]         # move it to the left side
                i += 1                                  # move boundary of <= pivot group forward
            j += 1                                      # continue checking remaining elements



        # place pivot in its correct sorted position (between the two groups) ie i by swapping
        arr[i], arr[last] = arr[last], arr[i]
        pivot_index = i



        # recursively quicksort left and right groups
        quicksort(arr, first, pivot_index - 1)
        quicksort(arr, pivot_index + 1, last)






# generate random numbers between 0 and 1000000 and then use quicksort


# n = int(input("Enter the total numbers to be randomly generated: "))
# arr = [random.randint(0, 1000000) for _ in range(n)]

arr = [random.randint(0, 1000000) for _ in range(1000)]

print("The numbers generated are:", arr )


quicksort(arr, 0, 999)


print("Sorted numbers are:")
print(arr)
