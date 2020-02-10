print('1：加法 +')
print('2：减法 —')
print('3：乘法 *')
print('4：除法 /')

i=0
while i==0:
    choice = int(input('Please input number(1/2/3/4): '))
    if choice not in list(range(1,5)):
        print('输入错误！')
    else:
        a = input('请输入第一个数：')
        b = input('请输入第二个数：')
        while (not a.isdigit()) or (not b.isdigit()):
            print('输入错误,请重新输入!')
            a = input('请输入第一个数：')
            b = input('请输入第二个数：')

        num1 = float(a)
        num2 = float(b)
        if choice == 1:
            print(num1,"+",num2,"=",(num1+num2))
        elif choice == 2:
            print(num1,"-",num2,"=",(num1-num2))
        elif choice == 3:
            print(num1,"x",num2,"=",(num1*num2))
        elif choice == 4:
            print(num1,"/",num2,"=",(num1/num2))

        again=input('需要再次运算吗？(Y/N):')
        if again.lower()=='n': i+=1
    