osoba = ["Sofija", 25, "plava", False]

for indeks in range(len(osoba)):
    print(osoba[indeks])

for osobina in osoba:
    print(osobina)

voce_i_povrce = ["jabuka", "beli luk", "crni luk", "banana", "mandarina", "lubenica", "krastavac"]
for stavka in voce_i_povrce:
    print(stavka)

for i in range(len(voce_i_povrce)):
    print(voce_i_povrce[i])

for indeks, vrednost, in enumerate(voce_i_povrce):
    print("Indeks:", indeks, "Stavka:", vrednost)

automobili = ["Citroen", "BMW", "Kia", "Yugo"]

#pozicija: 0 Auto: citroen

for pozicija, auto in enumerate(automobili):
    if pozicija == 1:    #if auto == "Opel"
        print("Kupujem")
        break
    print("Pozicija:", pozicija, "Auto:", auto)

    for pozicija, auto in enumerate(automobili):
        if len(auto) == 3:
            print(auto)

automobili.append("Mercedes")
automobili[2]= "Opel Corsa"
print(automobili)

del automobili[3]
print(automobili)

automobili.remove("BMW")
print(automobili)

automobili.pop(0)
print(automobili)

broj_opela=0
for indeks in range(len(automobili)):
    if automobili[indeks] == "Opel":
        print("Evo ga opel")
        broj_opela +=1

print("Imam", broj_opela, "na placu")

# automobili.clear()
print(automobili)

prazan_plac = []

automobili_akcija = []

for i in range(len(automobili)):
    if i == 1 or i == 2 or i ==3:
        automobili_akcija.append(automobili[i])

print(automobili_akcija)

# automobili_akcija = automobili[1:4]
# print automobili_akcija




