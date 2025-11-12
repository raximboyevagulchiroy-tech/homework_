# Python Lists
List1 = ["telegram", "instagram", "facebook"]
print(List1)
List2 = ["informatika", "ingliz tili", "tarix"]
print(List2)

# Access Items
# Listdagi ma'lum elementni indeksi orqali olish
List1 = ["apple", "banana", "strawberry"]
print(List1[0])
List2 = ["apple", "banana", "strawberry"]
print(List2[-1])

# Change List Items
# List ichidagi biror qiymatni yangi qiymat bilan almashtirish
fruits = ["apple", "banana", "cherry", "orange", "strawberry"]
fruits[1:3] = ["kiwi", "mango"]
print(fruits)
sonlar = ["10000", "99999", "23456", "76543"]
sonlar[2:3] = ["4444","1111"]
print(sonlar)

# Add Lst Items
#Append - list oxiriga yana bitta yangi element qo'shadi
cities = ["Tashkent", "Samarkand", "Urgench"]
cities.append("Khiva")
print(cities)
# Insert - listga yangi elementni istalgan joyiga indeks bo'yicha qo'shadi
students = ["islom", "Umid", "Doston"]
students.insert(0, "Malika")
print(students)
# Extend - boshqa ro'yxatdagi barcha elementlarni olib, oxiriga qo'shib qo'yadi
animals = ["cat", "dog"]
animals.extend(["lion", "tiger"])
print(animals)

# Remove list items
colors = ["blue", "green", "red"]
colors.remove("blue")
print(colors)
colors = ["blue", "green", "red"]
colors.pop(1)
print(colors)
colors = ["blue", "green", "red"]
del colors[0]
print(colors)
colors = ["blue", "green", "red"]
colors.clear()
print(colors)

# Loop Lists
subjects = ["Math", "Physics", "Biology"]
for x in subjects:
  print(x)
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
  thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
  thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
