#Pythonda aslında herbir dosya bir modüldür ve her bir modül içinde fonksiyonlar, sınıflar ve objeler barındırır. Biz de bu modülleri programımıza dahil ederek içindeki fonksiyonlardan, sınıflardan ve objelerden faydalanabiliriz.

#Pythonda da modül kavramı oldukça önemli bir kavramdır. Bir Python modülünü programımıza dahil ederek bu modüller içinde yazılan fonksiyonlardan ve sınıflardan kullanabilir ve programlarımızı daha efektif bir şekilde yazabiliriz. Eğer modül diye bir kavram olmasaydı, programlarımızdaki herbir fonksiyonu ve sınıfı kendimiz yazmak zorunda kalacaktık.

#Pythonda Python geliştiricileri tarafından yazılmış bir çok hazır modül bulunmaktadır. Ayrıca , programcıların internete ve Githuba yükledikleri bir çok modülü programlarımızda kullanabilir ve daha güzel programlar yazabiliriz.

#Modül Kavramını anladıysak bir sonraki konuda bir modül bir programa nasıl dahil edilir öğrenmeye çalışalım.

#>>>>>MODÜLLERİN KULLANIMI

import math # Modülü içeri aktarıyoruz. Artık bu modülün tüm fonksiyonlarını kullanabiliriz.
dir(math) # Math modülünün içindekileri görmek için dir fonksiyonunu kullanabiliriz.
help(math) # Fonksiyonların görevlerini görebilmek için help fonksiyonunu kullanabiliriz.

#Peki bu içeri aktarma yöntemiyle math modülünün herhangi bir fonksiyonunu nasıl kullanacağız ?

        #modül_adı.fonksiyonadı()

#Örneğin ilk olarak math modülünün içindeki factorial fonksiyonu ne iş yapıyor bakalım.

help(math.factorial)

print(math.factorial(5)) #çıktısı 120

print(math.floor(3.5))

import math as matematik #böyle de kullanabiliriz

matematik.factorial(5)

from math import * #yani math modülündeki bütün fonksiyonları dahil ettik

#böyle oluna fonksiyonun başına hiçbir şey yazmamıza gerek yok

print(factorial(5)) #çıktı 120 fonksiyonumuz direkt çalıştı

from math import factorial,floor,ceil #bu sefer math modülünden sadece bu 3 fonksiyonu içeri aktarmış olduk.

#KENDİ MODÜLLERİMİZİ YAZMAK







