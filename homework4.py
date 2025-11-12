# # O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
# davlatlar = ["Turkiya", "Amerika", "Rossiya", "O'zbekiston", "Germaniya", "Fransiya"]
# print(davlatlar)
#
# # Ro'yxatning uzunligini konsolga chiqaring
# hayvonlar = ["mushuk", "ot", "sher", "zebra", "yo'lbars"]
# print("Elementlar soni:", len(hayvonlar))
#
# # sorted()funksiyasiyordamida ro'yxatni tartiblangan holda konsolga chiqaring
# ranglar = ["yashil", "qizil", "ko'k", "pushti", "qora", "oq"]
# print("sorted() qaytargan ro'yxat:", sorted(ranglar))
#
# # sorted() yordamida ro'yxatni teskari tartibda ro'yxatga chiqaring
# ranglar = ["yashil", "qizil", "ko'k", "pushti", "qora", "oq"]
# print(sorted(ranglar, reverse=True))
#
# # Asl ro'yxatni qaytadan konsolga chiqaring
# ranglar = ["yashil", "qizil", "ko'k", "pushti", "qora", "oq"]
# print("sorted() qaytargan ro'yxat:", sorted(ranglar))
# print("Asl ro'yxat o'zgarmas qoldi:", ranglar)
#
# # reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
# kitoblar = ["o'tkan kunlar", "kecha va kunduz", "mehrobdan chayon", "ufq", "dunyoning ishlari", "ikki eshik orasi"]
# kitoblar.reverse()
# print(kitoblar)
#
# # sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring
# fanlar = ["matematika", "ingliz tili", "tarix", "ona tili"]
# fanlar.sort()
# print(fanlar)
# fanlar.reverse()
# print(fanlar)
#
# # 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
# juft_sonlar = list(range(120, 1200, 2))
# print("juft_sonlar:", juft_sonlar)
#
# # Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
# sonlar = 123, 124, 156, 157
# print(sum(sonlar))
#
# # Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
# sonlar = 123, 124, 156, 157
# son1 = min(sonlar)
# son2 = max(sonlar)
# print("ayirma:", int(son2 - son1))
#
# # Ro'yxatdagi elementlar sonini hisoblang
# kasblar = ["dasturchi", "o'qituvchi", "shifokor", "styuardessa", "diplomat"]
# print(len(kasblar))
#
# # Ro'yxatning boshidan,o'rtasidan va oxiridan 20ta qiymatni konsolga chiqaring
# sonlar = list(range(125, 356))
# print
# # taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
# taomlar = "manti", "palov", "lag'mon", "bishteks", "xonim"
# print(taomlar)
#
# # nonushta degan yangi ro'yxatga taomlardan nusxa oling
# nonushta = "manti", "palov", "lag'mon", "bishteks", "xonim"
# print(nonushta)
#
# # Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring va qo'shimcha 2ta taom qo'shing
# nonushta = "blinchik", "pyure", "kaklet", "pankeyk", "granada"
# print(nonushta)
#
# # Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
# taomlar = "manti", "palov", "lag'mon", "bishteks", "xonim"
# nonushta = "blinchik", "pyure", "kaklet", "pankeyk", "granada"
# print(taomlar, nonushta)
#
# # Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring
# nonushta = "blinchik", "pyure", "kaklet", "pankeyk", "granada"
