import random
eded=random.randint(1,100)
print(eded)
print("1-100 arasi reqem texmin edin: ")
print("3 Texmin Hakkiniz Var!")

sans=3
while sans>0:

    print("Qalan sans: ",sans)
    sans=sans-1
    texmin=int(input("Texmininiz:"))
    if texmin>eded:
        print("daha asagi")
    elif texmin<eded:
        print("daha yuxari")
    else:
        print("texmin dogrudur ")
    if sans==0:
        print("Sans bitti")
