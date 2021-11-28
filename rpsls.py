#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：冉佳乐
日期：2021.11.28
"""

import random
answer=random.randint(0,4)

#0 —  石头
#1 — 史波克
#2 —  布
#3 —  蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数

def name_to_number(name):
    """
    将游戏对象对应到不同的整数
    """
    if name=="石头":
        name=0
    elif name=="史波克":
        name=1
    elif name=="布":
        name=2
    elif name=="蜥蜴":
        name=3
    elif name=="剪刀":
        name=4
    else: name="Error: No Correct Name"
    return name

def number_to_name(number):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """
    if number==0:
        number="石头"
    if number==1:
        number="史波克"
    if number==2:
        number="布"
    if number==3:
        number="蜥蜴"
    if number==4:
        number="剪刀"
    return number

def rpsls(player_choice):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果

    """
    if player_choice == 0:
        if answer == 3:
            print("您赢了")
        elif answer == 4:
            print("您赢了")
        elif answer == 1:
            print("机器赢了")
        elif answer == 2:
            print("机器赢了")
        else:
            print("您和计算机出的一样呢")
    elif player_choice == 1:
        if answer == 0:
            print("您赢了")
        elif answer == 4:
            print("您赢了")
        elif answer == 2:
            print("机器赢了")
        elif answer == 3:
            print("机器赢了")
        else:
            print("您和计算机出的一样呢")
    elif player_choice == 2:
        if answer == 1:
            print("您赢了")
        elif answer == 0:
            print("您赢了")
        elif answer == 3:
            print("机器赢了")
        elif answer == 4:
            print("机器赢了")
        else:
            print("您和计算机出的一样呢")
    elif player_choice == 3:
        if answer == 1:
            print("您赢了")
        elif answer == 2:
            print("您赢了")
        elif answer == 0:
            print("机器赢了")
        elif answer == 4:
            print("机器赢了")
        else:
            print("您和计算机出的一样呢")
    elif player_choice == 4:
        if answer == 3:
            print("您赢了")
        elif answer == 2:
            print("您赢了")
        elif answer == 1:
            print("机器赢了")
        elif answer == 0:
            print("机器赢了")
        else:
            print("您和计算机出的一样呢")
    else:
        player_choice = "Error: No Correct Name"


print("欢迎使用RPSLS游戏")
print("----------------")
player_choice=input("请输入您的选择:")
print("----------------")
player_choice_number=name_to_number(player_choice)
computer_number=number_to_name(answer)
if player_choice_number=="Error: No Correct Name":
    print(player_choice_number)
else:
    print("您的选择为：%s"%player_choice)
    print("计算机的选择为：%s"%computer_number)
    rpsls(player_choice_number)

