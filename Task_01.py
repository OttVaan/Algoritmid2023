"""

1. Raamatute järjestamise algoritm
Ülesanne on luua selge ja lühike kirjalik algoritm, mis kirjeldab raamatute riiulil korraldamise samme nende kõrguse põhjal.

Piirangud:
Eeldage, et saate raamatu kõrgust vaadates kindlaks määrata. Arvestage, et riiulil on fikseeritud pikkus ja see mahutab kõik raamatud.

Esitamiseks:
Kirjalik algoritm pseudo-koodis või struktureeritud eesti keeles. Joonis algoritmi tööpõhimttest.

NB! Kasutan koodi kirjutamisel inglise keelt, kood ei ole internetist kopeeritud!
"""

def sort_highest_lowest(books):
    #Loome tühja listi, kuhu hakkame sorteerimist salvestama
    start_list = books
    result_list = []

    #Alguses on kõrgeim raamat kõige esimene, mida me vaatame
    for i in range(len(books)):
        tallest = start_list[0]
        #Võrdleme kõikide raamatutega, mida me ei ole veel sorteerinud ja leiame neist kõrgeima
        for j in range(len(start_list)):
            if start_list[j] > tallest:
                tallest = start_list[j]
        #Eemaldame raamatu sorteerimata raamatute listist ja lisame sorteeritud raamatute listi
        start_list.remove(tallest)
        result_list.append(tallest)
    
    return result_list


raamatud = [7, 4, 6, 2, 1, 11, 8]
test_array = [48, 7, 90, 21, 84, 19, 61, 98, 76, 2, 17, 95, 33, 60, 37, 43, 82, 70, 56, 15]
kasper_test = [7, 38, 12, 77, 62, 65]
print(sort_highest_lowest(kasper_test))