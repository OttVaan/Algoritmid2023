"""

3. Rekursiivne Fibonacci funktsioon
Kirjutage funktsioon, mis, olles antud täisarv n, tagastab n-nda Fibonacci numbri, kasutades rekursiivset meetodit.

Piirangud:
Eeldage, et n on mittenegatiivne täisarv.

Esitamiseks:
Kood rekursiivse Fibonacci funktsiooni jaoks.
Väike dokumentatsioon, mis selgitab teie rekursiivset lähenemist.

"""

def fibonacci_generator(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_generator(n - 1) + fibonacci_generator(n - 2)

print(fibonacci_generator(10))

"""

1) Alustame koodiga sellest, et paneme funktsiooni, mitmendat arvu me soovime
2) Vaatame, kas n == 1 või 0
3) Kui ei ole, siis me teame, et n-is arv on kahe eelmise ehk n-1 ja n-2 summa. Vaatame rekursiooniga, mis on n-1 ja n-2 väärtused.
4) Kui liidetavate järjekorranumber ei ole 0 või 1, siis vaatame millised liidetavad moodustasid otsitava n-1.
5) Teeme punkti 4 nii kaua, kuni jõuame kahe esimese arvuni ja hakkame neid mööda puud tagasi üles tagastama.
6) Jõuame tagasi algselt otsitava liikmeni ja tagastame selle.

"""