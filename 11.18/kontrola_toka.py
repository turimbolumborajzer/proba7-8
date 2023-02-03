x = 10
if x > 0:
    print("x je pozitivan")

vozilo_u_pokretu = True
brzina = 60
if vozilo_u_pokretu:
    print("Vozilo se krece")
    if brzina > 50:
        print("Prekoracili ste brzinu")
    if brzina <= 50:
        print("Brzina je OK")
if vozilo_u_pokretu == False:
    print("Vozilo se ne krece")
# 1 - prikaz; 2 - kupovina; 3 - izlaz
proizvod = "duks"
cena = 3000

# komanda = int(input("Unesite komandu: "))


# if komanda == 1:
#     print ("Prikazi proizvode")
#     print("Proizvod:", proizvod, "Cena:", cena)
# if komanda == 2:
#     print("Kupovina")
#     stanje = int(input("Unesite stanje na racunu: "))
#     if stanje >= cena:
#         print("Uspesna kupovina!")
#     else:
#         print("Nemate dovoljno novca")

# if komanda == 3:
#     print("Izlaz")

broj = 0
if broj > 0:
    print("Broj je veci od 0.")
else:
    print("Broj je nula ili manji od nule.")
if broj == 0:
    pass

devojka1 = "marija"
devojka2 = "sofija"

marija = False
sofija= False
ksenija= False
devojka_na_dejtu= ""

if marija:
    devojka_na_dejtu = "Marija"
elif sofija:
    devojka_na_dejtu = "Sofija"
elif ksenija:
    devojka_na_dejtu = "Ksenija"
else:
    devojka_na_dejtu = "nijedna"
print("Izlazi sa mnom:", devojka_na_dejtu)

automobil_polovan= False
godiste = 2021
boja = "crna"

if (automobil_polovan or godiste > 2017) and boja == "crna":
    print("Kupujem")

if automobil_polovan:
    print("Automobil je polovan.")

pol = "zenski"
poruka=""
# if pol == "muski":
#     print("Dobar dan, gospodine")
# else:
#     print("Dobar dan, gospodjo")

poruka = "Dobar dan, gospodine" if pol=="muski" else "Dobar dan, gospodjo"
print(poruka)
