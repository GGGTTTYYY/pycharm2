jiabin = ['张三', '李四', '王五', '赵六']
for i in jiabin:
    print("尊敬的" + i + "诚挚地邀请您参加宴会")
# print(jiabin )
quxiao_jiabin = '王五'
print("- -" * 20)
print(quxiao_jiabin + "无法参与宴会")
print("- -" * 20)
jiabin[jiabin.index(quxiao_jiabin)] = "王六"
for j in jiabin:
    print("尊敬的" + j + "诚挚地邀请您参加宴会")
# print(jiabin)
print("- -" * 20)
print("我找到了一个更大的餐桌")
print("- -" * 20)
jiabin.insert(0, '胖胖')
jiabin.insert(2, '榛子')
jiabin.append('胡七')
for i in jiabin:
    print("尊敬的" + i + "诚挚地邀请您参加宴会")
print("- -" * 20)
print("很抱歉的通知各位，只能邀请两人参加宴会")
print("- -" * 20)
# print(jiabin)
for m in jiabin:
    pop_jiabin = jiabin.pop(len(jiabin)-1)
    print(len(jiabin))
    print("尊敬的" + pop_jiabin + "很抱歉通知您由于桌位变化，不能与您共进晚餐")