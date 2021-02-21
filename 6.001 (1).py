##def rehber(ad = "none", soyad="none",yas="none"):
##    print("kayit aciliyor")
##    print("Ad:()\nSoyad:()\nYas:()\n".format(ad,soyad,yas))
##    print("kayit tamam")
##rehber(ad = 1,soyad = 2,yas = 3)
#def geo(sekil):
#    if len(sekil) == 3:
#        a = sekil[0]
#        b = sekil[1]
#        c = sekil[2]
#        if (a+b) > c and (a+c) > b and (b+c) > a:
#            print("this is ucgen")
#            if a == b and a == c:
#                return print("eskenar")
#            elif a == b or a == c or b == c:
#                return print("iki kenar")
#            else:
#                return print("cesitkenar")
#    elif len(sekil)== 4:
#        a = sekil[0]
#        b = sekil[1]
#        c = sekil[2]
#        d = sekil[3]
#        if a == b and b == c and c == d:
#            return print("kare")
#        elif a == b and c == d:
#            return print("dikdortgen")
#        elif a == c and b == d:
#            return print("dikdortgen")
#        else:
#            return print("dortgen")
#    else:
#        print("ucgen veyahut dortgen degil")
#    
#while(True):
#        eleman = int(input("eleman sayisi"))
#        if eleman == 3:
#            a = int(input("kenar uzunlugu"))
#            b = int(input("kenar uzunlugu"))
#            c = int(input("kenar uzunlugu"))
#            x = []
#            x.append(a)
#            x.append(b)
#            x.append(c)
#            geo(x)
#            break
#        elif eleman == 4:
#            a = int(input("kenar uzunlugu"))
#            b = int(input("kenar uzunlugu"))
#            c = int(input("kenar uzunlugu"))
#            d = int(input("kenar uzunlugu"))
#            x = []
#            x.append(a)
#            x.append(b)
#            x.append(c)
#            x.append(d)
#            geo(x)
#            break
#        else:
#            print("3 ya da 4 elemanli kenarlar lazim")
#        
#        

#            
#sporcu = ("sporcu")
#abc = {"falcon": sporcu, "edt":["dancer","dansci"], "beseri":"already broken"}
##print(type(abc)) 
##print(abc["falcon"])
#for i in abc.items():
#    print(i)
#x = input("ne bilmek istiyorsun")
#print("{}`nin icerigi".format(x))
#for i in (abc[x]):
#    print(i)
## sozluge girdigin seyler tuple ya da list olabilir ama sozlukteki girdilerin anlamin
## aciklama kismi tekse, for i in yaptiginda string`i tek olarak gorup, harfleri veriyor sana tek tek
## format`li kisimda {} koymanin faydasi yazdigin seyin hemen akabinde kesme isareti gormek icin
#
#import urllib.request
#url1 = "https://www.google.com.tr/search?q=ucak&client=opera&hs=QNU&sxsrf=ALeKk01e6lV6AJ-nfzD-xtveecO_4LteOQ:1585858981406&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjxnICKycroAhXKThUIHbsOAPMQ_AUoAnoECA0QBA&biw=1496&bih=754#imgrc=SE-7vU54gFo80M"
#url2 = "https://www.google.com.tr/search?q=ucak&client=opera&hs=QNU&sxsrf=ALeKk01e6lV6AJ-nfzD-xtveecO_4LteOQ:1585858981406&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjxnICKycroAhXKThUIHbsOAPMQ_AUoAnoECA0QBA&biw=1496&bih=754#imgrc=Ka8ex7KoTOjIKM"
#sayi=1
#
#urllist = [url1,url2]
#for i in urllist:
#    urllib.request.urlretrieve(i,"resim"+str(sayi)+".jpg")
#    # str olarak cevirmemizin sebebi int ile str`yi toplamak diye bir sey yok, bu sebeple
#    #i listedeki her url`yi alip indiriyor, akabindekileri birlestirip bir dosyaya kaydediyor
#
##
#sayi1 = input("sayi1")
#sayi2 = input("sayi 2")
#
#try:
#    sayi1 = int(sayi1)
#    sayi2 = int(sayi2)
#    print("{}: sayi 1".format(sayi1))
#    print("{}: sayi 2".format(sayi2))
#    #format kisimlarini buraya koymak su demek: eger calisiyorsa bunlar da calissin
#    print(sayi1/sayi2)
#
#except ValueError:
#    print("deger hatasi aliyoruz")
#except ZeroDivisionError:
#    print("0`a bolunmez")
#
#try:
#    dosya = open("odtu.txt","r")
#    dosya.close()  
#except NameError:
#    print("dosya bulunamadi")
#except SyntaxError:
#    print("idk this")
#except FileNotFoundError:
#    print("dosya yok"   )
#        
a = range(1,100)
for i in a:
    if i == 3:
        print("hell yeah")
    
    
    
    
    
    
    
    