# Program: Sistem Nilai

# Buat program:

# Input:
# Nama
# Nilai (0–100)

# Output:
# Nama: Dho
# Nilai: 82
# Grade: B
# Status: Lulus

# Aturan:
# Nilai	Grade	Status
# ≥85	A	Lulus
# 70–84	B	Lulus
# 55–69	C	Remed
# <55	D	Gagal

nama = input("Masukkan Nama : ")
nilai = int(input("Nilainya :"))

if ( nilai < 0 or nilai > 100):
    print("Nilai tidak Valid")

else:
    if nilai >= 85 :
        grade = "A"
        status = "Lulus"
    elif nilai >= 70 :
        grade = "B"
        status = "Lulus"
    elif nilai >= 55 :
        grade = "C"
        status = "Remed"
    elif nilai < 55 :
        grade = "D"
        status = "Tidak Lulus"

print("Nama :", nama)
print("Nilai :", nilai)
print("Grade :", grade)
print("Status :", status)
