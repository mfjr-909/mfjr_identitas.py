#OPERASI ARITMATIKA
a = 30
b = 5

#Operator Penjumlahan(+)
hasil = a + b
print(a, '+', b, '=', hasil)

#Operator Pengurangan(-)
hasil = a - b
print(a, '-', b, '=', hasil)

#Operator Perkalian(*)
hasil = a * b
print(a, '*', b, '=', hasil)

#Operator Pembagian(/)
hasil = a / b
print(a, '/', b, '=', hasil)

#Operator Eksponen(Pangkat)(**)
hasil = a ** b
print(a, '**', b, '=', hasil)

#Operator Modulus(%)
hasil = a % b
print(a, '%', b, '=', hasil)

#Operator Floor Division(//)
hasil = a / b
print(a, '//', b, '=', hasil)


#OPERASI KOMPARASI
x = 25
y = 3
#Lebih Dari(>)
print("======LEBIH DARI (>)")
hasil = x > 10
print(x, '>', 10, '=', hasil)
hasil = y > 5
print(y, '>', 5, '=', hasil)
print(" ")

#Kurang Dari(<)
print("=====KURANG DARI (<)")
hasil = x < 10
print(x, '<', 10, '=', hasil)
hasil = y < 5
print(y, '<', 5, '=', hasil)
print(" ")

#Lebih Dari Sama Dengan(>=)
print("=====LEBIH DARI SAMA DENGAN (>=)")
hasil = x >= 10
print(x, '>=', 10, '=', hasil)
hasil = y >= 5
print(y, '>=', 5, '=', hasil)
print(" ")

#Kurang Dari Sama Dengan(<=)
print("=====KURANG DARI SAMA DENGAN (<=)")
hasil = x <= 10
print(x, '<=', 10, '=', hasil)
hasil = y <= 5
print(y, '<=', 5, '=', hasil)
print(" ")

#Sama Dengan(==)
print("=====SAMA DENGAN (==)")
hasil = x == 10
print(x, '==', 10, '=', hasil)
hasil = y == 5
print(y, '==', 5, '=', hasil)
print(" ")

#Tidak Sama Dengan(!=)
print("=====TIDAK SAMA DENGAN (!=)")
hasil = x != 10
print(x, '!=', 10, '=', hasil)
hasil = y != 5
print(y, '!=', 5, '=', hasil)
print(" ")

#Operator IS dan IS NOT (Komparasi objek identify bukan literal identify)
#Is
d = 8
f = 20
hasil = d is f
print("d is f =", hasil)

#Is Not
hasil = d is not f
print("d is not f =", hasil)


#LATIHAN KONVERSI SATUAN SUHU
#PROGRAM KONVERSI SATUAN SUHU CELCIUS KE SATUAN LAIN

print("===PROGRAM KONVERSI SATUAN CELCIUS===")
celcius = float(input("Masukkan suhu dalam celcius: "))
print("suhu adalah", 35, "Celcius")

#Konversi Ke Reamur
reamur = (4/5) * 35
print("Suhu dalam satuan Reamur", reamur, "Reamur")

#Konversi Ke Fahrenheit
fahrenheit = ((9/5) * 35) + 32
print("Suhu dalam satuan Fahrenheit", fahrenheit, "Fahrenheit")

#Konversi Ke Kelvin
kelvin = 35 + 237
print("Suhu dalam satuan Kelvin", kelvin, "Kelvin")