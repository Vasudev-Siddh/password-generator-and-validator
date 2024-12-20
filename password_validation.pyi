def passd(password):

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
passd('sdpivikhx ')