"""
Ternary Search on otsingualgoritm, mida saab rakendada sorteeritud järjendil. Idee on jagada järjend kolmeks võrdseks osaks.
Tekitame kaks otspunkti (nimetame neid lippudeks) esimene lipp läheb 1/3 piirile ja teine 2/3 piirile.

1)Kui üks lippudest on võrdne otsitavaga, siis on vastus käes.

2)Kui otsitav on kahe lipu vahel, hakkame lippe indeksi kaupa üksteisele lähemale tõstma, kuni on tingimus 1.

3)Kui otsitav on lippude vahelt väljas, siis vaatame kummal pool ja hakkame seda lippu indeksi kaupa järjendi otsa suunas
iigutama, kuni on tingimus 1:

Küsimused 2 ja 3. Ternary Search'i ja binaarotsingu ajalinekeerukus
Teoreetiline analüüs:
WORST CASE TIME COMPLEXITY:
Ternary Search      -   O(log3 n)
Binary Search       -   O(log n)

Kuna Ternary Search on optimiseeritud lineaarne otsing ei ole ta konkureeriv binaarse otsinuga. Ainsad võimalused, kus Ternary oleks
kiirem oleks: otsitav ongi kas 1/3 või 2/3 peal või kohe nende lähedal. Kui element satub järjendi keskele või äärtesse, siis on suur 
eelis jälle binaarsel otsingul. Lisaks, Ternary Search'ile soodsad piirkonnad hääbuvad pikkade järjendite puhul väga kiiresti ja 
binaarne otsing on suurte andmete puhul ikkagi domineerivam. 
"""

import math


def ternarySearch(X, arr):
    left = math.floor(len(arr) / 3)
    right = math.floor(len(arr)/ 3 * 2)
    

    while True:
        print(left, right)
        if X == arr[left]:
            return left
        elif X == arr[right]:
            return right
        elif arr[left] < X < arr[right]:
            left += 1
            right += 1
        elif arr[left] > X:
            left -= 1
        else:
            right += 1


arr = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
print(ternarySearch(28,arr))