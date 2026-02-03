# Buat sistem login.
# Data benar:
# Username: admin
# Password: 12345
# Aturan:
# Jika dua-duanya benar → Login berhasil
# Salah satu salah → Login gagal
# Jika salah 3 kali → Akun diblokir
# Gunakan while + if.

dataAdmin = "admin"
dataPassword = "12345"

coba = 0
maks = 3

while coba < maks:

    admin = input("Masukkan nama Admin: ").lower()
    password = input("Masukkan Password: ")

    if admin == dataAdmin and password == dataPassword:
        print("Login berhasil")
        break

    else:
        coba += 1
        sisa = maks - coba
        print(f"Login gagal. Sisa percobaan: {sisa}")

else:
    print("Akun terblokir")


