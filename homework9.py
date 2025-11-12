# # 1.“To‘plamga yangi element qo‘shish funksiyasi.”
# thisset = {"cat", "dog", "duck"}
# thisset.add('house')
# print(thisset)
# thisset = {"matem","ingliz tili", "ona tili"}
# thisset.add("informatika")
# print(thisset)
#
# # 2.To‘plamdagi barcha elementlarni olib tashlaydi.
# fruits = {"apple", "banana", "strawbery"}
# fruits.clear()
# print(fruits)
# thisset = {"trigonometriya", "streometriya", "hosila", "integral"}
# thisset.clear()
# print(thisset)
#
# # 3.“To‘plamning nusxasini qaytaradi.”
# fruits = {"apple", "banana", "strawbery"}
# x = fruits.copy()
# print(x)
# thisset = {"trigonometriya", "streometriya", "hosila", "integral"}
# x = thisset.copy()
# print(x)
#
# # 4.To‘plamlar orasidagi farqli elementlardan yangi to‘plam hosil qiladi.”
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.difference(y)
# print(z)
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = y.difference(x)
# print(z)
#
# # 5.Boshqa to‘plamda bor elementlarni bu to‘plamdan o‘chiradi.”
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.difference_update(y)
# print(x)
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# y.difference_update(x)
# print(y)
#
# # 6.“Berilgan elementni o‘chiradi.”
# fruits = {"apple", "banana", "cherry"}
# fruits.discard("banana")
# print(fruits)
# thisset = {"trigonometriya", "streometriya", "hosila", "integral"}
# thisset.discard("hosila")
# print(thisset)
#
# # 7.“Ikki to‘plamda ham mavjud bo‘lgan elementlardan yangi to‘plam hosil qiladi.”
# x = {"instagram", "telegram", "facebook"}
# y = {"google", "microsoft", "instagram"}
# z = x.intersection(y)
# print(z)
# A = {"a", "b", "k"}
# B = {"b", "k","g"}
# z = A.intersection(B)
# print(z)
#
# # 8.“Faqat boshqa to‘plam(lar)da ham bor elementlargina qoldiriladi.”
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.intersection_update(y)
# print(x)
# x = {"a", "b", "c"}
# y = {"c", "d", "e"}
# z = {"f", "g", "c"}
# x &= y & z
# print(x)

# # 9.“Ikki to‘plam o‘zaro kesishadimi yoki yo‘qmi — shuni tekshiradi.”
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "facebook"}
# z = x.isdisjoint(y)
# print(z)
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.isdisjoint(y)
# print(z)
#
# # 10.“Bu to‘plamning hamma elementlari boshqa to‘plamda bo‘lsa, True qaytaradi.”Agar bu to‘plamdagi hamma elementlar kattaroq to‘plamda bo‘lsa, True qaytaradi.
# x = {"a", "b", "c"}
# y = {"f", "e", "d", "c", "b", "a"}
# z = x.issubset(y)
# print(z)
# x = {"a", "b", "c"}
# y = {"f", "e", "d", "c", "b", "a"}
# z = x <= y
# print(z)

# # 11.Boshqa to‘plamdagi hamma elementlar bu to‘plamda bo‘lsa, True qaytaradi.
# #Agar kichik to‘plamning hamma elementlari bu to‘plam ichida bo‘lsa, True chiqadi."
# x = {"f", "e", "d", "c", "b", "a"}
# y = {"a", "b", "c"}
# z = x.issuperset(y)
# print(z)
# x = {"f", "e", "d", "c", "b", "a"}
# y = {"a", "b", "c"}
# z = x >= y
# print(z)
# x = {"f", "e", "d", "c", "b"}
# y = {"a", "b", "c"}
# z = x.issuperset(y)
# print(z)

# #12. To‘plamdagi elementni olib tashlaydi."
# fruits = {"apple", "banana", "cherry"}
# fruits.pop()
# print(fruits)
# fruits = {"apple", "banana", "cherry"}
# x = fruits.pop()
# print(x)

# # 13.remove() funksiyasi to‘plamdan berilgan elementni olib tashlaydi.
# fruits = {"apple", "banana", "cherry"}
# fruits.remove("banana")
# print(fruits)
# cars = {"bmw","mercedes benz","Ki5"}
# cars.remove("mercedes benz")
# print(cars)
#
# # 14.Bu metod ikki to‘plamda faqat bittasida mavjud bo‘lgan elementlardan iborat yangi to‘plamni qaytaradi.
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.symmetric_difference(y)
# print(z)
# A = {'a','b','g'}
# B = {'b','c','g','m'}
# print(A.symmetric_difference(B))
# x = {"A", "B", "C"}
# y = {"F", "G", "A"}
# print(x ^ y)
#
# # 15.“Bu to‘plamga boshqa to‘plamdan faqat bittasida mavjud bo‘lgan elementlarni qo‘shadi.
# x = {"qulupnay", "olma", "anor"}
# y = {"google", "banan", "olma"}
# x.symmetric_difference_update(y)
# print(x)
# x = {"qulupnay", "olma", "anor"}
# y = {"google", "banan", "olma"}
# x ^= y
# print(x)

# # 16.Ikki yoki undan ortiq to‘plamdagi barcha elementlarni birlashtirib yangi to‘plam qaytaradi.
# x = {"qulupnay", "olma", "anor"}
# y = {"google", "banan", "olma"}
# z = x.union(y)
# print(z)
# x = {"qulupnay", "olma", "anor"}
# y = {"google", "banan", "olma"}
# z = x | y
# print(z)
# x = {"a", "b", "c"}
# y = {"f", "d", "a"}
# z = {"c", "d", "e"}
# result = x.union(y, z)
# print(result)
# x = {"a", "b", "c"}
# y = {"c", "d", "e"}
# z = {"f", "g", "c"}
# result = x | y | z
# print(result)

# # 17.“Bu to‘plamga boshqa to‘plamlardagi barcha elementlarni qo‘shib yangilaydi.”
# x = {"qulupnay", "olma", "anor"}
# y = {"google", "banan", "olma"}
# x.update(y)
# print(x)
# x = {"qulupnay", "olma", "anor"}
# y = {"google", "banan", "olma"}
# x |= y
# print(x)
# x = {"qulupnay", "olma", "anor"}
# y = {"google", "banan", "olma"}
# z = {"cherry", "green", "red"}
# x.update(y, z)
# print(x)
# x = {"qulupnay", "olma", "anor"}
# y = {"google", "banan", "olma"}
# z = {"cherry", "green", "red"}
# x |= y | z
# print(x)