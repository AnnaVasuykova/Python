def find_division_index(mas):
    start = 0
    end = len(mas)-1
    
    
    while start<=end:
        mid = (start+end) // 2                 
        
        
        if mas[mid] == 0 and mas[mid+1] == 1:   
            return mid+1                       
        elif mas[mid] == 0:                      
            start = mid + 1
        else:
            end = mid -1

    return - 1


mas = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1] 
print("Место разделения: Индекс", find_division_index(mas))