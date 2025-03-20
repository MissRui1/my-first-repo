times=0
count=3
while times<count:
    age=int(input("请输入您要猜的年龄："))
    if age==25:
        print('恭喜您猜对了！')
        times+=3
        #直接中断循环
        pass
    elif age>25:
        print ('猜大了，请再试试看')
        pass
    else:
        print('猜小了，请再试试看')
        pass
    times+=1
    if times==3:
        choose=input('想不想继续猜呢 Y/N?')
        if choose=='Y'or choose=='y':
            times=0 #重置为初始值
            pass
        elif choose=='N'or choose=='n':
            times+=1
            pass
        else:
            print('请输入正确的标识，谢谢配合！')
            pass
        pass