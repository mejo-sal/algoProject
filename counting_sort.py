def counting_sort(arr):
    # Step 1: Find the maximum value in the array
    max_val = max(arr)
    
    # Step 2: initialize the counting array
    count = [0] * (max_val + 1)
    
    # Step 3: Count the frequency of each element
    for num in arr:
        count[num] += 1
    
    # Step 4: reconstruct the sorted array
    sorted_index = 0
    for i in range(len(count)):
        while count[i] > 0:
            arr[sorted_index] = i
            sorted_index += 1
            count[i] -= 1
            print("count Array:", count)
    
    return arr

# example 
input_array = [15,4, 2, 2, 8, 5,3, 3, 1]
sorted_array = counting_sort(input_array)
print("Sorted Array:", sorted_array)

