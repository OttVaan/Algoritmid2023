"""
Ülesanne 1: Bubble Sort simulatsioon (1p)
Antud on järgnevate arvude loend: [64, 34, 25, 12, 22, 11, 90]. 
Simuleeri samm-sammult Bubble Sort algoritmi. 
Iga läbimise järel kirjuta üles tulemuseks olev loend.
"""


start_list = [64, 34, 25, 12, 22, 11, 90]

def BubbleSort(arr):        #bubble sort algorithm

    did_sort = True         #var for checking if we moved something
    steps = 0               #counter for steps
    print(f"Step 0: {arr}")


    while did_sort:         #main loop until we didnt have to move anything
        did_sort = False
        list_len = len(arr)

        for i in range(list_len-1):
            if arr[i] > arr[i+1]:
                memory = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = memory
                did_sort = True
                steps += 1
                print(f"Step {steps}: {arr}")
        
        if not did_sort:    #Print final result when we didnt change anything

            print(f"Sorted list: {arr}")




def BubbleSortFirst(arr):        

    did_sort = True         
    steps = 0               


    while did_sort:
        did_sort = False
        list_len = len(arr)

        for i in range(list_len-1):
            if arr[i] > arr[i+1]:
                memory = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = memory
                did_sort = True
                steps += 1
                if steps == 1:
                    print(f"Bubble // Step {steps}: {arr}")
        
        if not did_sort:
            break

if __name__ == "__main__":        
    BubbleSort(start_list)
