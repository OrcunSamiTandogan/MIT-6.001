def longest(s): 
   best = ''
   temp = ''
   for i in range(len(s)-1):
       if s[i] <= s[i+1]:
           temp += s[i]
           if (i+2) == len(s) and (len(temp)+1) > len(best):
               best = temp
           else:
               temp += s[i]
               if len(temp) > len(best):
                   best = temp
               temp = ''
   return best