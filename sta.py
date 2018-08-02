"""
打印下面的图形在输出上面
* * * * *
* * * * *
* * * * *
* * * * *
"""
for i in range(4):
    print("* " * 5)

print("# " * 50)
# 双层嵌套 循环打印

for i in range(4):
    for j in range(5):
        print("* ", end="")
    print()

"""
打印以下图形:
* * * * *
*       *
*       *
* * * * *

"""
print("=="* 50)
for i in range(4):
    if i == 0 or i == 3:
        print("* " * 5)
    else:
        print("*\t\t*")

print("# " * 50)
#双层嵌套循环打印
for i in range(4):
    if i == 0 or i == 3:
        print("* " * 5)
    else:
        for j in range(5):
            if j == 0 or j == 4:
                print("* ", end="")
            else:
                print("  ",end="")
        print()
print("==" * 50)
"""
打印下面三角形
* 
* * 
* * * 
* * * * 
* * * * * 
"""
for i in range(1, 6):
    print("* " * i)

print("##" * 50)
# 双层嵌套 循环打印
for i in range(5):
    for j in range(i +1):
        print("* ", end="")
    print()

print("==" * 50)
"""
# 打印空心三角形
* 
* * 
*   * 
*     * 
* * * * * 
"""
for i in  range(5):
    if i == 0 or i == 1 or i == 4:
        print("* " * (i + 1))
    if i == 2 or i == 3:
        print("*"," "*(i * 2 -3), "*")

print("##" * 50)
# 双层嵌套打印
# for i in range(1, 6):
#     if i == 1 or i == 5 or i == 2:
#         print("* " * i)
#     else:
#         for j in  range(i+1):
#             if j == 0:
#                 print("*", end="")
#             elif j == 3:
#                 print("*")
#             elif j == 4:
#                 print(" *")
#             else:
#                 print(" ", end="")


