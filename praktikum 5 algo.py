print('@@@@@@@ @ @@@@@ @    @ @@@@@ @@@@@ @')
print('@  @  @ @ @     @    @ @   @ @     @')
print('@  @  @ @ @     @@@@@@ @@@@@ @@@@@ @')
print('@  @  @ @ @     @    @ @   @ @     @')
print('@  @  @ @ @@@@@ @    @ @   @ @@@@@ @@@@@')

jumlah_bilangan = int(input("masukkan jumlah bilangan: "))
angka_pertama = int(input("masukkan angka pertama: "))
angka_kedua = int(input("masukkan angka kedua: "))

deret_fibonacci = [angka_pertama, angka_kedua]

for i in range(2, jumlah_bilangan):
    next_fibonacci = deret_fibonacci[i-1] + deret_fibonacci[i-2]
    deret_fibonacci.append(next_fibonacci)

for angka in deret_fibonacci:
    print("berikut urutannya \n", angka)





print('@@@@@@@ @ @@@@@ @    @ @@@@@ @@@@@ @')
print('@  @  @ @ @     @    @ @   @ @     @')
print('@  @  @ @ @     @@@@@@ @@@@@ @@@@@ @')
print('@  @  @ @ @     @    @ @   @ @     @')
print('@  @  @ @ @@@@@ @    @ @   @ @@@@@ @@@@@')

print("\n===== HITUNGAN GAJI =====\n")

# Input jam kerja
jamMasukKerja = float(input('Jam masuk kantor: '))

# Ucapan selamat pagi, siang, sore, malam berdasarkan waktu
if jamMasukKerja >= 6.00 and jamMasukKerja <= 12.00:
    print("Selamat pagi\n")
elif jamMasukKerja >= 12.00 and jamMasukKerja <= 15.00:
    print("Selamat siang\n")
elif jamMasukKerja >= 15.00 and jamMasukKerja <= 18.00:
    print("Selamat sore\n")
elif jamMasukKerja >= 18.00 and jamMasukKerja <= 24.00:
    print("Selamat malam\n")

# Input jam keluar kerja
jamKeluarKerja = float(input('Jam pulang kantor: '))

# Ucapan selamat pagi, siang, sore, malam berdasarkan waktu
if jamKeluarKerja >= 6.00 and jamKeluarKerja <= 12.00:
    print("Selamat pagi\n")
elif jamKeluarKerja >= 12.00 and jamKeluarKerja <= 15.00:
    print("Selamat siang\n")
elif jamKeluarKerja >= 15.00 and jamKeluarKerja <= 18.00:
    print("Selamat sore\n") 
elif jamKeluarKerja >= 18.00 and jamKeluarKerja <= 24.00:
    print("Selamat malam\n")

# Rincian gaji
print('===== Rincian Gaji Harian =====')
waktuKerja = (jamKeluarKerja - jamMasukKerja)
print(f"Total jam kerja: {int(waktuKerja)} jam")
gajiPerHari = 175000
if waktuKerja <= 8:
    gaji_total = gajiPerHari
else:
    gajiLembur = (int(waktuKerja) - 8) * 15000
    gaji_total = gajiPerHari + gajiLembur

# Menampilkan gaji per hari
print(f"Gaji harian    : Rp. {gajiPerHari}")
print(f"Lembur         : Rp. {gajiLembur:.2f} ({int(waktuKerja - 8)} jam x Rp.15000)")
print(f"Total          : Rp. {gaji_total:.2f}")

print("===== TERIMAKASIH =====")