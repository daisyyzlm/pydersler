# Ders 5: Dictionary'ler (Sözlükler)

"""
--Dictionary nedir?
-Dictionary aslında JavaScript'ten aşina olduğumuz JSON'lar gibidir.
-Dictionary'ler aslında key-value(anahtar-değer) listesidir.

--Dictionary'ler neden kullanılır?
-En basit örneğiyle oyun çevirilerindeki yazıların her bir dil için karşılığını value'lar ile,
-programlama içerisinde o yazıyı alabilmek için ise keyi kullanırız.

Dictionary Örnek:
sozluk = {
    "key1": "value1",
    "key2": "value2",
    "key3": {
        "key1": "value1"
    }
}
"""

sozluk = {
    "ad": "Ahmet",
    "boy": 1.82,
    "hobiler": "Yazılım, kitap okumak, oyun oynamak"
}

# Sözlüklerde anahtarı kullanarak değeri almak.
"""
print(sozluk["ad"])
veya
print(sozluk.get("ad")) # Daha güvenli
"""

# Sözlüğü temizleme.
"""
sozluk.clear()
"""

# Sözlükten anahtar-değer ikilisi silme.
"""
print(sozluk)
print(sozluk.pop("boy"))
print(sozluk)
"""

# Sözlükteki anahtarları list'e çevirme.
"""
print(sozluk.keys())
"""

# Sözlükteki değerleri list'e çevirme.
"""
print(sozluk.values())
"""

# Sözlüğün kaç anahtar-değer ikilisinden oluştuğunu öğrenme.
"""
print(len(sozluk))
"""