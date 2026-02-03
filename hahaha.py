
Latihannnn

Buat program:

Input umur

Jika umur >= 18 → "Dewasa"

Jika < 18 → "Belum Dewasa"

umur = int(input("Masukan Umur :"))

if umur >= 18:
    print("Dewasa")
elif umur < 18 :
    print("Belum Dewasa")
else:
    print("Nilai tidak valid")

    # -----------------------------------------------

    Soal 2 (Menengah)

Input nilai ujian dan absensi (%)

Syarat lulus:

Nilai ≥ 70

Absensi ≥ 75

Jika salah satu tidak memenuhi → Tidak Lulus


nama = input("Masukkan nama: ")
nilai = int(input("Masukkan nilai: "))
absensi = int(input("Masukkan absensi (%): "))

if nilai >= 70 and absensi >= 75:
    print(f"Maka siswa {nama} lulus")

elif nilai < 70 and absensi < 75:
    print(f"Maka siswa {nama} tidak lulus")

elif nilai >= 70 and absensi < 75:
    print(f" maka siswa {nama} ikut ujian tambahan ")

elif nilai < 70 and absensi >= 75:
    print(f"Maka siswa {nama} diluluskan dengan di denda!")

elif nilai >= 95 and < 100 and absensi < 75 :
    print (f"Maka siswa {nama} di luluskan karena nilainya bagus")

else:
    print("Nilai tidak valid")


Soal 3 (Grading + Predikat)

Tambahkan predikat:

Grade  |	Predikat
A	    | Sangat Baik
B	    | Baik
C	    | Cukup
D	    | Kurang
E	    | Gagal

nama = input("Masukkan nama :")
nilai = int(input("Masukkan Nilai :"))


if nilai >= 95 and nilai < 100  :
    grade = "A"
    predikat = "Sangat baik"
elif nilai >= 85 :
    grade = "B"
    predikat ="Baik"
elif nilai >= 75 :
    grade = "C"
    predikat ="Cukup"
elif nilai >= 65 :
    grade = "D"
    predikat ="Kurang"
elif nilai < 65 :
    grade = "D"
    predikat ="Gagal"
else:
    grade ("tidak valid")

print(f" Mahasiswa {nama} Mendapatkan nilai : {nilai}\n Maka Grade {grade}\n Predikatnya Adalah {predikat} ")

-----------------------------------------------------------------------------

Soal 4 (Logika Kompleks – Level Mahasiswa)
Buat sistem beasiswa:

Input:

IPK
Penghasilan orang tua

Aturan:

IPK ≥ 3.5 DAN Penghasilan < 3 juta → Full
IPK ≥ 3.0 DAN Penghasilan < 5 juta → Parsial
Lainnya → Tidak Dapat

nama = input("Masukan nama :")
nilai = float(input("Nilai IPK :"))
penghasilan = int(input("penghasilan :"))


if nilai >= 3.5 and penghasilan < 3000000 :
    beasiswa = "Full"
elif nilai >= 3.0 and penghasilan < 5000000 :
    beasiswa = "Parsial"
else :
    print(" Tidak Ada Beasiswa ")

print (f"Maka siswa {nama} Mendapatkan beasiswa {beasiswa} ")
