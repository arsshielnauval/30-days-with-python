#Variables

nama = "Arshiel"
umur = 22
negara = "Indonesia"

print(f"Nama saya {nama}")
print(f"Umur saya {umur}")
print(f"Saya tinggal di {negara}")

print(len("Data Science"))

nama = input("Masukkan nama: ")
umur = int(input("Masukkan umur: "))

print(f"Halo {nama}")
print(f"Umur kamu {umur}")

umur = int(input("Masukkan umur: "))
hari = umur * 365

print(f"Umur kamu dalam hari adalah {hari}")

# BIODATA
nama = input("Masukkan nama: ")
umur = int(input("Masukkan umur: "))
negara = input("Masukkan negara: ")
pekerjaan = input("Masukkan pekerjaan: ")

print("\n===== BIODATA =====")
print(f"Nama : {nama}")
print(f"Umur : {umur}")
print(f"Negara : {negara}")
print(f"Pekerjaan : {pekerjaan}")

# KONVERSI TAHUN KE HARI
tahun = int(input("\nMasukkan jumlah tahun: "))
hari = tahun * 365

print(f"{tahun} tahun adalah {hari} hari")

# RATA-RATA NILAI
nilai1 = int(input("\nMasukkan nilai 1: "))
nilai2 = int(input("Masukkan nilai 2: "))
nilai3 = int(input("Masukkan nilai 3: "))

rata = (nilai1 + nilai2 + nilai3) / 3

print(f"Rata-rata nilai adalah {rata}")
