# capitalize()  Converts the first character to upper case.
# (matn ichidagi birinchi harfni katta qiladi, qolgan barcha harflarni kichik harfga o‘zgartiradi.)

ism_familiya = "Gulchiroy Raximboyeva"
print(ism_familiya.capitalize())
shahar = "toshkent shahri"
print(shahar.capitalize())
fanlar = "matematika,Ingliz Tili,Tarix,Psixologiya"
print(fanlar.capitalize())

# casefold()  Converts string into lower case
# (matndagi barcha harflarni kichik harfga o‘zgartiradi.)

fasl = "Bahor,Yoz,Kuz,Qish"
print(fasl.casefold())
fakt = "BAXT KICHIK NARSALARDAN BOSHLANADI"
print(fakt.casefold())
ziyo_uz = "SEVGI bu dunyoning eng Go'zal tuyg'usidir💖"
print(ziyo_uz.casefold())

# center()  Returns a centered string
# (matnni markazga joylashtirish uchun ishlatiladi.)

meva = "olma"
print(meva.center(20))
otkan_kunlar = "Muhabbat insonni tirik qiluvchi, lekin azob bilan yashantiruvchi tuyg'udir"
print(otkan_kunlar.center(25))
kecha_va_kunduz = "Erkinlik bu nafaqat tananing balki fikrning ham ozodligidir"
print(kecha_va_kunduz.center(70))

# count()  Returns the number of times a specified value occurs in a string
# (matnda ma’lum bir belgi yoki so‘z necha marta uchraganini hisoblab beradi.)

Oybek = "Buyuk inson o'z xalqining orzusi bilan yashaydi"
x = Oybek.count("odam")
print(x)
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)
Said_Ahmad = "Baxt hech qachon uzoqda emas, u sening yuragingda yashaydi"
x = Said_Ahmad.count("yashaydi")
print(x)

# encode()  Returns an encoded version of the string
# (matn ni baytlarga  o‘zgartiradi.)

Otkir_Hoshimov = "Hayot ikki eshik orasidagi qisqa yo'l"
print(Otkir_Hoshimov.encode())
Erkin_Vohidov = "Tilini sevgan el o'zini yo'qotmaydi"
print(Erkin_Vohidov.encode())
Hamid_Olimjon = "Sevgi yurakning eng go'zal isyoni"
print(Hamid_Olimjon.encode())

# endswith()  Returns true if the string ends with the specified value
# (matn ma’lum bir so‘z yoki belgilar bilan tugaydimi yo‘qmi — shuni tekshiradi.)

txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)
txt = "Ba'zan jim turish ham katta javob bo'ladi"
x = txt.endswith(".")
print(x)
txt = "kulgiga o'rangan so'z ham. ba'zan yurakni og'ritadi"
x = txt.endswith("?")
print(x)

# expandtabs()  Sets the tab size of the string
# (matn ichidagi \t (tab) belgilarini bo‘sh joylarga  almashtiradi)

txt = "H\te\tl\tl\to"
x = txt.expandtabs(4)
print(x)
txt = "M\ta\tt\te\tm\ta\tt\ti\tk\ta"
x = txt.expandtabs(1)
print(x)
txt = "i\tn\ts\to\tn"
x = txt.expandtabs(2)
print(x)

# find()  Searches the string for a specified value and returns the position of where it was found
# (matn ichida ma’lum bir so‘z yoki belgi qayerda (nechanchi indeksda) joylashganini topadi.Agar topilmasa — -1 qiymatini qaytaradi.)

txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)
txt = "Ba'zi orzular faqat tushda amalga oshadi"
x = txt.find("orzular")
print(x)
x = "Zulm o'z soyasidan ham qo'rqadi"
x = txt.find("inson")
print(x)

# format()  Formats specified values in a string
# (matn ichiga qiymatlarni joylashtirish uchun ishlatiladi.Ya’ni, {} joylariga qiymatlar kiritiladi — xuddi shablon kabi ishlaydi.)

txt = "For only {price:.2f} dollars!"
print(txt.format(price=49))
txt = "Salom Dunyo {price: .2f}"
print(txt.format(price=100))
txt = "Umumiy narx {price:.3f} dollar!"
print(txt.format(price=100))

# format_map()  Formats specified values from a dictionary in a string
# (Matn ichidagi {} joylariga qiymatlarni lug‘atdan olib joylashtiradi.Ya’ni, {kalit} o‘rniga lug‘atdagi qiymat yoziladi.)

myvar = {"name": "Safiya", "age": 20}
txt = "Happy birthday {name} you are now on level {age}!"
print(txt.format_map(myvar))
malumot = {'ism': 'Gulchiroy', 'yosh': 19}
xabar = "Mening ismim {ism}, yoshim {yosh}da.".format_map(malumot)
print(xabar)
kitob = {'nomi': 'Otkan kunlar', 'muallif': 'Abdulla Qodiriy', 'yil': 1926}
matn = "{nomi} asari muallifi {muallif}, {yil}-yilda yozilgan.".format_map(kitob)
print(matn)

# index()  Searches the string for a specified value and returns the position of where it was found
# (Matndan ma’lum bir belgi yoki so‘zni qidiradi va birinchi uchragan o‘rnining indeksini (raqamini) qaytaradi.)

txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)
txt = "Sadoqat vaqt bilan o'lchanmaydigan tuyg'u"
x = txt.index("vaqt")
print(x)
txt = "Insonning qadri uning so'zida bilinadi"
x = txt.index("uning")
print(x)

# isalnum()  Returns True if all characters in the string are alphanumeric
# (Matndagi barcha belgilar agar harf yoki raqam bo‘lsa — True (rost) qaytaradi,aks holda — False (yolg‘on) qaytaradi.)

txt = "Company"
x = txt.isalnum()
print(x)
txt = "Python123"
x = txt.isalnum()
print(x)
txt = "Matematika-"
x = txt.isalnum()
print(x)

# isalpha()  Returns True if all characters in the string are in the alphabet
# (matnda faqat harflar bor-yo‘qligini tekshiradi.Agar matndagi barcha belgilar faqat harf bo‘lsa — True,aks holda — False qaytaradi.)

txt = "CompanyX"
x = txt.isalpha()
print(x)
txt = "python123"
x = txt.isalpha()
print(x)
txt = "Tarix darsi"
x = txt.isalpha()
print(x)

# isascii()  Returns True if all characters in the string are ascii characters
# (matndagi barcha belgilar ASCII (ya’ni oddiy inglizcha belgilar) ekanligini tekshiradi.)

txt = "python pycharm"
x = txt.isascii()
print(x)
txt = "Salom"
x = txt.isascii()
print(x)
txt = "🥰"
x = txt.isascii()
print(x)

# isdecimal()  Returns True if all characters in the string are decimals
# (matndagi barcha belgilar o‘nlik raqamlar (0–9) ekanligini tekshiradi.)

txt = "hello world"
x = txt.isdecimal()
print(x)
txt = "Matematika"
x = txt.isdecimal()
print(x)
txt = "Python111"
x = txt.isdecimal()
print(x)

# isdigit()  Returns True if all characters in the string are digits
# (matndagi barcha belgilar raqam (digit) ekanligini tekshiradi.)

txt = "Xorazm"
x = txt.isdigit()
print(x)
txt = "123456789"
x = txt.isdigit()
print(x)
txt = "12.87"
x = txt.isdigit()
print(x)

# isidentifier()  Returns True if the string is an identifier
# (matn (string) Python’da o‘zgaruvchi nomi sifatida ishlatilishi mumkinmi yoki yo‘qligini tekshiradi.)

txt = "string"
x = txt.isidentifier()
print(x)
txt = "veriable"
x = txt.isidentifier()
print(x)
txt = "Matematika__ 123"
x = txt.isidentifier()
print(x)

# islower()  Returns True if all characters in the string are lower case
# (Agar matndagi barcha harf belgilar kichik (a–z) bo‘lsa — True,aks holda — False.)

txt = "Tarix Fani"
x = txt.islower()
print(x)
txt = "kompyuter"
x = txt.islower()
print(x)
txt = "123456789"
x = txt.islower()
print(x)

# isnumeric()  Returns True if all characters in the string are numeric
# (matndagi barcha belgilar raqam (numeric) bo‘lsa True, aks holda False qaytaradi.U raqamlar, superscript belgilar (², ³), fraktsiyalar (½), va boshqa matematik raqamlarni ham tan oladi.)

txt = "1234567890"
x = txt.isnumeric()
print(x)
txt = "matematika"
x = txt.isnumeric()
print(x)
txt = "python123"
x = txt.isnumeric()
print(x)

# isprintable()  Returns True if all characters in the string are printable
# (matndagi barcha belgilar chop etiladigan (ko‘rinadigan) belgilar ekanligini tekshiradi.)

txt = "Hello, World!"
x = txt.isprintable()
print(x)
txt = "\nHello world"
x = txt.isprintable()
print(x)
txt = "12345"
x = txt.isprintable()
print(x)

# isspace()  Returns True if all characters in the string are whitespaces
# (matndagi barcha belgilar bo‘sh joy yoki oqim belgisi (whitespace) ekanligini tekshiradi.)

txt = "dasturchi"
x = txt.isspace()
print(x)
txt = "   "
x = txt.isspace()
print(x)
txt = "1233345342534"
x = txt.isspace()
print(x)

# istitle()  Returns True if the string follows the rules of a title
# (matndagi har bir so‘z bosh harfi katta va qolgan harflari kichik ekanligini tekshiradi.)

txt = "Salom Dunyo"
x = txt.istitle()
print(x)
txt = "Salom dunyo"
x = txt.istitle()
print(x)
txt = "Assalomu alaykum"
x = txt.istitle()
print(x)

# isupper()  Returns True if all characters in the string are upper case
# (matndagi barcha harflar katta ekanligini tekshiradi.)

txt = "MATEMATIKA"
x = txt.isupper()
print(x)
txt = "matematika"
x = txt.isupper()
print(x)
txt = "HELLO123"
x = txt.isupper()
print(x)

# join()  Joins the elements of an iterable to the end of the string
# (U ro‘yxat (list) yoki boshqa iterable ichidagi elementlarni belgilangan ajratuvchi bilan birlashtiradi va yangi string hosil qiladi.)

txt = ("Python", "Pycharm")
x = "#".join(txt)
print(x)
txt = ("15", "10", "2025")
x = "-".join(txt)
print(x)
txt = ("14", "07")
x = ".".join(txt)
print(x)

# ljust()  Returns a left justified version of the string
# (stringni chapga tekislab, kerak bo‘lsa o‘ng tarafini to‘ldiradi.)

txt = "HelloWorld"
x = txt.ljust(20)
print(x, "*")
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")
txt = "Python"
x = txt.ljust(10)
print(x, "-")

# lower()  Converts a string into lower case
# (matndagi barcha harflarni kichik harfga (a–z) aylantiradi.)

txt = "PYTHON"
x = txt.lower()
print(x)
txt = "TELEFON"
x = txt.lower()
print(x)
txt = "123ABC"
x = txt.lower()
print(x)

# lstrip()  Returns a left trim version of the string
# (stringning boshidan (chapidan) bo‘sh joy yoki belgilarning o‘chirilishini ta’minlaydi.Agar belgilar ko‘rsatilsa, faqat shu belgilar chap tomondan o‘chiriladi.)

txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")
txt = "    hello"
x = txt.lstrip()
print(x)
txt = "###Python###"
x = txt.lstrip("#")
print(x)

# maketrans()  Returns a translation table to be used in translations
# (matndagi belgilarni avtomatik almashtirish uchun ishlatiladi.)
txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))
txt = "Go'zal shaxar"
mytable = str.maketrans("x", "h")
print(txt.translate(mytable))
txt = "Hayrli tong"
mytable = str.maketrans("o", "u", "g")
print(txt.translate(mytable))

# partition()  Returns a tuple where the string is parted into three parts

txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)
txt = "Moviy dengiz moviy osmon"
x = txt.partition("Moviy")
print(x)
txt = "Moviy dengiz moviy osmon"
x = txt.partition("osmon")
print(x)

# replace()  Returns a string where a specified value is replaced with a specified valuebu
# (matn ichida qidirilayotgan substringning oxirgi uchrashuvini topadi.Agar topilsa — indeksni qaytaradi,topilmasa — -1 qaytaradi.)

txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)
txt = "Uning so'zlari meni hayratga soldi"
x = txt.replace("Uning", "Gulining")
print(x)
txt = "Umid qilsang, hatto qorong'ulikda ham yorug'lik topasan"
x = txt.replace("yorug'lik", "nur")
print(x)

# rfind()  Searches the string for a specified value and returns the last position of where it was found
# (matndagi substringning oxirgi uchrashuvining indeksini qaytaradi)

txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)
txt = "Sevgi bu o'zingni unutib, boshqaga qalbingni berishdir"
x = txt.rfind("qalbingni")
print(x)
txt = "Millatni qalbi birlashtirsa hech narsa uni sindira olmaydi"
x = txt.rfind("uni")
print(x)

# rindex()  Searches the string for a specified value and returns the last position of where it was found
# (matndagi substringning oxirgi uchrashuvining indeksini qaytaradi.Agar substring topilmasa, xato (ValueError) chiqaradi — rfind() esa -1 qaytaradi)

txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)
txt = "Sevgi bu o'zingni unutib, boshqaga qalbingni berishdir"
x = txt.rindex("qalbingni")
print(x)
txt = "Millatni qalbi birlashtirsa hech narsa uni sindira olmaydi"
x = txt.rindex("uni")
print(x)

# rjust()  Returns a right justified version of the string
# (matnni berilgan uzunlikka teng qilib, chap tomondan bo‘sh joy (yoki belgi) bilan to‘ldiradi. Ya’ni matn o‘ng tomonda joylashadi.)

txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit.")
txt = " Haqiqiy do'st doimo yoningda bo'ladi"
x = txt.rjust(50)
print(x)
txt = "Do'stlik"
x = txt.rjust(40)
print(x, "eng qimmatli xazina")

# rpartition()  Returns a tuple where the string is parted into three parts
# (matnni oxirgi uchrashgan separator (bo‘luvchi) bo‘yicha uch qismga bo‘ladi)

txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)
txt = "Kim namozni to'liq ado etsa, qalbi tinch bo'ladi 'hadisdan'"
x = txt.rpartition("qalbi")
print(x)
txt = "Ilm o'rganish orqali inson dunyoni ham oxiratni ham anglaydi"
x = txt.rpartition("Ilm o'rganish")
print(x
      )
# rsplit()  Splits the string at the specified separator, and returns a list
# (matnni o‘ng tomondan boshlab bo‘ladi, ya’ni oxiridan boshlab ajratadi.Natija sifatida ro‘yxat (list) qaytaradi.)

txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)
txt = "kutubxona, kitob, maktab"
x = txt.rsplit(" ,")
print(x)
txt = "kutubxona, kitob, maktab"
x = txt.rsplit("  .")
print(x)

# rstrip()  Returns a right trim version of the string
# (matnning o‘ng chetidan (ya’ni oxiridan)bo‘sh joylar yoki ko‘rsatilgan belgilarni olib tashlaydi

txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")
txt = "taqvodir      "
x = txt.rstrip()
print("Bandaning eng yaxshi boyligi", x, "'hadisdan'")
txt = "     Chiroyli xulq"
x = txt.rstrip()
print(x, "odamni eng yuksak darajaga yetkazadi")

# split()  Splits the string at the specified separator, and returns a list
# (matnni (stringni) bo‘luvchi belgi (separator) orqali bo‘lib oladi va natijani ro‘yxat (list) ko‘rinishida qaytaradi.)

txt = "welcome to the jungle"
x = txt.split()
print(x)
txt = "oddiy hayotning kichik lahzalari ham qimmatli saboqlar beradi"
x = txt.split()
print(x)
txt = "Telefon kamerasi oldida tabassum qilganingda, dunyo yanada yorqinroq bo'ladi"
x = txt.split()
print(x)

# splitlines()  Splits the string at line breaks and returns a list
# (matnni yangi qator belgisi (\n) bo‘yicha bo‘lib, ro‘yxat (list) ko‘rinishida qaytaradi.)

txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)
txt = "Inson o'zini bilmasa, \ndunyoni ham to'liq anglay olmaydi"
x = txt.splitlines()
print(x)
txt = "\nInson o'z harakatlarini anglab yashasa, hayoti ham tartibli bo'ladi"
x = txt.splitlines()
print(x)

# startswith()  Returns true if the string starts with the specified value
# (bu metod matn ma’lum bir so‘z yoki belgidan boshlanganini tekshirish uchun ishlatiladi.)

txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)
txt = "Hamma o'qiyotgan kitobni o'qigim kelmaydi..."
x = txt.startswith("kitobni")
print(x)
txt = "Java Developer"
x = txt.startswith("Java")
print(x)

# strip()  Returns a trimmed version of the string
# (bu metod Python’da matnning boshida va oxiridagi keraksiz belgilarni (odatda bo‘sh joylarni) olib tashlash uchun ishlatiladi.)

txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")
txt = "Matematika"
x = txt.strip()
print(x, "fanidan misol ishlaymiz")
txt = "   kuz  "
x = txt.strip()
print(x, "fasli tugashiga ham oz qolyapti")

# swapcase()  Swaps cases, lower case becomes upper case and vice versa
# (matndagi har bir harfning katta-kichikligini teskarisiga o‘zgartiradi.)

txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)
txt = "kompyuter texnologiyalari"
x = txt.swapcase()
print(x)
txt = "kompYUTER texnologiyaLARI"
x = txt.swapcase()
print(x)

# title()  Converts the first character of each word to upper case
# (har bir so‘zning birinchi harfini katta, qolgan qismini kichik qilib yozadi.)

txt = "Welcome to my world"
x = txt.title()
print(x)
txt = "Har bir Odam O'zicha To'g'ri "
x = txt.title()
print(x)
txt = "ODAM SO'ZI BILAN EMAS, AMALI BILAN TANILADI"
x = txt.title()
print(x)

# translate()  Returns a translated string
# (matndagi belgilarni almashtirish yoki o‘chirish uchun ishlatiladi.)

# use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83: 80}
txt = "Hello Sam!"
print(txt.translate(mydict))

# upper()  Converts a string into upper case
# (matndagi barcha harflarni katta (BOSH) harfga aylantiradi.)

txt = "Hello my friends"
x = txt.upper()
print(x)
txt = "Muzaffarovna💖"
x = txt.upper()
print(x)
txt = "urganch davlat universiteti"
x = txt.upper()
print(x)

# zfill()  Fills the string with a specified number of 0 values at the beginning
# (bu metod matnning chap tomoniga nol (0) qo‘shib, uni berilgan uzunlikka yetkazadi.)

txt = "50"
x = txt.zfill(10)
print(x)
txt = "111"
x = txt.zfill(35)
print(x)
txt = "..."
x = txt.zfill(27)
print(x)

