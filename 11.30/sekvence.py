brojevi = [9, 1, 3, 2, 5, 8, 7]
brojevi.sort()
brojevi.reverse()
print(brojevi)

brojevi = [9, 1, 3, 2, 5, 8, 7]

# 9   1
#x   y
#privremeno

#od najmanjeg do najveceg:
while True:
    izvrsena_zamena = False
    for i in range(1, len(brojevi)):
        if brojevi[i] < brojevi[i-1]: #1<9
            privremena = brojevi[i]  #1
            brojevi[i]= brojevi[i-1] #9
            brojevi[i-1] = privremena #1
            izvrsena_zamena = True
    if izvrsena_zamena == False:
        break
print(brojevi)


# 9   1
#x   y
#privremeno

proizvodi = ["Telefon", "TV", "Laptop"]
cene      = [100,    200,     300]

# for i in range(len(proizvodi)):
#     print(proizvodi[i], cene[i])

automobili = ["Audi", "BMW", "Yugo", "Citroen", "Kia", "Peugeout"]

# for i in range(len(automobili)):
#         if i==3:
#             print("Aleksandra vozi", automobili[i])

stvari = [
        ["iphone 11", "samsung 10", "xiaomi 12"],
        ["dell", "acer", "lg"],
        ["ipad", "samsung galaxy tab", "xiaomi tablet"]

        ]
#stvari[0][1]   [i][j]

telefoni = ["iphone 11", "samsung 10", "xiaomi 12"]
laptopovi = ["dell", "acer", "lg"]
tableti = ["ipad", "samsung galaxy tab", "xiaomi tablet"]

# print(stvari[0][0])
# print(stvari[1][1])

#stvari = [telefoni, laptopovi, tableti]

# for kategorija in stvari:
#     for stavka in kategorija:
#         print(stavka)
#stampa sve proizvode odjednom

# for telefon in telefoni:
#     print(telefon)

for i in range(len(stvari)):
    print(stvari[i]) #tri liste odvojeno
    for j in range(len(stvari[i])):
        print(stvari[i][j])

hrana = [
            ["cokolada", "bombone", "palacinke"],
            ["sarma", "musaka", "kiseli kupus"],
            ["pecena paprika", "ajvar", "sopska"]
        
        ]

for kategorija in hrana:
    for jelo in kategorija:
        print("Naziv:", jelo)
        if jelo == "sopska":
            print("Sopska nadjena!", jelo)
ime = "Sofija"

# poruka = "Cao" + ime + "!!!"
poruka = f"Cao {ime} !!!"
print(poruka)

# a=10
# b=15

# sabiranje = f"Saburanje brojeva {a} i {b} je {a+b}"

# print("Sabiranje brojeva", a, "i", b, "je", a+b)

biblioteka= [           ]


while True:
    print("Odaberi komandu: 1- unos, 2- prikaz, 3- brisanje, > 3 izlaz")
    komanda = int(input("Unesite komandu: "))
    if komanda == 1:
            #unos knjige, preuzmi podatke
            naslov= input("Unesite naslov: ")
            autor = input("Unesite autora: ")
            isbn= int(input("Unesite isbn: "))
            biblioteka.append([naslov, autor, isbn])
            print("Dodata knjiga")
    if komanda == 2:
        for knjiga in biblioteka:
            for detalj in knjiga:
                print(detalj)
    if komanda == 3:
        kljucna_rec = input("Unesite naziv kjige koje zelite da obrisete: ")
        for knjiga in biblioteka:
            #proveravam detalje KNJIGE
            for detalj in knjiga:
                if detalj == kljucna_rec:
                    biblioteka.remove(knjiga)
                    print("Knjiga je obrisana")



#pop i del po indeksu, remove po vrednosti
