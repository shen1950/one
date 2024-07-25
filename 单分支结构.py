a,b=eval(input())
print(a,b)
print(f'a={a},b={b}')
if a<b:
    a,b=b,a
print('a={},b={}'.format(a,b))