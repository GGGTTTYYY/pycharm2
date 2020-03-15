import random
a = input("请输入红包总数： ")
a1 = int(a)
b = input("请输入红包数 ")
b1 = int(b)
list1 = []
print("- - - - 开始抢红包- - - -")

for i in range(b1):
    s = input("输入q抢红包： ")
    if s == 'q':
        pass
    else:
        print("请输入正确字符！")
        break
    if i < (b1-1):
        qiangde = (random.uniform(0, 100-sum(list1)))/(10 - i)
    else:
        qiangde = a1 - sum(list1)
    qiangde = round(qiangde, 2)
    print("恭喜你，抢到{}元红包".format(qiangde))
    hongbaoshu = b1-1-i
    print("还剩余{}个红包".format(hongbaoshu))
    list1.append(qiangde)
    print("已经得到红包：", end="")
    print(list1)
    print("- - - - - - - - -")
print("所有红包已抢完")
zuidazhi = max(list1)
cishu = list1.index(zuidazhi)+1
print("第{0}次手气最好，抢得{1}元".format(cishu, zuidazhi))

