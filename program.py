# Program Pengecekan Perubahan Data Profil User Menggunakan MD5

import hashlib

# Fungsi untuk membuat hash MD5
def buat_md5(data):
    return hashlib.md5(data.encode()).hexdigest()

# =========================
# INPUT DATA AWAL USER
# =========================
print("=== INPUT DATA PROFIL USER AWAL ===")
nama = input("Masukkan Nama   : ")
email = input("Masukkan Email  : ")
no_hp = input("Masukkan No HP  : ")

# Gabungkan semua data user menjadi satu string
data_awal = nama + email + no_hp

# Membuat hash MD5 dari data awal
hash_awal = buat_md5(data_awal)

# Menampilkan hash awal
print("\nHash MD5 Awal :", hash_awal)

# =========================
# INPUT DATA BARU USER
# =========================
print("\n=== INPUT DATA PROFIL USER BARU ===")
nama_baru = input("Masukkan Nama Baru   : ")
email_baru = input("Masukkan Email Baru  : ")
no_hp_baru = input("Masukkan No HP Baru  : ")

# Gabungkan data baru
data_baru = nama_baru + email_baru + no_hp_baru

# Membuat hash MD5 dari data baru
hash_baru = buat_md5(data_baru)

# Menampilkan hash baru
print("\nHash MD5 Baru :", hash_baru)

# =========================
# MEMBANDINGKAN HASH
# =========================
print("\n=== HASIL PERBANDINGAN ===")
print("Hash Lama :", hash_awal)
print("Hash Baru :", hash_baru)

# Menentukan status perubahan data
if hash_awal == hash_baru:
    print("Status: Data profil TIDAK mengalami perubahan.")
else:
    print("Status: Data profil TELAH berubah atau dimodifikasi.")