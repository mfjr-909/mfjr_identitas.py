#LOGICAL, KOMPARASI LOGICAL DAN ELIF

#4.1 OPERASI LOGIKA ATAU BOOLEAN
#not, or, and, xor

#not
print('===NOT===')
a = True
b = not a
print('data a =' ,a)
print('------------- NOT')
print('data b =' ,b)
print('')

#or
print('===OR===')
a = False
b = False
c = a or b
print(a, 'or', b, '=', c)
a = False
b = True
c = a or b
print(a, 'or', b, '=', c)
a = True
b = False
c = a or b
print(a, 'or', b, '=', c)
a = True
b = True
c = a or b
print(a, 'or', b, '=', c)
print(' ')

#and
print('===AND===')
a = False
b = False
c = a and b
print(a, 'and', b, '=', c)
a = False
b = True
c = a and b
print(a, 'and', b, '=', c)
a = True
b = False
c = a and b
print(a, 'and', b, '=', c)
a = True
b = True
c = a and b
print(a, 'and', b, '=', c)
print(' ')

#xor
print('===XOR===')
a = False
b = False
c = a ^ b
print(a, 'xor', b, '=', c)
a = False
b = True
c = a ^ b
print(a, 'xor', b, '=', c)
a = True
b = False
c = a ^ b
print(a, 'xor', b, '=', c)
a = True
b = True
c = a ^ b
print(a, 'xor', b, '=', c)
print(' ')

#LOGIKA DAN KOMPARASI
#Membuat Gabungan Area Rentang Dari Angka

# +++++++3-------10+++++++
inputUser = int(input("Masukkan Angka: "))

# =======3-------
#lebih dari 3
#memeriksa angka kurang dari 3
isLebihDari = inputUser < 3
print("Kurang dari 3 =", isKurangDari)

# +++++++10-------
#kurang dari 10
isLebihDari = inputUser > 10
print("Lebih dari 10 =", isLebihDari)

isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukkan:", isCorrect)

print("=================================")


#IF DAN ELSE STATEMENT
# 1. if nya
# 2. kondisi nya
# 3. aksi nya

#Program if inline
if nama == "RH" : print("Loh Nama nya Singkat")
print("akhir dari program")

#Program if indentation
if nama == "RH":
    print("Kamu Pinter Gokil Juga")
    print("Sana Daftar CPNS")

#Else Statement
if nama == "RH":
    print("Suaramu Kayak Afgan Mash")
else:
    print("Ahh inimah Fals Suaranya")

print("akhir dari program")

#ELIF  ELSE IF STATEMENTT
# if kondisi:
#     aksi true
# elif kondisi:
#     aksi true
# elif kondisi:
#     aksi true
# else:
#     aksi false

nama = input("Whats Yo Name?: ")
if nama == "RH":
    print("Loh Tumben Ga Telat Mash")
elif nama == "Galang":
    print("Loh Sudah Ga Kesetrum Mash")
elif nama == "Jeni":
    print("Inimah MBG Gwehj")
else:
    print("Lau Siapa Coi?")

#LATIHAN SOAL
# 1. Buatlah program yang meminta user memasukkan usia seseorang,
#    lalu kategorikan usia tersebut berdasarkan kriteria berikut:
#     - Anak-anak: 0-12 tahun
#     - Remaja: 13-19 tahun
#     - Dewasa: 20-59 tahun
#     - Lansia: 60 tahun ke atas

#Meminta user input usia seseorang
usia = int(input("Masukkkan usia seseorang: "))

#Kategorikan usia yang dimasukkan menggunakan if, else, dan elif
if usia >= 0 and usia <= 12:
    print("Kategori Usia Anda: Anak-anak")
elif usia >= 13 and usia <= 17:
    print("Kategori Usia Anda: Remaja")
elif usia >= 18 and usia <= 59:
    print("Kategori Usia Anda: Dewasa")
elif usia >= 60 and usia <= 130:
    print("Kategori Usia Anda: Lansia")
elif usia >= -100 and usia <= -1:
    print("Kategori Usia Anda: Belum Lahir/Invalid")
else:
    print("Kategori Usia Anda: Immposible/Invalid")
