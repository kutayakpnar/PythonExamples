#Şimdi isterseniz 10'luk tabandaki bir sayıyı ikilik tabana çevirmek için kullanılan bin() fonksiyonuna bakalım.

bin(4) # bin fonksiyonu . Sayımız 2'lik tabanda yazıldı. (1 ve 0)
'0b100' # 2 üzeri 0 + 2 üzeri0 2 üzeri 1

bin(521) # bin fonksiyonu . Sayımız 2'lik tabanda yazıldı. (1 ve 0)
'0b1000001001'

#Şimdi de 10'luk tabandaki bir sayıyı 16'lık tabana çevirmek için kullanılan hex() fonksiyonuna bakalım.
hex(20)
hex(32) # Sayımız 16'lık tabanda yazıldı.
'0x20'

#Fonksiyonlar
#abs fonksiyonu
#Sayının mutlak değerini almamızı sağlar.

a=abs(22) #22
b= abs(-4)
c=abs(4.5)
d=abs(-1.4) #1.4
print(a,b,c,d)

#round fonksiyonu
#Sayıları alta veya üste yuvarlar.
round(3.4) #3
round(5.7) #6
round(3.2229,3) #virgülden sonraki kıım ondalıklı kısmın 3.basamağına göre yuvarla demek  #sonuç 3.223

round(3.21324321321323,4) # Ondalıklı sayının 4. hanesine göre yuvarlar
#3.2132

# max ve min fonksiyonu
max(3,4) # İstediğimiz kadar değer verebiliriz.
#4

max(100,-2,3,4,1,131)  # İstediğimiz kadar değer verebiliriz.
#131

max([13.2,-4.32,1.2,15.6]) # Sayıları liste şeklinde de verebiliriz.
#15.6

max((13.2,-4.32,1.2,15.6)) # Sayıları demet şeklinde de verebiliriz.
#15.6

#sum fonksiyonu
#sum() fonksiyonu verilen değerleri toplayarak döndürür. Değerlerin liste,demet vb. şeklinde verilmesi gerekir

x=sum((2,3,4,5))
y=sum([2,3,4,5,6])
print(x,y) # 14 ve 20 #float da gönderebiliriz.

#pow fonksiyonu
#pow() fonksiyonu üs alma işlemlerinde kullanılır.

z=pow(12,2) #144
pow(2,4) # 2 üzeri 4
#16
pow(3,4) # 3 üzeri 4
#81
pow(17,2) # 17 üzeri 2
#289