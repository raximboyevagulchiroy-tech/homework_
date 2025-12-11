# 1
import datetime as dt

hozir = dt.datetime.now()

for i in range(10):
    sana = hozir + dt.timedelta(days=14 * i)
    print(sana.date())


# 2
import datetime as dt

bugun = dt.datetime.today()

ramazon = dt.datetime(2026, 2, 18)
qurbon_hayiti = dt.datetime(2026, 5, 27)

ramazon_gacha = (ramazon - bugun).days
hayit_gacha = (qurbon_hayiti - bugun).days

print(f"Bugungi kundan Ramazon boshlanishigacha {ramazon_gacha} kun qoldi.")
print(f"Bugungi kundan Qurbon hayitigacha {hayit_gacha} kun qoldi.")


# 3
import datetime as dt
def hisoblash(yil,oy,kun):
    bugun = dt.datetime.today()
    tugilgan_kun = dt.datetime(yil,oy,kun)

    yil_farq = bugun.year - tugilgan_kun.year
    oy_farq = bugun.month - tugilgan_kun.month
    kun_farq = abs(bugun.day - tugilgan_kun.day)
    return yil_farq,oy_farq,kun_farq

y,o,k = hisoblash(2006,7,14)
print(f"{y} yil {o} oy {k} kun")


# 4
import re
tel_nomer = input("Telefon raqamingizni kiriting: ")
andoza = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
if re.match(andoza, tel_nomer):
    print("Raqam to‘g‘ri kiritildi.")
else:
    print("Raqam xato kiritildi.")

# 5
import re
def url(matn):
    andoza = r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)"
    url_top = re.findall(andoza, matn)
    return url_top

matn = "Darslar uchun resurslarni shu yerda topishingiz mumkin: https://www.kurslar.uz/python. Shu bilan birga, www.learn-uz.com ham juda foydali. Qo‘shimcha ma’lumotlar esa http://blog.example.net/tutorials sahifasida mavjud."
print(url(matn))
