# """renge() - sonli oraliq shakklantirins uchun funksiya """
# sonlar1 = list(range(-10,11))
# sonlar2 = list(range(2 ,21, 2))
# print(sonlar1)
# print(sonlar2)

# toq = list(range(4, 30, 2))
# print(toq)

# """ro'yxatdan nusxa olish"""
# son1 = list(range(50,100))
# print(son1)
# son2 = son1[30: ]
# print(son1)

# """ .sort() - ro'yxatni alifbo tartibida tartiblaydi"""
# name1 = ["Ali", "Aziz", "Sarvar"]
# print(name1)
# name1.sort()
# print(name1)
# name1.sort(reverse=True)
# print(name1)

# """sortred() - ro'yxatni  bir marta alifbo boyicha tartiblaydi"""
# name2 = ["Xoji", "Axmad", "Dovud"]
# print(name2)
# print(sorted(name2)) # to'g'ri tartibda
# print(sorted(name2, reverse=True)) # teskari tartibda

# """reverse() - royxatni boshini va oxirini aylantrib beradi """
# country = ["USA", "UZB", "RUS"]
# print(country)
# country.reverse() # ro'yxatni boshini va oxirini aylantirilg
# print(country)

# """max(), min(), sum()"""
# print(max(son1))
# print(min(son1))
# print(sum(son1))

# number = [55,32,434,-123,0,43,76,1,-23]
# number.sort()
# print(number)
# print(f"Ro'yxatdagi eng kata son {max(number)}, eng kichigi {min(number)}")

# """1-mashq"""
# countries = ["Ispaniya", "Amerika", "Uzbekistan", "Britaniya", "Portugaliya", "Germaniya", "Fransiya", "Rossiya"]
# print(countries)
# print(len(countries))
# print(sorted(countries))
# print(sorted(countries, reverse=True))
# print(countries)

# countries.reverse()
# print(countries)

# countries.sort()
# print(countries)

# """2-mashq"""
# a = list(range(120, 1200, 2))
# print(a)
# print(sum(a))
# print(max(a)-min(a))
# print(len(a))
# print(a[:20])
# print(a[260:280])
# print(a[520:])

# """3-mashq"""
# name = [ "Olim","Ali","Momin","Malika","Kamola"]
# b = name.copy()
# print(b)

# del b[1]
# print(b)

# b.append("Axror")
# b.append("Aziz")
# print(b)
# print(name)

# """ if-else """ #IF ELSE OPERATORI
# a = 4
# b = 2
# if a > b:
#     print(f"{a} > {b}")
# else:
#     print(f"{a} < {b}")

# "=="
# ismlar = [ "Olim","Ali","Momin","Malika","Kamola"]
# for ism in ismlar:
#     if ism == "Ali":
#         print(f"Salom {ism}, sizda yangi xabar bor")
#     else:
#         print(f"Salom {ism}")


# "!="
# for ism in ismlar:
#     if ism != "Ali":
#         print(f"Salom {ism}, Ali qani")
#     else:
#         print(f"Salom {ism}")

# """ elif """
# sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for son in sonlar:
#     if son < 5:
#         print(f"{son} 5dan kichik")
#     elif son == 5:
#         print(f"{son} 5ga teng")
#     else:
#         print(f"{son} 5dan katta ")
"""
== teng bolsa
=! teng bolmasa
> katta bolsa
< kichik bolsa
<= kata yoki teng bolsa
>= kichik yoki teng bolsa
or yoki
and va
"""

# """1-mashq"""
# s2 = int(input("1-sonni kiriting: "))
# s1 = int(input("2-sonni kiriting: "))

# if s1 > s2:
#     print(f"{s1} > {s2}")
# elif s1 == s2:
#     print(f"{s1} = {s2}")
# else:
#     print(f"{s1} < {s2}")



# """2-mashq"""
# ismlar = [ "Olim", "Ali", "Momin", "Kamron", "Malika", "Kamola"]
# for ism in ismlar:
#     if ism == "Kamron" or ism == "Momin":
#         print(f"Salom {ism} ahvollaring yaxshimi")
#     else:
#         print(f"Salom {ism}")


# """3-mashq"""
# mevalar = ["olma", "gilos", "tarvuz", "qovun",  "olcha", "nok", "anor", "shaftoli"]
# for m in mevalar:
#     if m == "tarvuz" or m == "qovun":
#         print(m.upper())
#     else:
#         print(m.title())

# """4-mashq"""
# number = list(range(205,2024))
# for n in number:
#     if n < 1000:
#         print(n**3)
#     elif n > 1500:
#         print(n-3)

# """ or va and """
# sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for son in sonlar:
#     if son < 5 or son > 5:
#         print(f"{son} 5ga teng emas")

# son = int(input("Son kiriting: "))
# 1-usul
# if son > 0:
#     print(f"{son} musbat")
#     if son%2 == 0:
#         print(f"{son} juft")
#     else:
#         print(f"{son} toq")
# elif son < 0:
#     print(f"{son} manfiy")
#     if son%2 == 0:
#         print(f"{son} juft")
#     else:
#         print(f"{son} toq")

# 2-usul
# if son%2 == 0 and son > 0:
#     print(f"{son} juft va manfiy")
# elif son%2 == 1 and son > 0:
#     print(f"{son} toq va manfiy")
# elif son%2 == 0 and son < 0:
#     print(f"{son} juft va musbat")
# elif son%2 == 1 and son < 0:
#     print(f"{son} toq va musbat")
# """1-mashq"""
# baho = int(input("Bahoni kiriting: "))
# if baho == 0:
#     print("JUDA YOMON")
# elif baho == 1:
#     print("YOMON")
# elif baho == 2:
#     print("QONIQARSIZ")
# elif baho == 3:
#     print("QONIQARLI")
# elif baho == 4:
#     print("YAXSHI")
# elif baho == 5:
#     print("ALO")
# else:
    # print("XATO")

# """"2-mashq"""
# from math import sqrt
# toq = list(range(201, 500, 2))
# for t in toq:
#     if t > 300:
#         print(f"{t}**4 = {t**4}")
#     if 350 < t < 400:
#         print(f"{t} ildizi = {sqrt(t)}")
#     if 420 < t < 480:
#         print(f" {t}/3.5 , 3xona yaxlid =  {round(t/3.5,3)}")
#     if 480 < t < 500:
#         print(f"{t}**6 = {t**6}")

# """3-mashq"""
# bal = int(input("Balinngizni kiriting: "))
# if 0 <= bal <= 40:
#     print("JUDA YOMON")
# elif 41 <= bal <= 60 :
#     print("QONIQARLI")
# elif 61 <= bal <=80 :
#     print("YAXSHI")
# elif 81 <= bal <= 99:
#     print("ALO")
# elif bal == 100:
#     print("TABRIKLAYMIZ SIZ GRANT YUTDINGIZ")
# else:
#     print("XATO")


# mahsulot = ["olma", "gilos", "tarvuz", "qovun",  "olcha", "nok", "anor", "shaftoli"]
# print(f"Dokonda quidagi mahsulotlar bor: {mahsulot}")
# bor = []
# yoq = []
# soni = int(input("Nechta mahsulot olasiz: "))
# for s in range(soni):
#     a = input(f"{s+1}-mahsulot nomi: ").lower().lstrip().rstrip().strip()
#     if a in mahsulot:
#         bor.append(a)
#     else:
#         yoq.append(a)
# print(f"Bizda bular bor: {bor}")
# print(f"Bizda bular yoq: {yoq}")


# """ Tub sonlar """
# max_son = int(input("Maksimal soni kriting: "))
# tub_sonlar = []
# for son in range(2, max_son+1)
#     tub = True

#     for i in range(2, son):
#         if son % i == 0:
#             tub = False
#             break
#         if tub:
#             tub_sonlar.append(son)
# print(tub_sonlar)

# "___"
# """1-mashq"""
# age = int(input("Yoshingizni kiriting: "))
# if 1 < age < 7 or 70 < age < 100:
#     print("Sizga bepul")
# elif 8 < age < 18:
#     print("Sizdan 5_000 so'm")
# elif 19 < age < 69:
#     print("Sizdan 10_000 so'm")
# elif  age < 0:
#     print("Faqat musbat yosh kiriting")
# else:
#     print("Xato")

# """3-mashq"""
# new_cars = ["totoya", "mazda", "hyundai", "gm", "kia"]
# for c in new_cars:
#     if c == "gm":
#         print(c.upper(), end=" ")
#     else:
#         print(c.title(), end=" ")

# """4-mashq"""
# from math import sqrt
# son = int(input("Son kiriting: "))
# if son > 0:
#     print(sqrt(son))
# elif son < 0:
#     print("Musbat son kiriting")

# """5-mashq"""
# parol1 = input("Parol kiriting: ")
# if len(parol1) >=8 :
#     parol2 = input("Parolni qayta kiriting: ")
#     if parol2 == parol1:
#         print("Parol muvafaqiyatli o'rnatildi")
#     elif parol2 != parol1:
#         print("Xatolik!", end=" ")
#         parol3 = input("Iltimos parolni boshqatdan kiting: ")
#         if parol3 == parol1:
#             print("Xush kelibsiz")
#         elif parol3 != parol1:
#             print("parol xato")
# elif len(parol1) < 8:
#     print("Faqatgina 8 xondan katta bolsin")

# """6-mashq"""
# ism = input("Ismingizni kiriting: ")
# jins = input("O'g'il yoki qiz: ").lower()
# yosh = int(input("Yoshingizni kiriting: "))
# if yosh == 15 and jins == "o'g'il":
#     print(f"{ism}, 9 blue sinfiga kirishingiz kerak")
# elif yosh == 15 and jins == "qiz":
#     print(f"{ism} 9 green sinfiga kirishingiz kerak")
# elif yosh != 15:
#     print("Biz faqat 15 yoshlilarni qabul qilamiz")

# "1"
# ism = input("Ismingizni kiriting: ")
# if bool(ism):
#     print("True")
# else:
#     print("Name erroe")




























