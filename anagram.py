'''
anagram : aynı harflerden oluşan farklı kelimeler
eğer iki kelie anagramsa "İki kelime anagramdır." değilse "İki kelime anagramdır." sonucunu verir.
'''

print("İlk kelime :",end=" ")
ilk_kelime = input()
print("İkinci kelime :",end=" ")
ikinci_kelime = input()

def anagram(ilk_kelime,ikinci_kelime):

    if len(ilk_kelime) != len(ikinci_kelime):
        return print("İki kelime anagram değil")

    l1 = []
    for i in range(0,len(ilk_kelime)):
        l1.append(ord(ilk_kelime[i]))

    for i in range(len(ikinci_kelime)):

        sayi_kod = ord(ikinci_kelime[i])

        for i in range(len(l1)):

            if sayi_kod == l1[i]:
                l1.remove(sayi_kod)
                break
            else:
                continue

    if len(l1) == 0:
        return print("İki kelime anagramdır.")
    else:
        return print("İki kelime anagram değildir.")

anagram(ilk_kelime,ikinci_kelime)



