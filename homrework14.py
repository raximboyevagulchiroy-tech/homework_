# # 1.
# def foydalanuvchi_info(ism, familiya, **malumot):
#     info = {
#         "ism": ism.title(),
#         "familiya": familiya.title()
#     }
#     info.update(malumot)
#     return info
#
# print(foydalanuvchi_info("aziz", "raximov", yil=2008, manzil="Xorazm", email="raximov@gmail.com"))



# # 2.
# def foydalanuvchi_info(ism, familiya, **malumot):
#     info = {
#         "ism": ism.title(),
#         "familiya": familiya.title()
#     }
#
# mijozlar = []
#
# while True:
#     print("\nYangi mijoz ma'lumotlari:")
#     ism = input("Ismi: ")
#     familiya = input("Familiyasi: ")
#     yosh = input("Yoshi: ")
#
#     mijoz = foydalanuvchi_info(ism, familiya, yosh=yosh)
#     mijozlar.append(mijoz)
#
#     stop = input("Yana qo'shasizmi? (ha/yo'q): ")
#     if stop.lower() == "yo'q":
#         break
#
# print("\nMijozlar ro'yxati:")
# for m in mijozlar:
#     print(m)


# # 3.
# def sonlar(a, b, c):
#     sonlar = max(a, b, c)
#     return sonlar
# print(sonlar(12, 29, 37))
#

# # 4.
# def aylana_info(radius):
#     diametr = 2 * radius
#     perimetr = 2 * 3.14 * radius
#     yuza = 3.14 * radius * radius
#
#     info =  {
#         "radius": radius,
#         "diametr": diametr,
#         "perimetr": perimetr,
#         "yuza": yuza
#     }
#     return info
# print(aylana_info(10))

# # 5.
# def tub_sonlar(a, b):
#     tublar = []
#     for son in range(a, b+1):
#         if son > 1:
#             for i in range(2, int(son**0.5)+1):
#                 if son % i == 0:
#                     break
#             else:
#                 tublar.append(son)
#     return tublar
#
# print(tub_sonlar(1, 20))

# # 6.
# def fibonacci(n):
#     fib = [1, 1]
#     for i in range(2, n):
#         fib.append(fib[-1] + fib[-2])
#     return fib[:n]
# print(fibonacci(10))