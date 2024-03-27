import math

while True:

    n = int(input('請輸入正整數...'))

#方法1、迭代-->    
    tmp = 1
    f1 = 0
    for i in range(1,n+1):
        tmp *= i
        f1 += tmp
    print(f1)
#方法1、迭代<--

#方法2、math.factorial()-->
    f2 = 0
    for i in range(1,n+1):
        f2 += math.factorial(i)
    print(f2)
#方法2、math.factorial()<--
