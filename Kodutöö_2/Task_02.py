"""
Ülesanne 2: Selection Sort visualiseerimine (1p)
Joonista plokkskeem, mis esindab Selection Sort algoritmi. 
Kasutades seda vooluskeemi, demonstreeri sortimisprotsessi loendile: [29, 15, 56, 77, 18]. 
Tuvasta iga iteratsiooni ajal väikseim element.
"""

start_list = [29, 15, 56, 77, 18]           #Our test list

def SelectionSort(arr):                     #Selection sort algorithm

    arr_len = len(arr)
    steps = 0
    print(f"Step 0: {arr}")

    for index in range(arr_len-1):          #go through the list len - 1 times (dont need to chceck last)
        smallest = arr[index]               #at the beginning smallest is at index
        smallest_index = index
        for comp in range(index, arr_len):  #need to start from index not full start
            if arr[comp] < smallest:        #check if next in array is the smallest that we have seen this run
                smallest = arr[comp]
                smallest_index = comp

        arr[smallest_index] = arr[index]    #change positions of smallest and our run start
        arr[index] = smallest
        steps += 1
        print(f"Step {steps}: {arr}")       #print step

def SelectionSortFirst(arr):                

    arr_len = len(arr)
    steps = 0

    for index in range(arr_len-1):         
        smallest = arr[index]              
        smallest_index = index
        for comp in range(index, arr_len):  
            if arr[comp] < smallest:     
                smallest = arr[comp]
                smallest_index = comp

        arr[smallest_index] = arr[index]  
        arr[index] = smallest
        steps += 1
        if steps == 1:
            print(f"Selection // Step {steps}: {arr}")     

if __name__ == "__main__":        
    SelectionSort(start_list)
        
        