"""
Jump Search on algoritm, mis muudab lineaarse otsimise natuke kiiremaks. Jump searchi jaoks peab järjend olema sorteeritud.
Järjendit hakatkase väiksemate alamlõikude kaudu vaatlema. Kas alamlõigu vasak otspunkt on < X ja kas parem otspunkt on > X.
Kui on, siis järelikult asub otsitav selles lõigus ja rakendame edasi lineaarset otsingut, nüüd juba väga palju väiksemal lõigul.

Küsimus 2. Ajalised keerukused worst:
Linear Search   -   O(n)
Jump Search     -   O(sqrt n)
Binary Search   -   O(log n)

Jump Search on parem, kui lineaarne otsing, kuid pole nii hea, kui binaarne otsing.

Küsimus 3.

JUMP VS LINEAAR:

Kui element asub kaugemal kui ühe alamlisti pikkus, on Jump Search juba lineaarist parem, kuna linear peab käima läbi
esimese vahemiku läbi, millest Jump Search üle hüppas.

JUMO VS BINAARNE:

Mida lähemal on element algusele, seda suurem eelis on Jump Searchil, kuna tema läheneb algusest, aga binaarne otsing hakkab
järjendi keskelt lähenema. Kindlasti peab otsitav olema otsitav järjendi esimeses pooles.  


"""
import math
from Task_01 import linear_search

def jumpSearch(X, arr):
    step = math.floor(math.sqrt(len(arr)))
    kordus = math.floor(len(arr) / step)
    i_total = 0
    #stepised sublistid mis mahuvad suuremasse list
    for i in range(kordus):
        sub_list = arr[i*step:(i+1)*step]
        print(sub_list)
        if sub_list[0] <= X and sub_list[-1] >= X:
            i_sub = linear_search(X, sub_list)
            i_total += i_sub
            return i_total
        i_total += step
    #Viimane ots kui ei jagu võrdselt
    sub_list = arr[i_total:]
    print(sub_list)
    i_sub = linear_search(X, sub_list)
    i_total += i_sub
    return i_total


arr = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
print(jumpSearch(30,arr))