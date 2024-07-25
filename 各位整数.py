m=input()
n=len(m)
a=eval(m%n)
b=eval(m//(n-1)%(n-1))
z=a+b
print(z)

#
x=input()
xlst=list(map(int,x))
total=sum(xlst)
print(total)
