import random

kurs = "Python Fundamentals"
print (kurs)

a = 10
b = 5
print(a+b)
rezultat_sabiranja = a + b
print(rezultat_sabiranja)
print("Oduzimanje:", a - b)
print("Mnozenje:", a * b)
print("Deljenje:", int(a / b))
print("Celobrojno deljenje:", a//b)
print(10//3)
print("Stepenovanje:", a**b)
print("Ostatak:", a%b)
print("Negacija je:", -a)
godine = 25
#godine + 1
print(godine)
godine=godine + 1
print(godine)
godine +=1
print(godine)
godine-=5
print(godine)
godine//=3
print(godine)

# broj1=15
# broj2=20
# print("Zbir:", broj1 + broj2)

# broj1=int(input("Unesite prvi broj: "))
# print(broj1)

# broj2=int(input("Unesite drugi broj: "))
# print(broj2)

# print("Rezultat je:", broj1 + broj2)

stara_kilaza = 80
nova_kilaza = 99

#print(stara_kilaza > nova_kilaza)

#rint(nova_kilaza > stara_kilaza)

#print(nova_kilaza == stara_kilaza)

# print(nova_kilaza != 100)

# print(nova_kilaza == 100)

username = "test"
password = "abc123"

# print(username == "test")
# print(password == "ABC123")

#unos = input()
#print(unos == password)

# godine = 20
# print(godine >= 16)

#vezba7
# korisnik = int(input("Unesite broj:"))
# racunar = random.randint(1, 10)
# print("Korisnik:", korisnik)
# print("Racunar:", racunar)
# print("Pogodak!", korisnik == racunar)

provera_imena = True #ime == sacuvano_ime
provera_sifre = False #sifra == sacuvana_sifra
print(provera_imena or provera_sifre)

lepo_vreme = True
print(not lepo_vreme)
a = [1,2,3]
b = [2,3,4]
a = b
print(a is b)

# x = 10
# y = 15
# print (x is y)


kurs = input("Unesite kurs:")
generacija = int(input("Generacija:"))
odobreno = kurs = "python" and generacija == 2022
print (odobreno)


