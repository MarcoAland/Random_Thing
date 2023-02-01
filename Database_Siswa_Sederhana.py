import datetime
import os 
import string
import random

siswa_template = {
    'nama':'nama',
    'kelas':'kelas',
    'tahun_lulus':'tahun_lulus',
    'lahir':datetime.datetime(1111,1,11),
}

data_siswa = {}

while True :
    os.system("cls")

    print(f"{'SELAMAT DATANG':^80}")
    print(f"{'DATA SISWA':^80}")
    print("-"*80)

    siswa = dict.fromkeys(siswa_template.keys())
    siswa['nama'] = input("Nama siswa: ")
    siswa['kelas'] = input("Kelas: ")
    siswa['tahun_lulus'] = int(input("Tahun lulus: "))
    TAHUN_LAHIR = int(input("Tahun lahir (YYYY): "))
    BULAN_LAHIR = int(input("Bulan lahir (1-12): "))
    TANGGAL_LAHIR = int(input("Tanggal lahir (1-31): "))
    siswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_siswa.update({KEY:siswa})

    print(f"\n{'KEY':<8} {'Nama':<25} {'Kelas':<12} {'Tahun Lulus':<15} {'Tanggal Lahir':<15}")
    print('-'*80)
    
    for siswa in data_siswa:
        KEY = siswa

        NAMA = data_siswa[KEY]['nama']
        KELAS = data_siswa[KEY]['kelas']
        TAHUN_LULUS = data_siswa[KEY]['tahun_lulus']
        LAHIR = data_siswa[KEY]['lahir'].strftime("%x")

        print(f"{KEY:<8} {NAMA:<25} {KELAS:<12} {TAHUN_LULUS:<15} {LAHIR:<15}")

    print("\n")
    is_done = input("Mau tambah lagi bro (y/n)? ")
    if is_done == "n":
	    break

print("\nAkhir dari program, terima kasih")
