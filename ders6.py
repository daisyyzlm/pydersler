# Ders 6: Tuple'lar

"""
--Tuple'lar nedir?
-Tuple'lar, listeler gibi çalışan veri tipleridir. Bir değişken içerisinde birden fazla değer tutmamıza yarar.

--Tuple'ların list'lerden farkı nedir?
-Tuple'ın list'ten farkı sıralanmış(sırası oluşturulduktan sonra değişmeyen) ve boyutunun sabit olmasıdır.

--Tuple'lar neden kullanılır?
-Tuple'lar yeni elemanlar eklenmesini istemediğimiz ve elemanların sırasının değiştirilmemesini istediğimiz zamanlarda kullanılabilir.

Tuple örneği:
tup = ("Elma", "Armut", "Kayısı")

*** UNUTMA! ***
Tuple'larda bir elemanlı tuple oluşturmak istediğinizde
tup = ("Elma",)
yapmazsanız python bunu string olarak algılar.

tup = ("Elma",)
tup2 = ("Elma")

print(type(tup))
print(type(tup2))

Sırasıyla çıkacak değerler:
<class 'tuple'>
<class 'str'>
"""

tup = ("Elma", "Armut", "Kayısı")

# Tuple uzunluğunu öğrenme.
"""
print(len(tup))
"""

# Boş tuple oluşturma.
"""
tup = tuple()
"""

# Tuple'daki bir değerin endeksini öğrenme.
"""
print(tup.index("Armut"))
"""
