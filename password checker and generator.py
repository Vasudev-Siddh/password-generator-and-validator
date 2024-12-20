import random
def rndm():
    rnd=random.choices('ABCDEFGHIJKLMNOP!@#$%^&*QRSTUVWXYZab1234567890cdefghijklmnopqrstuvwxyz')
    a=''
    for i in rnd:
        a=a+str(i)
    return a

def rndm1():
    rnd=random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    a=''
    for i in rnd:
        a=a+str(i)
    return a

def rndm2():
    rnd=random.choices('abcdefghijklmnopqrstuvwxyz')
    a=''
    for i in rnd:
        a=a+str(i)
    return a

def rndm3():
    rnd=random.choices('1234567890')
    a=''
    for i in rnd:
        a=a+str(i)
    return a

def rndm4():
    rnd=random.choices('!@#$%^&*')
    a=''
    for i in rnd:
        a=a+str(i)
    return a

def passchecker(password):

    if ' ' not in password:
        u=l=s=c=n=False
        for i in password:
            if i.isupper():
                u=True
            elif i.islower()==True:
                l=True
            elif i.isspace()==False:
                s=True
            elif i in ('!','@','#','$','%','^','&','*'):
                c=True
            elif i in ('1234567890'):
                n=True

        if u==True and l==True and s==True and c==True and n==True:
            print('Password can be considered strong')
        else:
            print('WEAK PASSWORD')
            if u==False:
                print('There is no uppercase characcter, try adding a few.')
            else:
                pass
            if l==False:
                print('There is no lowercase characcter, try adding a few.')
            else:
                pass
            if c==False:
                print('There is no special characcter, try adding a few.')
            else:
                pass
            if n==False:
                print('There are no numbers, try adding a few.')
            else:
                pass
            
    else:
        if ' ' in password:
                print('whitespaces are not allowed')
        else:
            print('Password is weak')

def passgenerator(paslen):
    i=4
    password=''
    password=password+rndm1()+rndm2()+rndm3()+rndm4()
    while i<paslen:
        password=password+rndm()
        i+=1
    print(password)
key= int(input('Enter 1 for checking wether password can be considered strong or not Enter 2 if you want to generate a password:   ' ))
if key==1:
    password=input('Enter your password to be checked: ')
    passchecker(password)
elif key==2:
    paslen=int(input('what length do you want your password to be(min:6 and max:10): '))
    if paslen>5 and paslen<11:
        passgenerator(paslen)
    else:
        print('Not in range asked')
else:
    print('Invalid Input')


    
