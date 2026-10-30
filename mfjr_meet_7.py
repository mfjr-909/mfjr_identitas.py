##LIST
#kumpulan dari beberapa data
print("=== CARA MEMBUAT LIST ===")

#kumpulan data numbers
data_angka = [1, 5, 3, 4]
print(data_angka)

#kumpulan data string
data_string = ["ucup", "RH", "hmz"]
print(data_string)

#kumpulan data boolean
data_boolean = [True, False, True]
print(data_boolean)

#kumpulan campuran data
data_campuran = [1, "mie ayam", 5, "es teh", True]
print(data_campuran)

##CARA ALTERNATIF MEMBUAT LIST
data_range = range(0, 10, 2)  #range(start, stop, step)
print(data_range)
data_list = list(data_range)
print(data_list)

#membuat list dengan for loop, list comprehension
list_for = [i **2 for i in range(0, 10)]
print(list_for)

#membuat list dengan for dan if
list_for_if = [i for i in range(0,10) if i !=5]
print(list_for_if)

list_for_if2 = [i for i in range(0, 10) if i %2 == 0]
print(list_for_if2)

list_for_if3 = [i for i in range(0, 10) if i &2 != 0]
print(list_for_if3)

##MANIPULASI LIST
##OPERASI LIST
print("=== OPERASI LIST ===")

#index 0(-3)  1(-2)  2(-1)
data = ["ucup", "adit", "fadhil"]

#mengambil data dari list
data_0 = data[0]
print(f"data pertama (index 0) = {data_0}")

data_terakhir = data[-1]
print(f"data terakhir adalah = {data_terakhir}")

#mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

##MANIPULASI DATA PADA LIST

#menambahkan item pada list sesuai posisi
print(f"data sebelum ditambah = \n{data}")

#data.insert(posisi, item)
data.insert(1, "asep")
print(f"data sesudah ditambah = \n{data}")

#menambah data di akhir list
data.append("yeni")
print(f"data setelah ditambah lagi = \n{data}")

#menambahkan list dengan list
data_baru = ["luffy", "zoro", "sanji"]
data.extend(data_baru)
print(f"data gabungan = \n{data}")

#merubah data
#kita ubah data 2 menjadi jarwo
data[2] = "jarwo"
print(f"data rubah = \n{data}")

#menghapus data
data.remove("ucup")
print(f"data hapus = \n{data}")

#menghapus data paling belakang
data.pop()
print(f"data hapus akhir = \n{data}")

##OPERASI LIST

#index 0(-3)  1(-2)  2(-1)
data_angka = [1,5,1,4,3,2,4,3,2,3,7,8,9,0]
print(f"data angka = \n{data_angka}")

#count data
jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)

print(f"jumlah angka 4 = {jumlah_data_4}")
print(f"jumlah angka 3 = {jumlah_data_3}")

#ambil posisi data
data = ["rendi", "iqbal", "gana", "khairi"]
print(f"data = {data}")

index_iqbal = data.index("iqbal")
index_gana = data.index("gana")

print(f"index si iqbal = {index_iqbal}")
print(f"index si gana = {index_gana}")

#mengurutkan list
print(f"data angka sebelum sort = \n{data_angka}")
data_angka.sort()
print(f"data angka sort = \n{data_angka}")

print(f"data = {data}")
data.sort()
print(f"data sort = {data}")

#balik listnya
data_angka.reverse()
data.reverse()
print(f"data di reverse \n{data_angka}")
print(f"data di reverse \n{data}")

##NESTED LIST
print("=== NESTED LIST ===")

data_0 = [1,2]
data_1 = [3,4]

data_list_biasa = [1,2,3,4]
print(f"list biasa = {data_list_biasa}")

list_2D = [data_0, data_1, 6,7]
print(f"list 2D = {list_2D}")

#contoh penggunaan
peserta_0 = ["rendi", 25, "laki-laki"]
peserta_1 = ["fadhil", 17, "laki-laki"]
peserta_2 = ["jeni", 20, "wanita"]

list_peserta = [peserta_0, peserta_1, peserta_2]
print(f"peserta = {list_peserta}")

for peserta in list_peserta:
    print(f"Nama\t : {peserta[0]}")
    print(f"Umur\t : {peserta[1]}")
    print(f"Gender\t : {peserta[2]}\n")