import random
target=random.randint(0,100)
guess=int(input("请输入一个0-100："))
if guess==target:
    print("good job!")
else:
    if guess>target:
        print("too high!")
    else:
        print("too low!")    