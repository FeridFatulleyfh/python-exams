eded=int(input())
if eded > 1:
    for i in range(2, int(eded / 2) + 1):
        if eded % i == 0:
            print(f"{eded} murekkeb ededdir")
            break
    else:
        print(f"{eded} sadedir")
else:
    print(f"{eded} murekkeb ededdir.")
