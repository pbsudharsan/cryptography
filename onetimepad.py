import sys
def xora(m, n):    
    return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(m[:len(n)], n)])
#Reading file and converting to ascii for comparison
with open(fname) as f:
 cipher = f.read().splitlines()
#converting to ascii for comparison can laso be done in binary
a = [i.decode("hex") for i in cipher]
stream = {}
# find (possible) blank spaces from each encrypted string
for i in range(0, len(a)):
        	text = {}
        for j in range(0, len(a)):
                if j != i :                  
                b = xora(a[i], a[j])
                for k in range(0, len(b)):
                       c=ord(b[k]) 
                      if (c >= 65 and c <= 90) or (c >= 97 and c <= 122)  
                      or (c == 0)   
                                if k in text :
                                        text[k] = text[k] + 1
                                else:
                                        text[k] = 1
        print “Possible spaces in meassage ”,i         
        print text
        
