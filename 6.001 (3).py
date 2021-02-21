s = str(input("giriniz:  "))

counter = 0
for i in range(0, len(s)-2):
    if s[i:i+3] == 'bob':
        counter += 1
print(counter)
        