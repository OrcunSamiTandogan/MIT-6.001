x = str(input("User 1 "))
y = str(input("User 2 "))
a = 0
while a < 3:    
     if (x == 'R'  and y == 'S'):
         print("1 wins")
         a +=1
         if a <3:
                      x = str(input("User 1 "))
                      y = str(input("User 2 "))
     elif x=='R' and y =='P':
         print("2 wins")
         a +=1
         break
     elif x == 'S' and y == 'R':
         print("2 wins")
         a +=1
         break
     elif x == 'S' and y == 'P':
         print("1 wins")
         a +=1
         break
     else:
         print("draw")
         a +=1
         if a <3:
                      x = str(input("User 1 "))
                      y = str(input("User 2 "))
    