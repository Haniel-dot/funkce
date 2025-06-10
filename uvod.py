def soucet():
    a=2
    b=3
    print(a+b)
soucet()
 
def jmeno():
    uzi=input("zadejte jmeno")
    print(f"Ahoj",uzi)
jmeno()
 
def pole():
    znamky=[5,2,1,3,4,2]
    soucet=sum(znamky)/len(znamky)
    print(soucet)
pole()
 
def ahoj():
    for i in range(5):
        print("ahoj")
 
ahoj()
 
def krava():
    zvire=[]
    for i in range(3):
        zvire.append(input("zadejte 3 zivre"))
    print(zvire)
    print(len(zvire))
 
krava()
