# #1
# def user_data(first_name, last_name, age):
#     print(f"Ism: {first_name.title()}")
#     print(f"Familiya: {last_name.title()}")
#     print(f"Yosh: {age}")
#
# ism = input("Ismingiz: ")
# fam = input("Familiyangiz: ")
# yosh = input("Yoshingiz: ")
#
# user_data(ism, fam, yosh)
#

# #2
# def find_max(a, b, c):
#     if a>b and a>c:
#         print("Eng katta son: A =", a)
#     if b>a and b>c:
#         print("Eng katta son: B =", b)
#     if c>a and c>b:
#         print("Eng katta son: C =", c)
#     if a==b and b>c:
#         print("Eng katta son: A va B =", a,)
#     if b==c and b>a:
#         print("Eng katta son: B va C =", b,)
#     if a==c and c>b:
#         print("Eng katta son: A va C =", a)
#     if a==b and b==c and c==a:
#         print("Eng katta son: A, B va C =",a)
#
# a = int(input("A: "))
# b = int(input("B: "))
# c = int(input("C: "))
#
# find_max(a, b, c)


# #3
# def find_letter_count(word, letter):
#     count = word.count(letter)
#     print(f'"{word}" so‘zida "{letter}" dan {count} ta.')
#
# word = input("So‘z: ")
# letter = input("Qaysi harf? ")
# find_letter_count(word, letter)

# # 4
# def list_sum(myList):
#     print("Listning elementlar yig'indisi =", sum(myList))
#
# myList = [15, 7, 10, 10]
# list_sum(myList)

# #5
# def daraja(a, b):
#     print(a ** b)
#
# daraja(2, 5)


# #6
# def daraja4(a, b, c, d):
#     print(a ** b, a ** c, a ** d)
#
# daraja4(2, 3, 4, 5)

# #7
# def digit_count_and_sum(word):
#     summ = 0
#     count = 0
#     for i in word:
#         if i.isdigit():
#             summ += int(i)
#             count += 1
#     print("Raqamlar yig'indisi:", summ)
#     print("Raqamlar soni:", count)
#
# digit_count_and_sum("ab12c3")

# #8
# def add_right(a, b):
#     print(int(str(a) + str(b)))
#
# add_right(12, 34)

# #9
# def add_left(a, b):
#     print(int(str(b) + str(a)))
#
# add_left(12, 34)

# #10
# def work_with_list(a):
#     mn = min(a)
#     for i in range(len(a)):
#         a[i] *= mn
#     print(a)
#
# work_with_list([5, 2, 7])


# # 11.
# def big_sales(sales):
#     return max(sales, key=sales.get)
#
# sales = {
#     "yanvar": 12000,
#     "mart": 6000,
#     "aprel": 15000,
#     "sentabr": 9000,
#     "dekabr": 10000
# }
#
# print(big_sales(sales))

# #12
# def min_max(numbers, max_num, min_num):
#     print("max_num eng katta sonmi?", max_num == max(numbers))
#     print("min_num eng kichik sonmi?", min_num == min(numbers))
#
# numbers = [3, 7, 2, 9, 5]
# min_max(numbers, 9, 3)


