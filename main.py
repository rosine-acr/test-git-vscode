num = 67
 
flag = False
if num == 1 :
    print(num, 'is not a prime number')
elif num > 1 :
    for i in range(2, num) :
        if(num % i) == 0:
            flag = True
            break
   
    if flag:
        print(num, "is not a prime numver")
    else:
        print(num, "is a primer number")
Dispose d’un menu contextuel