import random
f=open('fiveunique.txt', 'r')
dstring=f.read() 
dstring=dstring.lower()
f.close()
lis=dstring.split()
liss=[]
guess='crate'
knownletters=['_','_','_','_','_']
unknownletters=['_','_','_','_','_']
guesslist=[]
wl=[]
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def checkdupe(i,letters):
    
    if not len(i) == len(set(i)):
        
        return False
    
    return True
for i in lis:
    if checkdupe(i,letters):
        liss.append(i)
lis=[]
for i in liss:
    i=list(i)
    if len(i)==5:
        
        lis.append(i)






def smoothprint(word):
    a=''
    for i in list(word):
        a+=i
    return a



print('the word is',smoothprint(lis[random.randint(0,len(lis)-1)]))
def checkknownletters(kl,word):
   
    for i in range(len(kl)):
        
        
        if kl[i]!='_':
            if kl[i]!=word[i]:
                return False
          
                    
    return word
def checkunknownletters(un,word):
    for i in range(len(un)):
        if un[i] !='_':
          if not un[i] in word:
            return False
          if un[i]==word[i]:
            return False
          
          
            
    return word

def checkwrongletters(wl,word):
  
    for i in wl:
        if i in word:
            return False
    
    return word


def findguess(knownletters, unknownletters, lis,wl):
    global guesslist
    
    poskl=[]
    for i in lis:
        i=list(i)
        if checkknownletters(knownletters,i)!=False and checkunknownletters(unknownletters,i)!=False and not checkunknownletters(unknownletters,i) in guesslist and checkwrongletters(wl,i)!=False:
            poskl.append(checkknownletters(knownletters,i))
       
 
    try:
        return poskl[random.randint(0,len(poskl)-1)]
    except:
        print(poskl)
        while True:
            pass
       
while True:
    
    inp=input(smoothprint(guess)+': ')
    inp=list(inp)
    
    for i in range(len(inp)):
        if inp[i]=='2':
            knownletters[i]=list(guess)[i]
        if inp[i]=='1':
            unknownletters[i]=guess[i]
        if inp[i]=='0':
            wl.append(guess[i])
 
    guess=findguess(knownletters,unknownletters,lis,wl)
    guesslist.append(guess)
        








        
