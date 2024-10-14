from getpass import getpass
from prettytable import PrettyTable

# Data pengguna
users = {'admin': 'admin123', 'pasien': 'pasien123'}
pasien_data = []
queue = []

def pilih_peran():
    print("=== Sistem Manajemen Rumah Sakit Dirgahayu ===")
    print("1. Admin")
    print("2. Pasien")
    print("3. Keluar")
    pilihan = input("Pilih (1-3): ")
    return pilihan

def login(role):
    print(f"\nLogin sebagai {role}")
    username = input("Username: ")
    password = getpass("Password: ")
    if username in users and users[username] == password:
        print(f"Login berhasil, {username}\n")
        return True
    else:
        print("Login gagal\n")
        return False

def menu_admin():
    while True:
        print("\n1. Tambah Data Pasien")
        print("2. Lihat Data Pasien")
        print("3. Update Data Pasien")
        print("4. Hapus Data Pasien")
        print("5. Logout")
        pilihan = input("Pilih (1-5): ")
        if pilihan == '1': tambah_pasien()
        elif pilihan == '2': lihat_pasien()
        elif pilihan == '3': update_pasien()
        elif pilihan == '4': hapus_pasien()
        elif pilihan == '5': break

def tambah_pasien():
    nama = input("Nama Pasien: ")
    usia = input("Usia Pasien: ")
    kondisi = input("Keluhan Pasien: ")
    nomorhp = input("Nomor hp: ")
    pasien_data.append({'Nama': nama, 'Usia': usia, 'Kondisi': kondisi, 'Nomor hp': nomorhp})
    print(f"Pasien atas {nama} telah ditambahkan.\n")

def lihat_pasien():
    if not pasien_data:
        print("Belum ada data pasien.\n")
    else:
        table = PrettyTable(["No", "Nama", "Usia", "Kondisi", "Nomor hp"])
        for i, pasien in enumerate(pasien_data):
            table.add_row([i + 1, pasien['Nama'], pasien['Usia'], pasien['Kondisi'], pasien['Nomor hp']])
        print(table)

def update_pasien():
    lihat_pasien()
    nomor = int(input("Nomor pasien yang ingin diupdate: ")) - 1
    if 0 <= nomor < len(pasien_data):
        pasien_data[nomor]['Nama'] = input("Nama baru: ") or pasien_data[nomor]['Nama']
        pasien_data[nomor]['Usia'] = input("Usia baru: ") or pasien_data[nomor]['Usia']
        pasien_data[nomor]['Kondisi'] = input("Kondisi baru: ") or pasien_data[nomor]['Kondisi']
        pasien_data[nomor]['Nomor hp'] = input("Nomor hp baru: ") or pasien_data[nomor]['Nomor hp']
        print("Data diperbarui.\n")

def hapus_pasien():
    lihat_pasien()
    nomor = int(input("Nomor pasien yang ingin dihapus: ")) - 1
    if 0 <= nomor < len(pasien_data):
        print(f"Pasien {pasien_data.pop(nomor)['Nama']} dihapus.\n")

def menu_pasien():
    while True:
        print("\n1. Daftar Antrian")
        print("2. Lihat Antrian")
        print("3. Logout")
        pilihan = input("Pilih (1-3): ")
        if pilihan == '1': daftar_antrian()
        elif pilihan == '2': lihat_antrian()
        elif pilihan == '3': break

def daftar_antrian():
    nama = input("Nama Pasien: ")
    queue.append(nama)
    print(f"Pasien {nama} masuk antrian.\n")

def lihat_antrian():
    if not queue:
        print("Antrian kosong.\n")
    else:
        table = PrettyTable(["No", "Nama"])
        for i, nama in enumerate(queue):
            table.add_row([i + 1, nama])
        print(table)

def main():
    while True:
        pilihan = pilih_peran()
        if pilihan == '1' and login('Admin'): menu_admin()
        elif pilihan == '2' and login('Pasien'): menu_pasien()
        elif pilihan == '3': break

if __name__ == "__main__":
    main()
