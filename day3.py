#Strings

text = "python"
print(text[0])
print(text[4])
print(text[-1])

text = "datascience"
print(text[0:4])
print(text[4:])

text = "Saya Belajar Python"

print(text.lower())
print(text.upper())
print(text.split())

kalimat = input("Masukkan kalimat: ")

print(kalimat)
print(f"Jumlah karakter: {len(kalimat)}")
print(f"Jumlah kata: {len(kalimat.split())}")
print(f"Huruf kecil: {kalimat.lower()}")