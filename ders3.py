# Ders 3: Listeler

"""
--Listeler nedir?
-Listeler en basit tabiriyle birçok değeri tek bir değişkende tutmamıza yarayan veri tipidir.

--Listeler nasıl oluşturulur?
# İkisi de aynı şeyi verir.
liste = []
liste2 = list()

--Listeler neden kullanılır?
-Discord API üzerinden örnek verecek olursak şu soruyu kendimize sorarak liste kullanmanın mantığını anlayabiliriz.
-Her mesaj için ayrı bir değişken oluşturmak mı mantıklıdır, yoksa her mesajı tek bir değişken içerisinde tutmak mı mantıklıdır?

*** UNUTMA! ***
str(yazı değişkeni) aslında bir KARAKTER LİSTESİDİR.
yani 'a' karakteri ile 'b' karakterini aynı listede gösterince "ab" elde ediyoruz.
Bu yüzden len() fonksiyonunu str(yazı değişkenleri)'de de kullanabiliyoruz.
"""

# Listeden endeks numarasına göre değer alma.
"""
liste = ["Elma", "Armut", "Kayısı"]
alinandeger = liste[1]

print(alinandeger)
"""

# Listede endeks numarasına göre değer silme.
"""
liste = ["Elma", "Armut", "Kayısı"]
print(liste[1])
liste.remove(liste[1])
print(liste[1])
"""

# Listede bilinen bir değerin endeks numarasını bulma.
"""
liste = ["Elma", "Armut", "Kayısı"]
x = liste.index("Kayısı")
print(x)
"""

# Listedeki elemanları alfabeye göre veya küçükten büyüğe sıralama.
"""
liste = ["Elma", "Armut", "Kayısı"]
print(liste)
liste.sort()
print(liste)
"""

# Listenin sonuna bir değer ekleme.
"""
liste = []
print(liste)
liste.append("Mehmet")
print(liste)
liste.append(398)
print(liste)
liste.append(3.14)
print(liste)
liste.append(True)
print(liste)
"""

# Listenin en sonundaki değeri silme.
"""
liste = ["Elma", "Armut", "Kayısı"]
print(liste)
silineneleman = liste.pop()
print(liste)
print(silineneleman)
silineneleman = liste.pop(0)
print(liste)
print(silineneleman)
"""

# Listeyi ters çevirme.
"""
liste = ["Elma", "Armut", "Kayısı"]
print(liste)
liste.reverse()
print(liste)
"""

# İki listeyi birleştirme.
"""
liste1 = ["Ahmet", "Mehmet", "Ali", "Ayşe"]
liste2 = [3.14, 935, False, "Ahmet"]
print(liste1)
print(liste2)

# 1. yol
liste = liste1 + liste2
print(liste)

# 2. yol
liste1.extend(liste2)
print(liste1)
"""

# Bir değerin bir listede kaç defa olduğunu bulma.
"""
liste = ["Elma", "Armut", "Kayısı", "Armut"]
listedekacarmutvar = liste.count("Armut")
print(liste)
print(listedekacarmutvar)
"""

# Bir listenin uzunluğunu bulma.
"""
liste = ["Elma", "Armut", "Kayısı"]
listeuzunlugu = len(liste)
print(liste)
print(listeuzunlugu)
"""