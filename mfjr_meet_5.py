#PERULANGAN DAN KONTROL ALUR

#(program 5.1) Perulangan Loop
angka = 1
print(angka)
angka = angka + 1
print(angka)
angka = angka + 1
print(angka)

#for kondisi:
#    aksi

#dengan list data integer/float
angka2 = [0,1,2,3] #ini merupakan list
print(angka2)
for i in angka2:
    print(f"i sekarang -> {i}") #print(f) -> kombinasi text dan variabel
print("Akhir dari program\n")

#dengan range
angka3 = range (3)
for i in angka3:
    print(f"sekarang -> {i}")
print("Akhir dari program\n")

angka4 = range (1,4)
for i in angka4:
    print(f"i sekarang -> {i}")
print("Akhir dari program\n")

#dengan data string
data_str = "Ayo Gowes"

for huruf in data_str:
    print(huruf)
print("Akhir dari program\n")


#(PROGRAM 5.2) PROGRAM WHILE LOOP
#While Loop

#While Kondisi:
#     aksi ini
#     aksi itu

print("===contoh 1===\n")
angka = 10
while angka > 4:
    print("Angjay TIF")
    angka -= 2
print(" ")

print("===contoh 2===")
angka = 0
print(f"angka sekarang -> {angka}")

while angka < 4:
    angka += 2
    #angka = angka + 1
    print(f"angka sekarang -> {angka}")
    print("gwehj TIF sekarang")

print("Hmmm, gw maunya arsitek\n")


#(PROGRAM 5.3) CONTINUE, PASS, AND BREAK

#Pass = berfungsi sebagai dummy, tidak akan dieksekusi
angka = 0

while angka < 5:
    if(angka == 3):
        pass
        #print("Kamu anak bawang")
    angka = angka + 1

#Continue
angka = 0

while angka < 6:
    angka = angka + 2
    if(angka == 3):
        continue
    print(f"angka sekarang -> {angka}")
print("Done")

#(PROGRAM 5.4) Break
angka = 1

while angka < 5:
    print("bolehlah")
    angka = angka + 1
    if(angka == 3):
        break
print("udah lah")


#(PROGRAM 5.5) LATIHAN SOAL PERULANGAN

#Latihan Membuat Segitiga

#1.) Menggunakan for
sisi = 4
count = 1

for i in range(sisi):
    print("*" * count)
    count += 1
print(" ")

#2.) Menggunakan while
sisi = 4
count = 1

while True:
    print("*" * count)
    count += 1

    if count > sisi:
        break


#TUGAS LATIHAN
print("===Program Menampilkan Bilangan Menggunakan Perulangan===\n")
print("1.Buat program yang menampilkan bilangan ganjil dan genap dari 1 sampai 50 menggunakan perulangan!\n")
print("2.Buat program yang menampilkan semua bilangan prima antara 1 sampai 100 menggunakan perulangan!\n")

print("===1.Menampilkan bilangan ganjil & genap (1-50) dengan perulangan===")
for i in range(1,51):
    if i % 2 == 0:
        print(f"{i} (GENAP)")
    else:
        print(f"{i} (GANJIL)")
print("\n")

#Disini saya juga akan mencoba mengelompokkan setiap bilangan (1-50) berdasarkan kategori Ganjil atau Genap
print("===Mengelompokkan bilangan (1-50) dengan kategori ganjil/genap===")
print("Bilangan Ganjil:")
for i in range(1,51):
    if i % 2 != 0:
        print(i, end=" ")

print("\nBilangan Genap:")
for i in range(1,51):
    if i % 2 == 0:
        print(i, end=" ")
print("\n")

print("===2.Menampilkan semua bilangan prima dari (1-100) dengan perulangan===")
print("===Bilangan Prima Dari (1-100)===")
for angka in range(1,101):
    if angka > 1:
        is_prima = True
        for i in range(2,angka):
            if angka % i == 0:
                is_prima = False
                break
        if is_prima:
            print(angka, end=" ")