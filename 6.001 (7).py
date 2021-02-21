#def vowel(x):
#    a = ['a','e','i','o','u']
#    count = 0
#    for i in x:
#        if i in a:
#            count += 1
#    return count
#n = str(input("give me a word: "))
#a = vowel(n)
#print("Number of vowels", a)

#s = 'azcbobobegghakl'
#a = ['a','e','i','o','u']
#count = 0
#for i in s:
#    if i in a:
#        count += 1
#print("Number of vowels", count)

s= "boboboboboobobb"
#for i in range(0, len(s)-1):
#    print(s[i],"bu i", s[i+1],"bu +1",s[0],"bu da 0")
#    
c = 0
def bob(s):
    for i in range(0,len(s)-2):
        if s[[i]+s[i+1]+s[i+2] == "bob":
            c += 1
    return c
print("Number of times bob occurs is: ",c)
