"""
Küsimus 2:

Binary searchi aegkompleksust:
Best case: Otsitav element on täpselt listi keskel. O(1)
Worst case: Otsitav element on otstes ja kuna otsitav hulk läheb iga korraga poole väiksemaks kasutame log2N ehk O(log N)
Averag case: kehtib suures pildis sama, mis worst case O(log N)

Võrdleme Binary search vs Linear search ajalist keerukust. Väikeste hulkade juures ei ole vahe eriti suur.
Kui list muutub pikemaks, siis linear search läheb lineaarselt aeglasemaks, aga binary keerukus jääb suures pildis "konstantseks".



Küsimus 3: Binary search on kasulikum olukorras, kus meie andmed on juba sorteeritud. Sellisel juhul saaks binary sort välistada 
juba esimesel sammul terve esimese poole, mille linear search ikka läbi peab käima.

"""

#Kood on 1:1 võetud kodutöö 1.4
import math

def binary_search(sorted_list, element):
    start = 0
    end = len(sorted_list) - 1
    mid_point = round((end - start) / 2)
    answer_index = 0
    
    while True:  
        #Vaatame kas meie element on hulga esimene element
        if element == sorted_list[start]:
            answer_index = start
            break

        #Vaatame kas meie element on hulga viimane element
        elif element == sorted_list[end]:
            answer_index = end
            break

        #Vaatame kas meie element on täpselt hulga keskpunktis asuv element (edaspidi midpoint)
        elif element == sorted_list[mid_point]:
            answer_index = mid_point
            break

        #Vaatame kas meie element on väiksem kui hulga midpoint. Kui on siis uue hulga end on midpoint
        elif element < sorted_list[mid_point]:
            end = mid_point
            mid_point = math.floor((end - start) / 2)

        #Vaatame kas meie element on suurem kui hulga midpoint. Kui on siis uue hulga start on midpoint
        elif element > sorted_list[mid_point]:
            start = mid_point
            mid_point = mid_point + math.floor((end - start) / 2)
            
    
    return answer_index


#test_list = [0, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
test_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
print(binary_search(test_list, 2))