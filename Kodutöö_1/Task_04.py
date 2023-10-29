"""

4. Binaarne otsingualgoritm
Looge (vabalt valitud) binaarne otsingualgoritm, mis leiab kindla täisarvu sorteeritud täisarvude loendist.

Piirangud:
Teie algoritm peaks tagastama täisarvu indeksi, kui see on leitud, või sõnumi, mis väidab, et täisarvu loendis pole.

Esitamiseks:
Kood binaarse otsingu algoritmi jaoks.
Lühike dokumentatsioon, mis selgitab teie teostust.

"""
import math

def binary_search(sorted_list, element):
    start = 0
    end = len(sorted_list) - 1
    mid_point = round((end - start) / 2)
    answer_index = 0
    
    while True:  
        print(start, mid_point, end)

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
print(binary_search(test_list, 15))

"""
1. Määrame alguse - listi nullis element
2. Määrame lõpu - listi -1. element
3. Määrame keskpunkti - listi keskmine element
4. Vaatame kas meie otsitav väärtus on suurem või väiksem kui keskpunktis
5.1 Kui on väiksem siis uus lõpp on keskpunkt
5.2 Kui on suurem siis uus algus on keskpunkt
6. Kordame eelnevaid punkte uute algus- ja lõpppunktidega, kuni jõuame lahenduseni

LAHENDUS:
a) kui otsitav on == alguspunktiga => vastus olemas
b) kui otsitav on == keskpunktiga => vastus olemas
c) kui otsitav on == lõpppunktiga => vastus olemas



"""
