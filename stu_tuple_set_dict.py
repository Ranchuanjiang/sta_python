# 元组的学习
# count() 同 list 查找参数在元组 出现的次数
t1 = (1, 2, 2, 3, 5, 6, 7, 2)
print(t1.count(2))
print("@@" * 20)
# index() 同list 查找参数 在元组 出现的位置 有多个返回第一个的位置
# index(value,[sta ,end]) 可以指定查询范围
print(t1.index(3))
print(t1.index(2))
print("@@" * 20)
