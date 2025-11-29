# 1
class Mahsulot:
    def __init__(self, id, nomi, narxi, soni, reyting):
        self.id = id
        self.nomi = nomi
        self.narxi = narxi
        self.soni = soni
        self.reyting = reyting

    def get_info(self):
        return f"ID: {self.id}  \nNOMI: {self.nomi} \nNARXI: {self.soni} \nREYTING: {self.reyting}"

    def yangilangan_narxi(self, yangilangan_narxi):
        self.narxi = yangilangan_narxi


# 2
class Savat:
    def __init__(self):
        self.mahsulotlar = []
        self.umumiy_narx = 0

    def mahsulot_qoshish(self,mahsulot):
        self.mahsulotlar.append(mahsulot)
        self.hisobla()

    # def mahsulot_olib_tashlash(self):


    def tozalash(self):
        self.mahsulotlar = []
        self.umumiy_narx = 0

    def hisobla(self):
        self.umumiy_narx =sum( mahsulot for mahsulot in self.mahsulotlar)

    def boshmi(self):
        return len(self.mahsulotlar) == 0

    def tekshirish(self):
        if self.boshmi():
            return "Savat bo'sh"
        else:
            return "Savat bo'sh emas"


# 3
class Buyurtma:
    def __init__(self, id, status, savat, yaratiluv_vaqti, jami_narx):
        self.id = id
        self.status = status
        self.savat = savat
        self.yaratiluv_vaqti = yaratiluv_vaqti
        self.jami_narx = jami_narx

    # def buyurtmani_tasdiqlash(self):

    def yangilash(self):
        self.status = self.status

    def get_info(self):
        return f"ID: {self.id} \nStatus: {self.status} \nSavat: {self.savat} \nVaqt: {self.yaratiluv_vaqti}\nJami narx: {self.jami_narx}"


# 4
class Foydalanuvchi:
    def __init__(self, id, ism, email,savat,buyurtmalar):
        self.id = id
        self.ism = ism
        self.email = email
        self.savat = savat
        self.buyurtmalar = buyurtmalar
        self.savat = savat()
        self.buyurtmalar = []

    def mahsulot_qoshish(self,mahsulot):
        self.buyurtmalar.append(mahsulot)

    def mahsulot_olib_tashlash(self, mahsulot):
        self.buyurtmalar.remove(mahsulot)

    # def buyurtma_yaratish(self):
    #     self.buyurtmalar = []


    def buyurtma_tarixi(self):
        if not self.buyurtmalar:
            return "Buyurtmalar tarixi bo'sh."
        matn = "Buyurtmalar tarixi:\n"
        for buyurtma in self.buyurtmalar:
            matn += buyurtma.malumot() + "\n"
        return matn


 # 5
class Dokon:
    def __init__(self, nomi, mahsulotlar, foydalanuvchilar):
        self.nomi = nomi
        self.mahsulotlar = mahsulotlar
        self.foydalanuvchilar = foydalanuvchilar
        self.mahsulotlar = []
        self.foydalanuvchilar = []

    def mahsulot_qoshish(self,mahsulot):
        self.mahsulotlar.append(mahsulot)

    def foydalanuvchi_qoshish(self, foydalanuvchi):
        self.foydalanuvchilar.append(foydalanuvchi)

    # def mahsulot_qidirish(self, mahsulot_id):


    # def yuqori_reytingli(self):


    def sotilgan_hisobot(self):
        if not self.mahsulotlar:
            return "Hali hech narsa sotilmagan."
        matn = "Sotilgan mahsulotlar:\n"
        for m in self.mahsulotlar:
            matn += m.malumot() + "\n"
        return matn




m1 = Mahsulot(1, "Noutbuk", 550, 10, 4.8)
m2 = Mahsulot(2, "Telefon", 300, 15, 4.5)
m3 = Mahsulot(3, "Kompyuter sichqoncha", 20, 50, 4.1)
