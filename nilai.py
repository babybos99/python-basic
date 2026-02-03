# Tantangan Lanjutan (Naik Level)
# Kalau kamu mau naik dari “cukup” ke “kuat”, kerjakan ini:
# Soal:
# Buat sistem nilai akhir mahasiswa.
# Input:
# Tugas (30%)
# UTS (30%)
# UAS (40%)
# Hitung nilai akhir.
# Aturan:
# ≥85 → A
# ≥75 → B
# ≥65 → C
# ≥50 → D
# <50 → E
#Tambahkan validasi:
#Semua nilai harus 0–100.
tugas = int(input("Masukkan Nilai Tugas: "))
uts = int(input("Masukkan Nilai UTS: "))
uas = int(input("Masukkan Nilai UAS: "))

# Validasi
if (tugas < 0 or tugas > 100 or
    uts < 0 or uts > 100 or
    uas < 0 or uas > 100):

    print("Input nilai tidak valid") 

else:
    total = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)

    if total >= 85:
        grade = "A"

    elif total >= 75:
        grade = "B"

    elif total >= 65:
        grade = "C"

    elif total >= 50:
        grade = "D"

    else:
        grade = "E"

    print(f"Nilai Akhir: {total:.2f}")
    print(f"Grade: {grade}")
