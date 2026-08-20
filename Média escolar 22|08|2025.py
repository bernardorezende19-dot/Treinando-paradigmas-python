n1 = 5
s1 = 1
s2 = 0
avs = 0
def b(n1, s1, s2, avs):
    if((n1+s1+s2)>= 6):
        print("Passou")
    else:
        if (avs >= 6):
            print("Passou")
        else:
            print("Reprovado")

b(5,1,0,0)
b(2,1,0,0)
b(1,1,6,5)
