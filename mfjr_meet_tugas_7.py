##LATIHAN SOAL
print("==== LATIHAN SOAL ====")

# 1.) Diberikan list berikut:
#     kendaraan = ["Motor", "Mobil", "Sepeda", "Bus"]
#     a. Tambahkan "Truk" di akhir list
#     b. Sisipkan "Becak" pada indeks ke-1
#     c. Hapus data yang berada di paling belakang dari list tersebut
#     d. Ubah elemen "Sepeda" menjadi "Skuter"
#     e. Tampilkan informasi jumlah total data dari list tersebut

kendaraan = ["Motor", "Mobil", "Sepeda", "Bus"]

#1.a) Tambahkan "Truk" pada akhir list
print("1.a) Tambahkan elemen (Truk) pada akhir list!")
print(F"kendaraan sebelum ditambahkan = \n {kendaraan}")
kendaraan.append("Truk")
print(f"kendaraan setelah penambahan = \n{kendaraan}\n")

#1.b) Sisipkan "Becak" pada indeks ke-1
print("1.b) Sisipkan elemen (Becak) pada indeks ke-1!")
print(f"kendaraan sebelum penyisipan = \n{kendaraan}")
kendaraan.insert(1, "Becak")
print(f"kendaraan setelah penyisipan = \n{kendaraan}\n")

#1.c) Hapus data yang berada di paling belakang list
print("1.c) Hapus data yang berada di paling belakang list!")
print(f"kendaraan sebelum penghapusan = \n{kendaraan}")
kendaraan.pop()
print(f"kendaraan setelah penghapusan = \n{kendaraan}\n")

#1.d) Ubah elemen "Sepeda" menjadi "Skuter"
print("1.d) Ubah elemen (Sepeda) menjadi (Skuter)!")
print(f"kendaraan sebelum pengubahan = \n{kendaraan}")
kendaraan[3] = "Skuter"
print(f"kendaraan setelah pengubahan = \n{kendaraan}\n")

#1.e) Tampilkan informasi jumlah total data dari list tersebut
print("1.e) Tampilkan informasi jumlah total data dari list tersebut!")
jumlah_data = len(kendaraan)
print(f"jumlah data = {jumlah_data}\n\n")


# 2.) Diberikan list berikut:
#     angka = [75, 80, 90, 75, 85, 100, 65]
#     a. Cari tahu di indeks ke berapa skor 100 berada
#     b. Hitung ada berapa banyak siswa yang mendapat skor 75
#     c. Urutkan list skor_ujian tersebut dari nilai terkecil hingga terbesar
#     d. Balikkan urutan list yang sudah diurutkan tersebut sehingga menjadi dari terbesar hingga terkecil

angka = [75, 80, 90, 75, 85, 100, 65]

#2.a) Cari tahu di indeks ke berapa skor 100 berada!
print("2.a) Cari tahu di indeks ke berapa skor 100 berada!")
print(f"angka = {angka}")
index_100 = angka.index(100)
print(f"index skor 100 = {index_100}\n")

#2.b) Hitung ada berapa banyak siswa yang mendapat skor 75!
print("2.b) Hitung ada berapa banyak siswa yang mendapat skor 75!")
print(f"angka skor = {angka}")
jumlah_skor_75 = angka.count(75)
print(f"Jumlah siswa yang mendapat skor 75 = {jumlah_skor_75}\n")

#2.c) Urutkan list skor_ujian tersebut dari nilai terkecil hingga terbesar!
print("2.c) Urutkan list skor_ujian tersebut dari nilai terkecil hingga terbesar!")
print(f"data angka sebelum sort = \n{angka}")
angka.sort()
print(f"data angka setelah sort = \n{angka}\n")

#3.d) Balikkan urutan list yang sudah diurutkan tersebut sehingga menjadi dari terbesar hingga terkecil
print("3.d) Balikkan urutan list yang sudah diurutkan tersebut sehingga menjadi dari terbesar hingga terkecil")
print(f"data angka sebelum di reverse = \n{angka}")
angka.reverse()
print(f"data angka setelah di reverse = \n{angka}\n\n")


# 3.) menu_utama = ["Nasi Goreng", "Mie Ayam"]
#     menu_tambahan = ["Kerupuk", "Es Teh"]
#     Gabungkan menu_tambahan ke dalam menu_utama menggunakan fungsi, kemudian tampilkan hasil dari data gabungan tersebut!
    
menu_utama = ["Nasi Goreng", "Mie Ayam"]
menu_tambahan = ["Kerupuk", "Es Teh"]

print("3.) Gabungkan menu_tambahan ke dalam menu_utama menggunakan fungsi, kemudian tampilkan hasil dari data gabungan tersebut!")
print(f"menu sebelum penambahan = {menu_utama}")
menu_utama.extend(menu_tambahan)
print(f"menu setelah penambahan = {menu_utama}\n\n")


# 4.) Diberikan data nested list berupa informasi nama barang dan harganya:
#     data_barang = [["Buku", 5000], ["Pensil", 2000], ["Penggaris", 3000]]
#     a. Tampilkan harga dari "Pensil" (yaitu 2000) dengan memanggil indeks baris dan kolom yang spesifik dari list tersebut.
#     b. Gunakan perulangan untuk membaca data satu per satu, lalu tampilkan output dengan format:
#        Nama: [nama barang]
#        Harga: [harga]
#        untuk setiap elemen di dalamnya.  

data_barang = [["Buku", 5000], ["Pensil", 2000], ["Penggaris", 3000]]

#4.a) Tampilkan harga dari "Pensil" (yaitu 2000) dengan memanggil indeks baris dan kolom yang spesifik dari list tersebut.
print("4.a) Tampilkan harga dari (Pensil) (yaitu 2000) dengan memanggil indeks baris dan kolom yang spesifik dari list tersebut.")
print(f"data barang = {data_barang}")
print(f"data barang(Pensil) = {data_barang[1][1]}\n")

#4.b) Gunakan perulangan untuk membaca data satu per satu, lalu tampilkan output dengan format:
#     Nama: [nama barang]
#     Harga: [harga]
#     untuk setiap elemen di dalamnya.
print("4.b) Gunakan perulangan untuk membaca data satu per satu, lalu tampilkan output dengan format: Nama: [nama barang], Harga: [harga], untuk setiap elemen di dalamnya.")
print(f"data barang = {data_barang}")
for item in data_barang:
    print(f"Nama\t : {item[0]}")
    print(f"Harga\t : {item[1]}\n")