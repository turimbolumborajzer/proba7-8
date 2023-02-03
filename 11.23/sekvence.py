#           0       1      2      3
osoba = ["Sofija", 20, "plava", True]
print(osoba)

print(osoba[0])
print("Godine:", osoba[1])

automobili = ["Opel", "Citroen", "Mercedes"]
print(automobili[1])
       #012345
kurs = "python"
# print(kurs[0])
# print(kurs[1])
# print(kurs[2])
# print(kurs[3])
# print(kurs[4])
# print(kurs[5])

for x in range(len(kurs)):
    print("Na poziciji:", x, kurs[x])

#len(sekvenca)
# duzina = len(kurs)

ustanova = "IT Academy"
for indeks in range(len(ustanova)):
    print(ustanova[indeks])

print()

primer = "zadatak1"
for x in range(len(primer)):
    print(primer[x])

# korisnicko_ime = "admin"
# uneto_kor_ime = input("Unesite korisnicko ime:")
# if korisnicko_ime == uneto_kor_ime.lower():
#     print("Dobrodosli")
# else:
#     print("Pogresni podaci")




