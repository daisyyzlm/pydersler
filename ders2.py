# Ders 2: Değişkenler

"""
--Değişkenler nedir?
-Değişkenler (matematikte bilinmeyenler de denir) her zaman değişmeye müsait olan ve değerleri temsil eden bir kavramdır.
(Mesela x, y, z, a, b, c vs. ancak Python'da tek harfli bir değişken olmasına gerek yok.)

--Değişken nasıl tanımlanır?
x = 36
y = 500.2
z = "Merhaba!"

--Değişken isimlendirme kuralları
-Değişkenler latin alfabesindeki bütün karakterleri içerebilir, özel karakter olarak ise sadece "_" karakteri kullanılabilir.
-Değişken adlarına büyük harfle başlanmaması tavsiye edilir.
-Değişken adlarında türkçe harfler kullanılmamalı.

Sayı değişkenlerinde bütün aritmetik operatörler kullanılabilir.
Yazı değişkenlerinde toplama (+) ve çarpma (*) hariç hiçbir aritmetik operatör KULLANILAMAZ.

Aritmetik Operatörler:
+ (Toplama)
- (Çıkarma)
* (Çarpma)
/ (Bölme)

% (Mod Alma, yani bölme işlemi sonucunda kalan sayıyı yazdırır.)
"""

# Örnek:
# Herhangi bir öğrenicinin 3 not ortalamasını alma.

not1 = 15
not2 = 0
not3 = 100

# Ortalama = sayıların toplamı / sayı miktarı'dır

ortalama = (not1 + not2 + not3) / 3
print("Ortalama:", ortalama)