# Kerjakan ini TANPA COPY.
# Soal Baru:
# Buat sistem parkir:
# Input:
# Jam masuk
# Jam keluar
# Aturan:
# 2 jam pertama: 5000/jam
# Setelah itu: 3000/jam
# Output:
# Total bayar.
# Contoh:
# Masuk 8, keluar 13 → 5 jam
# Bayar = 2×5000 + 3×3000 = 19000

jam_masuk = int(input("Masukkan jam masuk: "))
jam_keluar = int(input("Masukkan jam keluar: "))

durasi = jam_keluar - jam_masuk

if durasi <= 0:
    print("Data waktu tidak valid")

elif durasi <= 2:
    total = durasi * 5000
    print("Bayar:", total)

else:
    total = (2 * 5000) + ((durasi - 2) * 3000)
    print("Bayar:", total)


