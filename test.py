# 对于给定列表 , 用下标4与下标0比较 , 5与1比较 , 6与2比较, 依次后移.所以样本前四个是没有TD数字的
list1 = (1, 2, 3, 4, 5, 8, 7, 6, 69, 2, 3, 4, 5, 6, 7, 8, 12, 123, 233, 445, 446, 6, 5, 4, 3)  #list1是测试样本
list2 = [0, 0, 0, 0]  # list2是存储TD结果用的,前4个无效用0占位置.因为TD定义是下标第n和n-4比较
top = 0  # 初始化上标
bot = 0  # 初始化下标
for i in range(4, len(list1)):   #为何会从4开始,因为要用index n与index n-4 作比较,比他大才算TD上标1
    if list1[i] > list1[i - 4]:  #由于i本身就是从4开始, 所以就是由4与0比较,i的最后一个循环到列表的最后一个数字,能够遍历完
        top += 1
        bot *= 0
        list2.append(top)
    else:
        top *= 0
        bot += 1
        list2.append(-bot)
for c in list2:
    print(c)