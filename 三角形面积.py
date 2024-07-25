import math
a=eval(input("请输入三角形的第一条边："))
b=eval(input("请输入三角形的第二条边："))
c=eval(input("请输入三角形的第三条边："))
p=(a+b+c)/2
area=math.sqrt(p*(p-a)*(p-b)*(p-c))
a=str(a)
b=str(b)
c=str(c)
s="三角形的第一条边："+a,"三角形的第二条边："+b,"三角形的第三条边："+c
print(s,"三角形的面积为:{:.2f}".format(area))
