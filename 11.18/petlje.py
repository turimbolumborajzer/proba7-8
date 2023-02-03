pozicija_automobila = 0
pozicija_cilja = 10

pozicija_automobila += 2
print(pozicija_automobila == pozicija_cilja)

for ime in ["marko", "milos", "marija", "ana", "sofija"]:
    print("Hello", ime)

print("Prva sledeca linija...")

# for broj in [1, 2, 3, 4, 5]:
#     print("Ovo je moj broj:", broj)


# for broj in range(1, 21):
#     print(broj)


# for broj in range(1, 21, 2):
#     print(broj)

for broj in range(100, 0, -1):
    print(broj)

pozicija_automobila = 0
pozicija_cilja = 10

for kretanje in range(5):
    pozicija_automobila += 2
    print(pozicija_automobila == pozicija_cilja)

startDate=2010
endDate= 2016
for dozvoljene_godine in range(startDate, endDate):
    print(dozvoljene_godine)

for zvezda in range(100):
    print("*", end="")

print()

print("1\t2\t3")
print("************************")
for brojac in range(1, 6):
    print(brojac * 1, end="\t")
    print(brojac * 2, end="\t")
    print(brojac * 3)

broj = 1.9545
print("%.2f" % broj)

# picka = int(input("Unesite broj: "))
# for brojac in range(1, picka + 1):
#     print(brojac * 5)

for x in range(5):
    for y in range(3):
        print("Ovo je X:", x, "Ovo je Y:", y)


for x in range(6):
    for y in range(3):
        print("#", end= " ")
    print()

print("sipuga")

for x in range(5):
    for y in range(4):
        if x==y:
            print("*", end= " ")
        else:
            print("#", end=" ")
    print()

# for x in range(5):
#     for y in range(4):
#         print("*" if x==y else "#", end=" ")
#     print()

for x in range(10):
    for y in range(10):
        if x==0 or x==9 or y==0 or y==9:
            print("#", end=" ")
        else:
            print(" ", end=" ")
        
    print()

# baterija = 90
# while baterija > 0:
#     print("Mozes koristiti telefon.")
#     baterija -= 10

# print("Baterija je prazna")

import random
baterija = 90
while baterija > 0:
    print("Mozes koristiti telefon.", baterija, "%")
    baterija -= random.randint(5,20)

print("Baterija je prazna")

for broj in range(11):
    if broj ==5:
        break
    print(broj)

#sve osim broja 2

for broj in range(11):
    if broj == 2:
        continue
    print(broj)
