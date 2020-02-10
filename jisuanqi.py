print('欢迎使用python加法简易计算器')

a=input('请输入您要运算的第一个数：')
if a=='':
    print('数字不可为空')
    a=input('请重新输入第一个数：')
else:
    print('您输入的第一个数是:',a)

b=input('请输入您要运算的第二个数：')
if b=='':
    print('数字不可为空')
    b=input('请重新输入第二个数：')
    print(a,'+',b,'=',float(a)+float(b))
else:
    print('您输入的第二个数是:',b)
    print(a,'+',b,'=',float(a)+float(b))