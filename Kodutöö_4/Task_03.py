"""
2. Efektiivsuse Võrdlus:

Ajaline komplekssus:
Separate Chaining:          O(1) keskmiselt (kui ahelad on lühikesed).
Open Addressing:            Sõltub kasutatavast meetodist (nt lineaarne proovimine, kvadratuurproovimine), kuid võib olla kuni O(n), kus n on räsitabeli suurus.

Ruumiline komplekssus:
Separate Chaining:          O(n + m), kus n on räsitabeli suurus ja m on kokkupõrgete arv.
Open Addressing:            O(n), kus n on räsitabeli suurus.


3. Plusse ja Miinuseid Separate Chaining'us:

Plussid:
Lihtsus:                    Separate Chaining on lihtne rakendada.
Efektiivsus:                Kui kokkupõrked on haruldased, on otsingud ja lisamised kiired.
Hea jaotus:                 Ei sõltu otseselt räsi kvaliteedist, kuna igal räsitabeli kohal on oma ahel.

Miinused:
Mälu kasutus:               Iga ahel kasutab täiendavat mälu, mis võib suurendada üldist mälu kasutust.
Efektiivsuse langus:        Kui ahelad muutuvad liiga pikaks, võib efektiivsus langeda, sest tuleb läbi käia kogu ahel.

"""

def index_mapping(data_in):
    #Vaatame kui pikk peab olema meie räsitabel
    hash_len = 0
    for element in data_in:
        ele_str = str(element)
        ele_sum = 0
        for arv in ele_str:
            ele_sum += int(arv)
        if ele_sum > hash_len:
            hash_len = ele_sum
    hash_len += 1

    #Loome räsitabeli
    hash_table = [[]] * hash_len
    

    #Lisame elemendid räsitabelisse
    for item in data:
        ele_str = str(item)
        ele_sum = 0
        for arv in ele_str:
            ele_sum += int(arv)
        if len(hash_table[ele_sum]) == 0:
            hash_table[ele_sum] = [item]
        else:
            linked_list = hash_table[ele_sum]
            linked_list.append(item)
            hash_table[ele_sum] = linked_list
    
    return hash_table

def search_from_hash(search, hash_tab):
    ele_str = str(search)
    ele_sum = 0
    for arv in ele_str:
        ele_sum += int(arv)
        
    index_1 = ele_sum

    for i in range(len(hash_tab[ele_sum])):
        if search == hash_tab[ele_sum][i]:
            index_2 = i
            return (index_1, index_2)

    
if __name__ == "__main__":
    data = [6, 24, 56, 211, 888, 33]
    db = index_mapping(data)
    print(db)
    print(search_from_hash(888, db))