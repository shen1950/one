# 编写一个程序，需要找钱给用户，现在只有50元，5元和1元的人民币若干
# 张。输入一个整数金额值，给出找钱的方案，假设人民币足够多，且优先使用面额大
# 的钱币。
money=int(input())
m50=money//50
money=money%50
m5=money//5
money=money%5
print("50元",m50,"张",sep="")
print("5元",m5,"张",sep="")
print("1元",money,"张",sep="")