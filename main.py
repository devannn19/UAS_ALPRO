import json
import os

class Pasien:
    def __init__(self, nama, umur, keluhan):
        self.nama = nama
        self.umur = umur
        self.keluhan = keluhan

    def to_dict(self):
        return {
            "nama": self.nama,
            "umur": self.umur,
            "keluhan": self.keluhan
        }

class AntrianKlinik:
    def __init__(self):
        self.antrian = []
        self.load_data()

    def load_data(self):
        if os.path.exists('antrian.json'):
            with open('antrian.json', 'r') as file:
                data = json.load(file)
                for pasien_data in data:
                    pasien = Pasien(pasien_data['nama'], pasien_data['umur'], pasien_data['keluhan'])
                    self.antrian.append(pasien)

    def save_data(self):
        with open('antrian.json', 'w') as file:
            json.dump([pasien.to_dict() for pasien in self.antrian], file)

    def tambah_pasien(self, nama, umur, keluhan):
        pasien = Pasien(nama, umur, keluhan)
        self.antrian.append(pasien)
        self.save_data()
        print(f"Pasien {nama} telah ditambahkan ke antrian.")

    def panggil_pasien(self):
        if self.antrian:
            pasien = self.antrian.pop(0)
            self.save_data()
            print(f"Pasien yang dipanggil: {pasien.nama}, Umur: {pasien.umur}, Keluhan: {pasien.keluhan}")
        else:
            print("Tidak ada pasien dalam antrian.")

    def tampilkan_antrian(self):
        if self.antrian:
            print("Antrian Pasien:")
            for i, pasien in enumerate(self.antrian, start=1):
                print(f"{i}. Nama: {pasien.nama}, Umur: {pasien.umur}, Keluhan: {pasien.keluhan}")
        else:
            print("Antrian kosong.")

def main():
    antrian_klinik = AntrianKlinik()
    
    while True:
        print("\nSistem Manajemen Antrian Pasien Klinik")
        print("1. Tambah Pasien")
        print("2. Panggil Pasien")
        print("3. Tampilkan Antrian")
        print("4. Keluar")
        
        pilihan = input("Pilih opsi (1-4): ")
        
        if pilihan == '1':
            nama = input("Masukkan nama pasien: ")
            umur = input("Masukkan umur pasien: ")
            keluhan = input("Masukkan keluhan pasien: ")
            antrian_klinik.tambah_pasien(nama, umur, keluhan)
        elif pilihan == '2':
            antrian_klinik.panggil_pasien()
        elif pilihan == '3':
            antrian_klinik.tampilkan_antrian()
        elif pilihan == '4':
            print("Keluar dari sistem.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
