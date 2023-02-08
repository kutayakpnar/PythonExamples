#upper() ve lower()
#upper() metodu stringin tüm karakterlerini büyük harfe çevirir.
#lower() metodu stringin tüm karakterlerini küçük harfe çevirir.

a="kutay".upper() #KUTAY
b="AKPINAR".lower() #akpinar
print(a,b)

#replace()
#replace(x,y) : Stringteki x değerlerini y ile değiştirir.
"Herkes ana baba bacı gardaş".replace("a","o")
#'Herkes ono bobo bocı gordoş'
"Kunduz".replace("duz","zun")
#'Kunzun'
"Python Programlama Dili".replace(" ","-")
#'Python-Programlama-Dili'


#startswith() ve endswith()
#startswith(x) : String x ile başlıyorsa True, başlamıyorsa False değeri döndürür.

#endswith(x) : String x ile bitiyorsa True, bitmiyorsa False değeri döndürür.

"python".startswith("P") # FALSE
"python".startswith("p") #TRUE
"python".endswith("n") #true
"python".endswith("on") #true

#split()
#split(a) : Verilen bir a değerine göre string parçalara ayrılarak herbir parça listeye atılır.

liste = "Python Programlama Dili".split(" ") # Boşluk karakterine göre ayrıldı.
print(liste) #['Python', 'Programlama', 'Dili']
liste2="mehmet-ku-tay-ak-pı-nar".split("-")
print(liste2) #['mehmet', 'ku', 'tay', 'ak', 'pı', 'nar']

#strip() , lstrip() ve rstrip()
#strip(x) : Stringin başında ve sonunda bulunan x değerlerini siler.

#lstrip(x) : Stringin sadece başında bulunan x değerlerini siler.

#rstrip(x) : Stringin sadece sonunda bulunan x değerlerini siler.

a="          mehmet kutay      akpınar   ".strip() # değer göndermezsek varsayılan olarak boşluk karakteri
print(a) #mehmet kutay      akpınar

">>>>>>>>>>>>>>Mustafa>>>>>>>>>>>>>>>>>>>>>>>>>>".strip(">")
'Mustafa'

"                            python      ".lstrip()
'python      '

"                            python      ".rstrip()
'                            python'

#join()
#Listenin elemanlarını bir string değeriyle birleştirmemizi sağlar.

liste = ["21","02","2014"]
x= "/".join(liste)
print(x) #21/02/2014
liste2=["kutay","1","5"]
y = "-".join(liste2)
print(y) #kutay-1-5
#join kullanırken içersinin string olması lazım int olursa hata verir.


#count()
#count(x): Stringin içindeki x değerlerini sayar.

#count(x,index): Stringin içindeki x değerlerini verilen index değerinden başlayarak saymaya başlar.
a =" mehmet kutay akpınar".count("e")
print(a) #2
a =" mehmet kutay akpınar".count("e",7) #0

#find() ve rfind()
#find(x) : x değerini baştan itibaren string içinde arar ve bulursa ilk bulduğu indeksi döndürür. Bulamazsa "-1" değerini verir.

#rfind(x) : x değerini sondan itibaren string içinde arar ve bulursa ilk bulduğu indeksi döndürür. Bulamazsa "-1" değerini verir.

"araba".find("a")
0

"araba".find("s")
-1

"araba".rfind("a")
4

"araba".rfind("s")
-1