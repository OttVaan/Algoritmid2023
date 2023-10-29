"""
Ülesanne 5: Stabiilsus ja adaptiivsus sortimisel (1p)
a) Defineeri, mida tähendab, et sortimisalgoritm on "stabiilne." Anna näide stabiilsest sortimisalgoritmist antud loendist.

VASTUS: Kui meil on listis kaks identse väärtusega elementi, siis stabiilne algoritm säilitab nende algse järjekorra peale sorteerimist.

Näide: meil on listis pikkused ja meil on kaks last, kes on sama pikkad nt 150cm. Esimene on Mari ja teine Mati.
Peale stabiilset sorteerimist on ikka veel Mari pikkus enne Matit. Kui algoritm oleks ebastabiilne, siis võivad samade 
väärtuste järjekorrad vahetusse minna.


b) Selgita "adaptiivsuse" kontseptsiooni sortimisel. Millistest eelmainitud sortimisalgoritmidest peetakse adaptiivseks?

VASTUS: Adaptiivus on algoritmi võime "kohaneda" vastavalt sisendile. 

Näide: Insertion sort on adaptiivne, kuna juhul kui list on osaliselt sorteeritud, muutub meie algoritm sellest kiiremaks.


"""