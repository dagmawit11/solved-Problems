n = int(input())
for i in range(n):
    num = int(input())
    newGrad = (((num +4))//5)*5
    if num < 38:
        print(num)
    elif newGrad - num < 3:
        print(newGrad)
    else:
        print(num)



