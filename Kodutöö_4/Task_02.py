"""
2. Aja- ja Ruumikomplekssuse Analüüs:

Aja komplekssus: Andmete sisestamisel on aja komplekssus O(n), kus n on andmete arv. Andmete otsimisel räsiväärtuse järgi on aja komplekssus O(1), 
kuna me pääseme otse määratud indeksile.

Ruumikomplekssus: Ruumikomplekssus on O(m), kus m on maksimaalne andmeväärtus. Meie räsimassiiv kasutab iga võimaliku andmeväärtuse jaoks ühte kohta.



3. Indeksi Kaardistamise Rakendamine Reaalses Maailmas:

    Indeksi kaardistamine sobib hästi olukordadesse, kus andmed on võimalik kaardistada otse mõne kindla vahemiku või piiranguga indeksiteks. 
    Näiteks:

            Sõnastiku rakendused: Kui sõnastikus on teatud sõnad või mõisted, saab neid kasutada otse indeksitena, 
            muutes kiireks otsimiseks ja juurdepääsuks.

            Kalendri rakendused: Kui päevad on nummerdatud, saab igale päevale omistada otse selle numbri, 
            muutes kiireks päeva leidmise või haldamise.

            Unikaalsete identifikaatorite haldamine: Kui igal elemendil on unikaalne identifikaator (nt kasutajaid, tooteid), 
            saab neid otse kasutada indeksitena, mis lihtsustab kiiret otsimist ja juurdepääsu.
"""

def index_mapping(data_in):
    max_value = max(data_in)
    hash_table = [None] * (max_value + 1)
    for item in data:
        hash_table[item] = item

    return hash_table

data = [4, 2, 8, 1, 3]
hash_table = index_mapping(data)
print(hash_table)
