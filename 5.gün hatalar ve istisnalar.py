#Ancak bu istisnai durumlarda, hataların türüne göre programlarımızı daha güvenli bir şekilde yazabiliriz.
#Yani hata çıkarabilecek kodlarımızı öngörerek bu hataları programlarımızda yakalayabiliriz. Pythondaki bazı hatalara şunlar örnek verilebilir;

#Hata Yakalama - try,except,finally
#Bu konuda programlarımızda hata verebilecek kodları yakalayabildiğimiz try,except,finally
#bloklarını ve fonksiyonlarda kendi hatalarımızı nasıl fırlatacağımızı öğreneceğiz.
"""   try:

                                           Hata çıkarabilecek kodlar buraya yazılıyor.
                                                   Eğer hata çıkarsa program uygun olan except bloğuna girecek.
                                                Hata oluşursa try bloğunun geri kalanındaki işlemler çalışmayacak.
                                           except Hata1:
                                                   Hata1 oluştuğunda burası çalışacak.
                                           except Hata2:
                                                   Hata2 oluştuğunda burası çalışacak.


                                             / """


try:
    a = int("324234dsadsad")  # Burası ValueError hatası veriyor.
    print("Program burada")
except:  # Hatayı belirtmezsek bütün hatalar bu kısma giriyor.
    print("Hata oluştu")  # Burası çalışır.

print("Bloklar sona erdi")

#Burada a = int("324234sadsad") kodu sıkıntı verdiği için program bu bloktan çıkarak direk except bloğuna girdi
# ve "Hata oluştu" yazdı. try ,except bloğu bitince program ekrana "Bloklar sona erdi" yazdırdı.

try:
    a = int(input("Sayı1:"))
    b = int(input("Sayı2:")) # Hata burada oluşuyor. ValueError'a bloğuna giriyoruz.
    print(a / b)
except ValueError:
    print("Lütfen inputları doğru girin.")
except ZeroDivisionError:
    print("Bir sayı 0'a bölünemez.")

#İstersek bu iki hatanın aynı except bloğuna girmesini sağlayabiliriz.

try:
    a = int(input("Sayı1:"))
    b = int(input("Sayı2:"))
    print(a / b)
except (ValueError,ZeroDivisionError):
    print("ZeroDivision veya ValueError hatası")

#try,except,finally blokları

#Bazen programlarımızda her durumda mutlaka çalışmasını istediğimiz kodlar bulunabilir.Bunun için biz kendi try,except bloklarına ek olarak bir tane finally bloğu ekleyebiliriz.
# finally blokları hata olması veya olmaması durumunda mutlaka çalışacaktır. Yapısı şu şekildedir;

"""               try:

                    Hata çıkarabilecek kodlar buraya yazılıyor.
                    Eğer hata çıkarsa program uygun olan except bloğuna girecek.
                    Hata oluşursa try bloğunun geri kalanındaki işlemler çalışmayacak.
                except Hata1:
                    Hata1 oluştuğunda burası çalışacak.
                except Hata2:
                    Hata2 oluştuğunda burası çalışacak.

                    //
                    //
                    //
                finally:
                    Mutlaka çalışması gereken kodlar buraya yazılacak.
                    Bu blok her türlü çalışacak."""

try:
    a = int(input("Sayı1:"))
    b = int(input("Sayı2:"))
    print(a / b) # Hata burada oluşuyor. ZeroDivisionError'a bloğuna giriyoruz.
except ValueError:
    print("Lütfen inputları doğru girin.")
except ZeroDivisionError:
    print("Bir sayı 0'a bölünemez.")
finally:
    print("Her durumda çalışıyorum.")

#Hata fırlatmak

#Bazen kendi yazdığımız fonksiyonlar yanlış kullanılırsa kendi hatalarımızı üretip Pythonda bu hataları fırlatabiliriz.
# Bunun içinde raise anahtar kelimesini kullanacağız. Hata fırlatma şu şekilde yapılabilmektedir;


"""     raise HataAdı(opsiyonel hata mesajı)        """




# Verilen string'i ters çevirmek
def terscevir(s):
    if (type(s) != str):
        raise ValueError("Lütfen doğru bir input girin.")
    else:
        return s[::-1]