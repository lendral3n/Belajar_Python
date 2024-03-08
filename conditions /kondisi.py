#Kondisi if adalah kondisi yang akan dieksekusi oleh program jika bernilai benar atau TRUE

nilai = 9

#jika kondisi benar/TRUE maka program akan mengeksekusi perintah dibawahnya
if(nilai > 7):
    print("Sembilan Lebih Besar Dari Angka Tujuh") # Kondisi Benar, Dieksekusi

#jika kondisi salah/FALSE maka program tidak akan mengeksekusi perintah dibawahnya
if(nilai > 10):
    print("Sembilan Lebih Besar Dari Angka Sepuluh") # Kondisi Salah, Maka tidak tereksekusi
    
    
# Kondisi if else adalah jika kondisi bernilai TRUE maka akan dieksekusi pada if,
# tetapi jika bernilai FALSE maka akan dieksekusi kode pada else

nilai = 3
# Jika pernyataan pada if bernilai TRUE maka if akan dieksekusi,
# tetapi jika FALSE kode pada else yang akan dieksekusi.
if(nilai > 7):
    print("Selamat Anda Lulus")
else:
    print("Maaf Anda Tidak Lulus")
    
    
hari_ini = "Minggu"

if(hari_ini == "Senin"):
    print("Saya akan ngoding")
elif(hari_ini == "Selasa"):
    print("Saya akan ngoding")
elif(hari_ini == "Rabu"):
    print("Saya akan ngoding")
elif(hari_ini == "Kamis"):
    print("Saya akan ngoding")
elif(hari_ini == "Jumat"):
    print("Saya akan ngoding")
elif(hari_ini == "Sabtu"):
    print("Saya akan ngoding")
elif(hari_ini == "Minggu"):
    print("Saya akan libur")