#proses memasukan data ke dalam variabel
nama = "lendra"
#proses mencetak variabel
print(nama)

#nilai dan tipe data dalam variabel dapat diubah
umur = 20 #nilai awal
print(umur) #cetak umur
type(umur) #cek tipe data umur
print(type(umur)) #cetak type data umur
umur = "dua puluh" #nilai setelah di ubah
print(umur) #cetak umur
type(umur) #cek tipe data umur
print(type(umur)) #cetak type data umur

namaDepan = "lendra"
namaBelakang = "syaputra"
nama = namaDepan + " " + namaBelakang
umur = 20
hobi = "turu"
print("biodata\n", nama, "\n", umur, "\n", hobi)

#contoh variabel lainya
inivariabel = "Halo"
ini_juga_variabel = "Hai"
inivariabel222 = "Bye"

panjang = 10
lebar = 5
luas = panjang * lebar
print(luas)

# Banyak Nilai ke Beberapa Variabel
x, y, z = "jeruk", "pisang", "mangga"
print(x)
print(y)
print(z)

# Satu Nilai ke Beberapa Variabel
a = b = c = "MELON"
print(a)
print(b)
print(c)

# Membongkar Koleksi
buah = ["rambutan", "melon", "manggis"]
d, e, f = buah
print(d)
print(e)
print(f)

# variabel global
x = "awesom"
def myFunc():
    x = "fantastis"
    print("python is" + x)

myFunc()
print("python is" + x)