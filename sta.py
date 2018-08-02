"""
打印以下图形:
* * * * *
*       *
*       *
* * * * *

"""
print("for 循环测试")
for i in range(4):
    if i == 0 or i == 3:
        print("* " * 5)
    else:
        print("*\t\t*")

