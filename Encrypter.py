import time
def encode(x):
    y=x[::-1]
    if (len(x)>3):
        p=y[0:len(y)//2]
        q=y[len(y)//2:]
        y=q+p
    y=y.replace(" ","$")
    return y
def decode(x):
    x=x.replace("$"," ")
    if (len(x)>3):
        p=x[0:len(x)//2]
        q=x[len(x)//2:]
        x=q+p
    x=x[::-1]
    if len(x)>4 and len(x)%2!=0:
        x=x[-1]+x[0:-1]
    return x
while (1):
    z=input("\nPress Y to encrypt\tN to Decrypt\t \tQ to quit\n")
    if z=="Y" or z=="y":
        a=input("Write something here:\n")
        a=encode(a)
        print(a)
    elif z=="n" or z=="N":
        b=input("Write encrypted text:\n")
        b=decode(b)
        print(b)
    elif z=="q" or z=="Q":
        print("Quitting in 5 seconds.....")
        time.sleep(5)
        exit()
    else:
        print("Please Enter a Valid input\t")
