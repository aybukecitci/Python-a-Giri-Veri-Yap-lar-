###############################################
# Python Alıştırmalar
###############################################

###############################################
# GÖREV 1: Veri yapılarının tipleriniz inceleyiniz.
###############################################


x = 8
type(x)


y = 3.2
type(y)

x * y

int(x * y)

dir(str)

z = 8j + 18

type(z)

a = "Hello World"

type(a)


b = True
type(b)


c = 23 < 22
type(c)



l = [1, 2, 3, 4,"String",3.2, False]

type(l)


d = {"Name": "Jake",
     "Age": [27,56],
     "Adress": "Downtown"}

type(d)


t = ("Machine Learning", "Data Science")

type(t)


s = {"Python", "Machine Learning", "Data Science","Python"}

type(s)



###############################################
# GÖREV 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.
###############################################

text = "The goal is to turn data into information, and information into insight."


text.replace(".", " ").replace(",", " ").upper().split()


###############################################
# GÖREV 3: Verilen liste için aşağıdaki görevleri yapınız.
###############################################

lst = ["D","A","T","A","S","C","I","E","N","C","E"]


# Adım 1: Verilen listenin eleman sayısına bakın.

len(lst)

# Adım 2: Sıfırıncı ve onuncu index'teki elemanları çağırın.


print(lst[0], lst[10])


# Adım 3: Verilen liste üzerinden ["D","A","T","A"] listesi oluşturun.

range(len(lst))
lst[0:4]

# Adım 4: Sekizinci index'teki elemanı silin.


lst.pop(8)


# Adım 5: Yeni bir eleman ekleyin.

lst.append("AYB")

print(lst)


# Adım 6: Sekizinci index'e  "N" elemanını tekrar ekleyin.

lst.insert(8, "N")
print(lst)


###############################################
# GÖREV 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
###############################################

dict = {'Christian': ["America",18],
        'Daisy':["England",12],
        'Antonio':["Spain",22],
        'Dante':["Italy",25]}


# Adım 1: Key değerlerine erişiniz.

print(dict.keys())


# Adım 2: Value'lara erişiniz.

print(dict.values())


# Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.

dict = {'Christian': ["America",18],
        'Daisy':["England",12],
        'Antonio':["Spain",22],
        'Dante':["Italy",25]}



dict.update({'Daisy':["England",13]})
print(dict)


dict["Daisy"][1] = 13
print(dict)


# Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.


dict.update({"Ahmet": ["Turkey",24]})
print(dict)


# Adım 5: Antonio'yu dictionary'den siliniz.

dict.pop("Antonio")
print(dict)



###############################################
# GÖREV 5: Arguman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atıyan ve bu listeleri return eden fonskiyon yazınız.
###############################################



#Alternatif1

l = [2, 13, 18, 93, 22]


def seperate(l):
    odd = [x for x in l if x % 2 != 0]

    even = [x for x in l if x % 2 == 0]

    return odd, even


odds, evens = seperate(l)

print("odd numbers:", odds)

print("evens number:", evens)



#Alternatif2
l = [2, 13, 18, 93, 22]

def cift_ve_tek_ayir(l):
    cift_sayi = []

    tek_sayi = []

    for new_l in l:

        if new_l % 2 == 0:

            cift_sayi.append(new_l)

        else:

            tek_sayi.append(new_l)

    return cift_sayi, tek_sayi


cift_sayi, tek_sayi = cift_ve_tek_ayir(l)

print("Çift Sayılar:", cift_sayi)

print("Tek Sayılar:", tek_sayi)





###############################################
# GÖREV 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri bulunmaktadır.
# Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de tıp fakültesi öğrenci sırasına aittir.
# Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.
###############################################


ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

for i, student in enumerate(ogrenciler, start=1):
    faculty = "Engineering Department" if i <= 3 else "Medical School"

    index = i if i <= 3 else i - 3

    print(f"{faculty} {index} . student: {student}")


# OR -----------


def list_students(ogrenciler):
    for i, student in enumerate(ogrenciler, start=1):
        faculty = "Engineering Department" if i <= 3 else "Medical School"

        index = i if i <= 3 else i - 3

        print(f"{faculty} {index} . student: {student}")


list_students(ogrenciler)
#fstring araştır!!!!!!!!!!!

#Alternatif çözüm1

ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

for i, isim in enumerate(ogrenciler, 1):

    if i < 4:

        print("Mühendislik Fakültesi {}. Öğrenci: {}".format(i, isim))

    else:

        print("Tıp Fakültesi {}. Öğrenci: {}".format((i - 3), isim))



#Alternatif2

for i, ogrenci in enumerate(ogrenciler[:3], 1):
    print(f"Mühendislik Fakültesi {i}. öğrenci: {ogrenci}")

for i, ogrenci in enumerate(ogrenciler[3:], 1):
    print(f"Tıp Fakültesi {i}. öğrenci: {ogrenci}")




#Alternatif 3
for i, ogr in enumerate(ogrenciler, start = 1):

    if i < 4:

        faculty = "Engineer Faculty"

        index = i

        student = ogr

    else:

        faculty = "Medical Faculty"

        index = i - 3

        student = ogr

    print(f" {faculty} {index} . student : {student}")




#f-Strings biçimlendirilmiş dizeler olarak geçer. dışarıdan string dışında bir şey yazılacağı zaman kullanılır bunlar ifadeler veya değişkenler olabilir.  örnek olarak  ;

#ingilizce = 78
#matematik = 56
#türkçe = 85

#print(f"ders notları toplamı  {ingilizce + matematik + türkçe } puandır")

###############################################
# GÖREV 7: Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.
###############################################



ders_kodu = ["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]


for i in range(len(ders_kodu)):
    print(f"Kredisi {kredi[i]} olan {ders_kodu[i]} dersinin kontenjanı {kontenjan[i]} kişidir.")


###############################################
# GÖREV 8: Aşağıda 2 adet set verilmiştir.
# Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.
###############################################

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

#alternatif çözüm 1

def def_set(arg1, arg2):
    a = arg1 - arg2

    b = arg1 == arg2

    if b == True:

        print(arg2)

    elif a != set():

        print(arg2)

    else:

        print(arg2 - arg1)


def_set(kume1, kume2

#alternatif çözüm 2

def kümeler(set1, set2):

    for sets in (set1, set2):

        if set1.issuperset(set2):

            print(set1.intersection(set2))

        else:

            print(set1.symmetric_difference(set2))

    return set1, set2




