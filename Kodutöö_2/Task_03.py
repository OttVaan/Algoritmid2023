"""
Ülesanne 3: Insertion Sort praktikas (1p)
Antud on osaliselt sorteeritud loend: [12, 11, 13, 5, 6, 7]. 
Rakenda Insertion Sort algoritmi. 
Selgita, miks Insertion Sort võib olla tõhusam sellele loendile võrreldes täielikult sortimata loendiga.

SELGITUS:
Kui me hakkame asetame uut elementi oma sorteeritud listi ja see on juba osaliselt sorteeritud,
siis on võimalik, et me ei pea nii palju võrdlusi tegema. Võib juhtuda, et element on juba õigel kohal.

Näide: listis [3, 5, 7, 10, 8, 14] tahame liigutada 10 õigele kohale, aga ta on juba sorteeritud listis õigel kohal.

"""

start_list = [12, 11, 13, 5, 6, 7]      #Our starting list

def InsertionSort(arr):                 #Insertion sorting algorithm

    len_arr = len(arr)
    steps = 0
    print(f"Step {steps}: {arr}")

    for i in range(1, len_arr):                                #Go through the list with every element
        steps += 1
        for j in range(i, -1, -1):                          #go through the sorted part of list in backwards

            if arr[i] < arr[j] and arr[i] > arr[j-1]:       #if we find smaller on left and bigger on right
                memory = arr[i]                             #store the value
                arr.remove(memory)                          #remove from the list
                arr.insert(j, memory)                       #add back to correct position
                break                                       #break from loop to optimize
            
            elif j == 0 and arr[i] < arr[0]:                #if we reached the start of our sorted list            
                memory = arr[i]                             #store the value
                arr.remove(memory)                          #remove from the list
                arr.insert(0, memory)                       #add back to correct position
                break                                       #break from loop to optimize
            
        print(f"Step {steps}: {arr}")


def InsertionSortFirst(arr):                 

    len_arr = len(arr)
    steps = 0

    for i in range(1, len_arr):                               
        steps += 1
        for j in range(i, -1, -1):                         

            if arr[i] < arr[j] and arr[i] > arr[j-1]:     
                memory = arr[i]       
                arr.remove(memory)         
                arr.insert(j, memory)              
                break                             
            
            elif j == 0 and arr[i] < arr[0]:                      
                memory = arr[i]       
                arr.remove(memory)         
                arr.insert(0, memory)                       
                break                                       
        if steps == 1:    
            print(f"Insertion // Step {steps}: {arr}")

if __name__ == "__main__":
    InsertionSort(start_list)


