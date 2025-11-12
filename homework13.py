# # 1
# def yil(ism,yosh):
#     tugilgan_yil = 2025 - int(yosh)
#     print(f"Hurmatli {ism} siz tug'ilgan yil: ", tugilgan_yil)
#
# ism = input("Ismingizni kiriting: ")
# yosh = input("Yoshingizni kiriting: ")
#
# yil(ism,yosh)

# # 2
# def son(a):
#     kvadrat = a**2
#     kub = a**3
#     print("Kiritilgan sonning kvadrati: ", kvadrat)
#     print("Kiritilgan sonning kubi: ", kub)
#
# a = float(input("a sonini kiriting: "))
# son(a)


# # 3
# def son(a):
#     if a % 2 == 0:
#         print("Berilgan son juft")
#     else:
#         print("Berilgan son toq")
#
# a = int(input("a sonini kiriting: "))
# son(a)

# # 4
# def son(a,b):
#     if a>b:
#         print(a)
#     elif b>a:
#         print(b)
#     else:
#         print("Sonlar teng")
#
# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))
# son(a,b)

# # 5
# def son(x,y):
#     A = x**y
#     print("x^y =",A)
#
# x = int(input("x ni kiriting: "))
# y = int(input("y ni kiriting: "))
# son(x,y)

# # 6
# def son(x,y=2):
#     A = x**y
#     print("x^y =",A)
#
# x = int(input("x ni kiriting: "))
# son(x,y=2)

# # 7
# def bolinish_alomatlari(a):
#     for i in range(2,11):
#         if  a % i == 0:
#          print(f"{a} {i} ga qoldiqsiz bo'linadi")
#
# a = int(input("a sonini kiriting: "))
# bolinish_alomatlari(a)

