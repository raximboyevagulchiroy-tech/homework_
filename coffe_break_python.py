# 7.4 Iterable Unpacking

x, y = '12'
y, z = '34'
print(x + y + z)

"""Strings are iterables in Python. Therefore, you can use iterable unpacking to assign a string of length 2, to two
variables. After the assignments our three variables x, y, z have the following values: x = ’1’, y = ’3’, z = ’4’.
Note that the value of variable y is overwritten in the second assignment. Since you can concatenate
strings with the operator +, you get the output 134. It’s a string value, not an integer!

Python’da stringlar iteratsiya qilinadigan obyektlar hisoblanadi.Shu sababli, iterable unpacking yordamida uzunligi
2 bo‘lgan stringni 2 ta o‘zgaruvchiga biriktirish mumkin.Biriktirishlar bajarilgandan so‘ng,
bizning uchta o‘zgaruvchimiz x, y, z quyidagi qiymatlarga ega bo‘ladi: x = '1', y = '3', z = '4'.
E’tibor bering, ikkinchi biriktirishda y o‘zgaruvchisining qiymati ustiga yoziladi.
+ operatori yordamida stringlarni birlashtirish mumkin bo‘lgani uchun, natija 134 bo‘ladi. Bu string qiymat, butun son (integer) emas!"""


# 8.1 Dictionary Conditional Insert

d = {0: 'Peter', 1: 'Tom', 2: 'Mary'}
x = d.setdefault(2, 'John')
print(x)

"""The method setdefault() returns the value of the item with the specified key. If the key does not exist,
it inserts the key, with the specified value, and returns the value. Since a value for key 2 exists in the dictionary,
the output is ’Mary’—the value for the given key

setdefault() metodi berilgan kalitga (key) mos keluvchi elementning qiymatini qaytaradi.
Agar bu kalit mavjud bo‘lmasa, u kalitni berilgan qiymat bilan lug‘atga qo‘shadi va shu qiymatni qaytaradi.
Kalit 2 uchun qiymat lug‘atda allaqachon mavjud bo‘lgani sababli, natija 'Mary' bo‘ladi — ya’ni berilgan kalitga mos qiymat."""


# 8.2 Dictionary Initialization

d = {bool(-1): {0},
True : {0, 1},
1 : {0, 1, 2},
(2,) : {0, 1, 2, 3}}
print(len(d))

'''In a dictionary, all keys are unique. If you add a dictionary entry with a key that already exists, you’ll simply update the entry.
In the puzzle, you add the entry bool(-1): 0 to the dictionary. In other words, the non-zero key bool(-1)
evaluates to 1 (which is the representation of the Boolean value True) and the next entry updates the first one.
The third entry 1 also updates the existing one. So, after the first three entries, the dictionary contains
only one entry 1: 0, 1, 2. Only the last entry has a different key, so you create a new entry. The final
dictionary has only two entries. The result of len(d) is, therefore, 2.'''

'''Lug‘atda (dictionary) barcha kalitlar noyobdir.
Agar siz allaqachon mavjud bo‘lgan kalit bilan yangi element qo‘shsangiz, Python shunchaki mavjud yozuvni yangilaydi.
Misolda siz lug‘atga bool(-1): 0 elementini qo‘shasiz. Boshqacha aytganda, nolga teng bo‘lmagan kalit bool(-1) 1 ga 
teng bo‘ladi (bu Boolean qiymat True ni ifodalaydi) va keyingi qo‘shilgan element birinchisini yangilaydi. Uchinchi element
1 ham mavjud elementni yangilaydi. Shunday qilib, birinchi uchta element qo‘shilgandan keyin, lug‘atda faqat bitta yozuv qoladi:
1: 0, 1, 2. Faqat oxirgi elementda boshqa kalit mavjud bo‘lgani uchun, yangi yozuv yaratiladi.
Oxirgi lug‘atda faqat ikki yozuv mavjud. Shuning uchun len(d) ning natijasi 2 bo‘ladi.'''
