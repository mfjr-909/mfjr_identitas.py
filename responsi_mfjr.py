# #Soal nomor 1
# print("====== SOAL NOMOR 1 =======")
# print("==== GRADE NILAI UJIAN ====")

# nilai = int(input("Masukkan Nilai Ujian (0-100): "))

# if nilai < 0 or nilai > 100:
#     print("Nilai Tidak Valid, Masukkan Nilai Antara (0-100)!")
# elif nilai >= 90:
#     print("Grade A")
#     print("Sangat Memuaskan")
# elif nilai >= 80:
#     print("Grade B")
#     print("Memuaskan")
# elif nilai >= 70:
#     print("Grade C")
#     print("Cukup")
# elif nilai >= 60:
#     print("Grade D")
#     print("Kurang")
# else:
#     print("Grade E")
#     print("Tidak Lulus")



#Soal nomor 2
print("======= SOAL NOMOR 2 ======")
print("=== TARIF TIKET BIOSKOP ===")

harga_normal = 50000
print("==== SELF SERVICE TIKCET MACHINE CINEMAX XXI ====")
nama = input("Nama Pembeli: ")
jumlah = int(input("Jumlah Tiket: "))
print(" ")
print("=== Input Data Pengunjung ===")

subtotal = 0
for i in range(1, jumlah + 1):
    usia = int(input("Usia Pengunjung " + str(i) + ": "))
    if usia < 5:
        tarif = 0
        kategori = "Balita"
    elif usia <= 12:
        tarif = harga_normal * 50 // 100
        kategori = "Anak-anak"
    elif usia <= 59:
        tarif = harga_normal
        kategori = "Dewasa"
    else:
        tarif = harga_normal * 70 // 100
        kategori = "Lansia"
    print(" -> Tarif: Rp", format(tarif, ","), "(" + kategori + ")")
    subtotal = subtotal + tarif
#PENGHITUNGAN DISKON ROMBONGAN
if jumlah >= 5:
    diskon = subtotal * 10 // 100
else:
    diskon = 0

total_bayar = subtotal - diskon
print(" ")
print("-" * 40)
print("===== STRUK PEMBAYARAN =====")
print("Pembeli                :", nama)
print("Total Jumlah Tiket     :", jumlah, "orang")
print("Subtotal Tiket         : Rp", format(subtotal, ","))
print("Diskon Rombongan(10%)  : Rp", format(diskon, ","))
print("-" * 40)
print("Total Bayar            : Rp", format(total_bayar, ","))
print("=" * 40)