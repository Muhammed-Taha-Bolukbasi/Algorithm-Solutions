#'''
#   elimizde bir dizi ör = [5,8,2,4,9,6] bu dizide indis lere gün olarak bakarsak
# dizi elemanları da o gün bir malın alım-satım fiyatı, yani soru bu malı hangi gün
# alıp hangi gün satarsak  max kar elde ederiz. Bu max karı ekrana yazan program
#
# '''

l1 = [4,5,8,9,6,2]

def kar(a=[]):
    max_kar = 0
    for i in range(0,len(a)-1):
        b = a[i]
        for j in range(i,len(a)-1):
            c = b - a[j+1]
            if c < 0 :
                c*=-1
                if c > max_kar:
                    max_kar = c
    print(max_kar)

kar(l1)
