import calendar
import time;


ticks = time.time()
print("berjalan sejak 12:00pm, January 1, 1970:", ticks)

# dapatkan Waktu Saat Ini
localtime = time.localtime(time.time())
print("waktu lokal saat ini : ", localtime)

# dapatkan Waktu yang berformat
localtimes = time.asctime( time.localtime(time.time()))
print("waktu lokal saat ini", localtimes)

# dapatkan kalender dalam sebulan
cal = calendar.month(2024, 1)
print("dibawah ini adalah kalender : ", cal)