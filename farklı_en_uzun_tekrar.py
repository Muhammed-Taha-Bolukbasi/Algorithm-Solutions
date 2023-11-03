#yazılan ifadenin farklı en uzun tekrarını alır, aynı harf ile tekrar karşılaşılırsa baştaki silinir

s = input("---> ")
def lengthOfLongestSubstring(s : str):
    max = 0
    list_main = []
    list_sub = []
    max_sub = 0

    


    for i in range(0,len(s)):
        if s[i] not in list_sub:
            list_sub.append(s[i])
        try:
            for j in range(i + 1, len(s)):
                if s[j] not in list_sub:
                    list_sub.append(s[j])
                else:
                    max_sub = len(list_sub)
                    if max_sub > max:
                        max = max_sub
                        list_main.clear()
                        list_main = list_sub.copy()
                        list_sub.clear()
                    else:
                        list_sub.clear()
                    break
        except:
            pass

    if len(list_main) == 0:
        max = len(list_sub)
        str = ""
        for i in list_sub:
            str += i
        print(str)
        print(max)

    str = ""
    for i in list_main:
        str += i
    print(str)
    print(max)

lengthOfLongestSubstring(s)









