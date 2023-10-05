"""

2. LIFO/FIFO andmestruktuur.
Looge mõni peamine LIFO või FIFO andmestruktuur teie valitud programmeerimiskeeles.

Piirangud:
Ärge kasutage ühtegi sisseehitatud teeki lifo või fifo jaoks.

Esitamiseks:
Andmestruktuuri teostamiseks kood.
Dokumentatsioon, mis lühidalt selgitab teie koodi.
Analüüsige ja mõõtke oma sisestamise ja kustutamise toimingute ajaline keerukus, selgitage oma põhjendust.

"""

import openpyxl
from openpyxl.utils import get_column_letter
import time
import random

#Create an empty list with desired length
def lifo_create(capacity):
    array = [None] * capacity
    return array

#Add new element to the end of the list (first index that isnt empty)
def lifo_add(item):
    global end_index
    if end_index < capacity:
        work_array[end_index] = item
        end_index += 1
    else:
        print("The stack is full.")

#Remove the last element from the list
def lifo_remove():
    global end_index
    last_item = work_array.pop(end_index - 1)
    print(f"You removed the last item that was: {last_item}")
    end_index -= 1

#Take a look at the element that will come out next aka last added element
def peek():
    print(f"You peeked at the last element that was: {work_array[end_index-1]}")

#This function checks if the list is empty and returns boolean
def empty_check():
    if start_index == end_index:
        print("The list is empty.")
        return True

#This function checks list's size  
def size_check():
    size = end_index
    return size


#FROM HERE STARTS THE REAL CODE

# Define start, end indexes and also the capacity of the array
start_index = 0
end_index = 0
capacity = 10000

# Create a new Excel workbook and select the active sheet
workbook = openpyxl.Workbook()
sheet = workbook.active

# Add headers to my columns
sheet['A1'] = 'Index'
sheet['B1'] = 'Time µs'

# Number of rows to generate in excel Including the header row
num_rows = capacity + 1  

# Start from row 2 (since the first row is for headers)
for index in range(2, num_rows+1):
    # Write the index in column A
    sheet['A{}'.format(index)] = index - 2  # Subtract 2 to start from 0
    # Create the stack we want to work with
    work_array = lifo_create(index - 1)
    end_index = 0
    
    start_time = time.time_ns()
    for size in range(len(work_array)):
        # Calculate and write the time value in column B
        new_value = random.randint(0, 9)
        lifo_add(new_value)   

    end_time = time.time_ns()
    print(work_array)   
    total_time = int((end_time - start_time) / 1000)
    print(total_time, len(work_array))
    sheet['B{}'.format(index)] = total_time

# Save the workbook to a file
workbook.save('index_time_data.xlsx')

# Close the workbook
workbook.close()

print(work_array)



    