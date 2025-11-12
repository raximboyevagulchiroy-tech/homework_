# # 1-misol
# while True:
#     rang = input("Svetafor qaysi rangda?: ").lower()
#     if  rang in ["qizil","sariq","yashil"]:
#         print("Rahmat, to'g'ri keladi!")
#         break
#     else:
#         print("Xato rang")


# # 2-misol
# import random
# tasodifiy_son = random.randint(1,10)
# while True:
#     son = int(input("1 dan 10 gacha bo'lgan son tanlang: "))
#     if son == tasodifiy_son:
#         print("Tabriklaymiz, siz topdingiz")
#         break
#     else:
#         print("noto'g'ri, qayta urinib ko'ring")

# # 3-misol
# dostlar = [ ]
#
# print("Do'stlaringiz ro'yxatini tuzamiz.")
# n = 1
# while True:
#     savol = f"{n}-do'stingizni ismini kiriting: "
#     ism = input(savol)
#     dostlar.append(ism)
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     if javob == "ha":
#         n+=1
#         continue
#     else:
#         break
# print(dostlar)

# # 4-misol
# kurs = 12600
# print("valyuta ayirboshlash dasturiga xush kelibsiz!💖")
# while True:
#     summa = input("So'm miqdorini kiriting: ")
#     if summa.lower() != "exit":
#         som = int(summa)
#         dollar = som / kurs
#         print(f"{som} so'm = {dollar:.2f} USD\n")
#         continue
#     else:
#         break
#         print()
#













