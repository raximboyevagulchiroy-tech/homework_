# # 1.
# def kopaytma(*sonlar):
#     natija = 1
#     for s in sonlar:
#         natija *= s
#     return natija
#
# print(kopaytma(2, 3, 4))
# print(kopaytma(5, 10))


# # 2.
# def talaba_info(ism, familiya, **malumotlar):
#     malumot = {
#         "ism": ism.title(),
#         "familiya": familiya.title()
#     }
#     malumot.update(malumotlar)
#     return malumot
#
# print(talaba_info("guli", "raximboyeva", yosh=19, kurs=2))
# print(talaba_info("islom", "otaboyev"))