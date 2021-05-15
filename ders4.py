# Ders 4: Stringler
"""
--String nedir?
-String yazı değişkenlerine verilen isimdir, yani karakter dizileridir (listelerle karıştırmayın).

--String nasıl oluşturulur?
-İki çift tırnak(") veya iki tek tırnak(') arasına yazılan yazılar aslında bir string değerdir.
Örnek:
yazi = "merhaba"
# Çift tırnak(") yerine tek tırnak(') da kullanılabilir.
"""

# Stringi cümle halinde yazma(ilk harfi büyük, geriye kalan harfleri küçük yazma).
"""
yazi = "Merhaba, Dünya!"
print(yazi)
yazi = yazi.capitalize()
print(yazi)
"""

# Bir string içerisinde bir stringin kaç defa tekrarlandığını bulma.
"""
yazi = "Merhaba, Dünya!"
kactaneavar = yazi.count("a")
print(yazi)
print(kactaneavar)
"""

# Stringin içerisinde bir stringin indexini bulma.
"""
yazi = "Merhaba, Dünya!"
index = yazi.find("Dünya")
print(yazi)
print(index)
"""

# Bir stringin alfanümerik(sadece latin alfabesi içeren yazı) olup olmadığını kontrol etme.
"""
yazi = "Merhaba, Dünya!"
isalnum = yazi.isalnum()
print(yazi)
print(isalnum)
"""

# Stringin alfabetik sırada olup olmadığını kontrol etme.
"""
yazi = "Merhaba, Dünya!"
alfabetik = yazi.isalpha()
print(yazi)
print(alfabetik)
"""

# Stringin ASCII karakterlerinden oluşup oluşmadığını kontrol etme.
"""
yazi = "Merhaba, Dünya!"
isascii = yazi.isascii()
print(yazi)
print(isascii)
"""

# Stringin sadece rakamlardan oluşup oluşmadığını kontrol etme.
"""
yazi = "45346783627836786483763478264"
isdigit = yazi.isdigit()
print(yazi)
print(isdigit)
"""

# Stringin küçük/büyük harflerden oluşup oluşmadığını kontrol etme.
"""
yazi = "Merhaba, Dünya!"
islower = yazi.islower()
isupper = yazi.isupper()
print(yazi)
print(islower) # Küçük
print(isupper) # Büyük
"""

# Stringi küçük/büyük harflerle yazar.
"""
yazi = "Merhaba, Dünya!"
print(yazi)
yazi = yazi.lower() # Küçük harf
print(yazi)
yazi = yazi.upper() # Büyük harf
print(yazi)
"""

# Stringi belirli bir stringe göre bölmek.
"""
yazi = "Merhaba, Dünya!"
kelimeler = yazi.split(" ")
print(yazi)
print(kelimeler)
"""

# Listeyi birleştirerek string yapma.
"""
liste = ["Ali", " ayvayı ", "yedi."]
yazi = "".join(liste)
print(liste)
print(yazi)
"""