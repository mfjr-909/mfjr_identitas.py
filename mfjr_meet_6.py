#IF BERSARANG(NESTED IF) DAN PERULANGAN BERSARANG(NESTED LOOPING)

#PROGRAM 6.1
#NESTED IF
print("====NESTED IF====")
status_akun = "aktif"
saldo = 7000000
nominal_tarik = 500000

if status_akun == "aktif":
    if nominal_tarik <= saldo:
        if nominal_tarik >= 500000:
            saldoSetelahtraik = saldo - nominal_tarik
            print(f"Transaksi Berhasil: RP.{nominal_tarik:,} ")
            print(f"Sisa Saldo: Rp.{saldoSetelahtraik:,} ")
        else:
            print("Transaksi Minimal 500000")
    else:
        print("Saldo Tidak Mencukupi")
else:
    print("Akun Terblokir")

#PROGRAM 6.2
#NESTED WHILE
#CONTOH 1
print("====NESTED WHILE====")
i = 1
while i <= 2:
    j = 2
    while j <= 3:
        print("Teknik TIF")
        j += 1
    print("\n")
    i += 1

#CONTOH 2
i = 1
n = 1
while i <= 2:
    j = 1
    while j <= 3:
        print(n)
        n = n + 2
        j += 1
    i += 1
print(" ")

#PROGRAM 6.3
#NESTED FOR
print("====NESTED FOR====")
for i in range(1, 3):
    for j in range(1, 11):
        print(f"[{i},{j}]", end=" ")
    print(" ")
print(" ")

#PROGRAM 6.4
#FOR IN A WHILE
print("====FOR IN A WHILE====")
sesi = 1
while sesi <= 3:
    print(f"Sesi ke-(sesi):")
    for antrean in range(1, 3):
        print(f"Pasien Nomor: {antrean}")

    sesi += 1
    print("----------------")