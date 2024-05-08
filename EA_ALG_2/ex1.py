num = input()

pd = num[0]
ud = num[(len(num))-1]

flag = (pd == ud)

if flag:
    print("sim")
else:
    print("não")