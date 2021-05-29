import random
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
player_choice=str(choice_name)
def name_to_number(name):
    if name == "石头":
        name = 0
        return name
    elif name == "史波克":
        name = 1
        return name
    elif name == "布":
        name = 2
        return name
    elif name == "蜥蜴":
        name = 3
        return name
    elif name == "剪刀":
        name = 4
        return name
def number_to_name(number):
    if number == 0:
       number = "石头"
       return number
    elif number == 1:
       number = "史波克"
       return number
    elif number == 2:
       number = "布"
       return number
    elif number == 3:
       number = "蜥蜴"
       return number
    elif number == 4:
       number = "剪刀"
       return number
        
computer_choice = random.randrange(5)
player_number = name_to_number(player_choice)
print ("你的选择为: " + player_choice)
print ("计算机的选择为: " + number_to_name(computer_choice))
difference = (int(player_number) - computer_choice) % 5
draws = 0
playerwins = 0
computerwins = 0
if difference in [1, 2]:
    print ("你获胜了！")
    playerwins = playerwins + 1
elif difference == 0:
    print ("平手了!")
    draws = draws + 1
else:
    print ("机器赢了!")
    computerwins = computerwins + 1




