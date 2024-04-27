def find_division_index(arr):
    left = 0
    right = len(arr)-1
    
    
    while left<=right:
        mid = (left+right) // 2                 
        
        
        if arr[mid] == 0 and arr[mid+1] == 1:   
            return mid+1                       
        elif arr[mid] == 0:                      
            left = mid + 1
        else:
            right = mid -1

    return - 1


arr = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1] 
print("Место разделения: Индекс", find_division_index(arr))