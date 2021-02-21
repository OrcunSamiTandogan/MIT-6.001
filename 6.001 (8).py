#
#def bob(n):
#    count = 0
#    for i in range(0,len(n)-2):
#        if n[i:i+3] == 'bob':
#            count += 1
#    return print(count)
#a = str(input("bir seyler"))
#if bob(a):
#    print('this is your vowel number')
s = 'azcbobobegghakl'
def bob(s):
    count = 0
    for i in range(0,len(s)-2):
        if s[i:i+3] == 'bob':
            count += 1
    return count
print("Number of times bob occurs is:", bob(s))