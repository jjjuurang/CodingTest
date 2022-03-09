def binary_search(arr, length, target):
    start = 0   				
    end = arr[-1] 			

    while (end - start >= 0):
        mid = (start + end) // 2 
        sum = 0
            
        for i in arr:
            sum += i // mid

        if (sum == target):	  
            return mid				

        elif (sum > target):   
            start = mid + 1 		

        else:                   	
            end = mid - 1 			
    return 0

arr = [int(input()) for i in range(4)] 

print(binary_search(arr, len(arr), 10))