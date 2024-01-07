# Topelt Räsimise Eelised:
# 
# Konfliktide Vähendamine: 
#     Topelt räsimine võimaldab vähendada konfliktide arvu võrreldes ühekordse räsimisega, sest teine räsimisfunktsioon võib 
#     anda erineva indeksi ka samadele võtmetele.
# 
# Laiaulatuslik Räsimine: 
#     Topelt räsimise abil saab saavutada laiaulatusliku räsimise, kus mitu räsimisfunktsiooni hajutavad võtmeid erinevalt.
# 
# Aja- ja Ruumikomplekssus:
#     Aja komplekssus: Topelt räsimise puhul on aja komplekssus sageli O(1), kuid see võib suureneda konfliktide korral. 
#     Kui konflikte on palju, võib otsing kuluda kauem aega.
# 
# 
# Ruumikomplekssus: Ruumikomplekssus on O(n), kus n on räsimistabeli suurus.
# 
# 
# Efektiivne Stsenaarium:
# 
# Topelt räsimine on eriti efektiivne, kui räsimistabeli suurus on piiratud ja konfliktide arv on mõõdukas. 
# See võimaldab paremat hajutamist ja suuremat tõenäosust leida vaba koht. Efektiivsust suurendab ka hea räsimisfunktsiooni valik.


def hash_function1(key, size):
    return key % size

def hash_function2(key, size):
    return 1 + (key % (size - 1))

def insert(table, key, value, size):
    index = hash_function1(key, size)

    if table[index] is None:
        table[index] = (key, value)
    else:
        step = hash_function2(key, size)
        current_index = (index + step) % size

        while table[current_index] is not None:
            current_index = (current_index + step) % size

        table[current_index] = (key, value)

def search(table, key, size):
    index = hash_function1(key, size)
    step = hash_function2(key, size)
    current_index = index

    while table[current_index] is not None and table[current_index][0] != key:
        current_index = (current_index + step) % size

    if table[current_index] is not None and table[current_index][0] == key:
        return table[current_index][1]
    else:
        return None

# Näide kasutamisest
table_size = 10
hash_table = [None] * table_size

insert(hash_table, 5, "A", table_size)
insert(hash_table, 15, "B", table_size)
insert(hash_table, 25, "C", table_size)

print(search(hash_table, 5, table_size))  # Väljund: A
print(search(hash_table, 15, table_size)) # Väljund: B
print(search(hash_table, 25, table_size)) # Väljund: C
