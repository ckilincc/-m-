cumle = ("new blood join this earth")

kelimeler = cumle.split()


# kelimeler.sort() 
# kullanılabilir fakat kendi algoritmasına göre sıralar

for kelime in kelimeler:
    print(kelime)
    
# for döngüsü kullanılarak her satıra birer kelime veya harf yazdırılabilir

for kelime in kelimeler:
    for harf in kelime:
        print(harf)