# Örnek 1: Ekranda 5 defa isim yazdıran örnek.


for i in range(5):
    print("Ömer")                   # / Ömer Ömer Ömer Ömer Ömer

# Örnek 2: Kullanıcının Girdiği metni ekranda 5 defa yazdıran Python For Döngüsü Örneği:

metin = input("Lüfen Bir Metin Giriniz : ")

for i in range(5):
    print(metin)                    # input("metin")  / metin , metin , metin , metin , metin

# Örnek 3: 10′ a kadar olan çift sayıları listeleyen Python For Döngüsü Örneği

for i in range(0,10):
    if i %2 == 0:
        print(i)
    else: 
        continue                    # / 0 2 4 6 8 


# Örnek 4:  Kullanıcının girdiği 2 sayı arasındaki sayıları listeleyen Python For Döngüsü Örneği

sayi1 = int(input("1.sayi : "))
sayi2 = int(input("2.sayi : "))


for i in range(sayi1,sayi2+1):
    print(i)                        # / 2 3 4 5


# Örnek 5: kullanıcının girdiği 2 sayı arasındaki sayıların toplamını bulan Python For Döngüsü Örneği:

sayi1 = int(input("1.sayi : "))
sayi2 = int(input("2.sayi : "))
toplam=0


for i in range(sayi1,sayi2+1):
    toplam+=i
print("{} ile {} arasındaki sayıalrın tolamı {} eder." .format(sayi1,sayi2,toplam))     # / input(sayi1) ile input(sayi2) arasındaki sayıalrın tolamı xx eder.


# Örnek 6: kullanıcının girdiği sayının faktoriyelini alan Python For Döngüsü Örneği:

sayi1 = int(input("1.sayi : "))
fak = 1

for i in range(1,sayi1+1):
    fak*=i
print("{} sayısının faktörüyeli {} dir.".format(sayi1,fak))                     # / input(sayi1) sayısının faktörüyeli xxx dir.


# Örnek 7: Kullanıcının girdiği sayının asal sayı olup olmadığını kontrol eden Python For Döngüsü Örneği

sayi = int(input("Lütfen bir sayi giriniz : "))
sayac=0
for i in range(2,sayi+1):
    if sayi %i ==0:
        sayac+=1
        break
if(sayac!=0):
    print("{} Sayı Asal Değil".format(sayi))
else:
    print("{} sayı asaldır.".format(sayi))

# Örnek 8: Çıktısı aşağıdaki gibi devam eden çarpım tablosunu iç içe döngü kurarak kodlayınız.
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# 1 x 4 = 4
# 1 x 5 = 5
# 1 x 6 = 6
# 1 x 7 = 7
# 1 x 8 = 8
# 1 x 9 = 9
# 1 x 10 = 10

# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 2 x 4 = 8
# 2 x 5 = 10

for i in range(1,11):
    for j in range(1,11):
        print("{} x {} = {}".format(i,j,i*j))
    print("\n")    

# Çıktısı :                                              
# / 1 x 1 = 1
# / 1 x 2 = 2
# / 1 x 3 = 3
# / 1 x 4 = 4
# / 1 x 5 = 5
# / 1 x 6 = 6
# / 1 x 7 = 7
# / 1 x 8 = 8
# / 1 x 9 = 9
# / 1 x 10 = 10


# / 2 x 1 = 2
# / 2 x 2 = 4
# / 2 x 3 = 6
# / 2 x 4 = 8
# / 2 x 5 = 10
# / 2 x 6 = 12
# / 2 x 7 = 14
# / 2 x 8 = 16
# / 2 x 9 = 18
# / 2 x 10 = 20


# örnekler : 

sayilar = [1,3,5,7,9,12,19,21]


# # 1- Sayilar listesindeki hangi sayılar 3' ün katıdır ?

# for i in sayilar:
#     if i%3==0:
#         print(i)                            # / 3 9 12 21 


# 2- Sayilar listesinde sayıların toplamı kaçtır ?

toplam=0

for i in sayilar:
    toplam+=i
print(toplam)                           # / 77 


# 3- Sayilar listesindeki tek sayıların karesini alınız.

for i in sayilar:
    if i %2!=0:
        print(i*i)                  # / 1 9 25 49 81 361 441 
    

# 4- Şehirlerden hangileri en fazla 5 karakterlidir ?

sehirler = ["Kocaeli" , "İstanbul" , "Ankara" , "İzmir" , "Rize"]

for i in sehirler:
    if(len(i) <= 5):
       print(i)
    else:
        continue                    # / İzmir , Rize


# 5- Ürünlerin fiyatları toplamı nedir ?

urunler = [
  {'name':'samsung S6', 'price': '3000' },
  {'name':'samsung S7', 'price': '4000' },
  {'name':'samsung S8', 'price': '5000' },
  {'name':'samsung S9', 'price': '6000' },
  {'name':'samsung S10', 'price': '7000' }
]

toplam = 0

for i in urunler:
    fiyat = int(i["price"])
    toplam+=fiyat
print("toplam ürün fiyatı : {} ".format(toplam))                # / toplam ürün fiyatı : 25000

# 6- Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz ?

for i in urunler:
    fiyat = int(i["price"])
    if fiyat <= 5000:
        print(i["name"])
