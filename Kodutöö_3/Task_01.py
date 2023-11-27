"""
Küsimus 2:

Ruumilinekompleksus: 
Kuna me ei jäta midagi meelde vaid ainult võrdleme, siis ruumilinekompleksus on -> O = 1

Ajalinekompleksus:
Worst case: Otsitav element on viimane ehk peame läbi käima kogu listi ühe korra -> O = n 
Best case: Otsitav element on esimene ehk lõpetame töö peale esimest võrdlust -> O = 1
Average case: Otsitav element on kustahes järjendis -> O = n 



Küsimus 3:

Miski ei takista meid kasutamast antud otsingut igal pool. Mina leian, et pigem on küsimus selles, kus oleks seda kasulik kasutada.
Lihtsamate ja väiksemate otsingute puhul nagu see test siin oleks see mõistlik, sest meetodi implementeerimine on lihtsam, 
kui keerulistematel algoritmidel.
"""

def linear_search(search, arr):
    for i in range(len(arr)):

        if arr[i] == search:
            print(f"Element is at position {i} (starting from 0)")
            return i

    print("no such element in list")
if __name__ == "__main__":
    test_list = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
    linear_search(20,test_list)
