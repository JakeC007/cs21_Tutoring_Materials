def binary_search(lst, search):

    low = 0
    
    high = len(lst) - 1
    
    while low <= high:
    
        middle = int((low + high)/2)
        
        if search == lst[middle]:
            return True 
            
        elif search > lst[middle]:
            low = middle + 1
            
        else: # too low
            high = middle -1
            
    return False 
