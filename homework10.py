# # 1.
# davlatlar ={
#     "O'zbekiston":{
#             "poytaxt": "Toshkent",
#             "hudud": "448978 kv.km",
#             "aholisi": "33 000 000",
#             "pul_birligi": "so'm"
#          },
#     "Rossiya":{
#             "poytaxt": "Moskva",
#             "hudud": "17 098 246 kv.km",
#             "aholisi": "144 000 000",
#             "pul_birligi": "rubl"
#         },
#     "AQSH": {
#             "poytaxt": "Vashington",
#             "hudud": "9 631 418 kv.km",
#             "aholisi": "327 000 000",
#             "pul_birligi": "dollar"
#         },
#         "Malayziya": {
#             "poytaxt": "Kuala-Lumpur",
#             "hudud": "329 750 kv.km",
#             "aholisi": "25 000 000",
#             "pul_birligi": "ringgit"
#         },
#     }
# for ism, info in davlatlar.items():
#     print(f"\n{ism.title()}ning poytaxti {info['poytaxt'].title()}\n"
#           f"Hududi: {info['hudud']}\n"
#           f"Aholisi: {info["aholisi"]}\n"
#           f"Pul Birligi: {info['pul_birligi']}")
#
# # 2.

davlatlar ={
    "O'zbekiston":{
            "poytaxt": "Toshkent",
            "hudud": "448978 kv.km",
            "aholisi": "33 000 000",
            "pul_birligi": "so'm"
         },
    "Rossiya":{
            "poytaxt": "Moskva",
            "hudud": "17 098 246 kv.km",
            "aholisi": "144 000 000",
            "pul_birligi": "rubl"
        },
    "AQSH": {
            "poytaxt": "Vashington",
            "hudud": "9 631 418 kv.km",
            "aholisi": "327 000 000",
            "pul_birligi": "dollar"
        },
        "Malayziya": {
            "poytaxt": "Kuala-Lumpur",
            "hudud": "329 750 kv.km",
            "aholisi": "25 000 000",
            "pul_birligi": "ringgit"
        },
    }
nom = input("Davlat nomini kiriting: ").capitalize()
if nom in davlatlar.keys():
    print(f"\n{nom}ning poytaxti {davlatlar[nom]['poytaxt']}")
    print(f"Hududi: {davlatlar[nom]['hudud']}")
    print(f"Aholisi: {davlatlar[nom]['aholisi']}")
    print(f"Pul birligi: {davlatlar[nom]['pul_birligi']}")
else:
    print("Bizda bu davlat haqida ma'lumot mavjud emas")



