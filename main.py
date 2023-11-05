'''elimizdeki toplam çikolatayı öğrencilere olabildiğince fazla çikolata vererek ardışık sayılarda paylaştıracağız,
işlem sonucu kalan ekrana yazdırılacak, kalan yoksa "paylaştırılamaz diyecek"'''

print("Sınıf mevcudu :",end=" ")
ogrenci = input()
ogrenci = int(ogrenci)
print("Çikolata sayısı :",end=" ")
c = input()
c = int(c)
def cikoalta(ogrenci,c):
    arr = []
    j = 1
    kalan = 0
    while (1):
        for i in range(0, ogrenci):
            arr.append(j)
            j += 1
        toplam = sum(arr)
        if ((ogrenci-1)*ogrenci/2) + sum(arr) <= c:
            j = arr[0]+1
            arr.clear()
            continue
        else:
            kalan = c - toplam
            break
    if(kalan<0):
        print("paylaştırılamaz !")
    else:
        return kalan

print("Kalan Çikolata : ",cikoalta(ogrenci,c))











