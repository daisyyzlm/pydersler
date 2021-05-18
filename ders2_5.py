# Ara Ders (Ders 2.5): Kullanıcıdan giriş alma ve tür dönüşümleri, None.

"""
--Kullanıcıdan bilgi istemek
Kullanıcıdan oluşturduğumuz komut istemi penceresinden bilgi isterken "input" fonksiyonunu kullanabiliriz.
"input" fonksiyonu opsiyonel olarak kullanıcıdan bilgi isterken sorulacak olan soruyu da yazdırabilir.
Bunu da ilk parametresine sormasını istediğimiz yazı değişkenini giriyoruz.

--Tür dönüşümleri
Bazı durumlarda mesela yazıyı sayıya, sayıyı yazıya çevirmemiz gerekiyor.
Böyle durumlarda tür dönüşümlerine ihtiyaç duyarız.
Örnek olarak yazıyı sayıya çevirmek istediğimizde şu kod işimizi görecektir:
x = "3.14"
y = float(x) # Ondalıklı sayılar: float

a = "98"
b = int(a) # Tam sayı: int uzun adıyla integer

Sayıyı yazıya çevirmek:
x = 2.984
y = str(x) # Yazı: str uzun adıyla string

--None
Bazı durumlarda değişkenlere değer atamayıp Python'a onların varlığını göstermemiz gerekebilir.
Bu gibi durumlarda "None" kullanabiliriz. Anlamından da anlaşılacağı üzere hiç, yok gibi anlamlara gelir.
"""

# Kullanıcıdan giriş alma
"""
ad = input("Adınızı giriniz: ")
print("Hoş geldin, " + ad)
"""

# Tür dönüşümleri
"""
x = 3.14
print("Yazdırmak istediğimiz sayı: " + str(x))
"""

# None
"""
x = None
"""