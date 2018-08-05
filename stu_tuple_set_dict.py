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
# 字典 学习
# clear 清除字典
dict1 = {"a": 1, "b": 2, "c": 3}
dict1.clear()
print(dict1)
# copy()复制字典
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = dict1.copy()
print(dict2)
print(id(dict1))
print(id(dict2))
print("@@" * 20)
# fromkeys() 按照指定的序列为键创建字典, 值都是一样的
list1 = ["a", "b", "c"]
print({}.fromkeys(list1,2))
print({}.fromkeys(list1))
print("@@" * 20)
# get() 根据键返回值 找不到的键 如果设默认值 则返回默认值 如果没设默认值 则返回None
dict1 = {"a": 1, "b": 2, "c": 3}
print(dict1.get("a"))
print(dict1.get("d"))
print(dict1.get("d", 4))
print("@@" * 20)
# items() 将字典变成类似玉元组的形式方便遍历
dict1 = {"a": 1, "b": 2, "c": 3}
for k, v in dict1.items():
    print(k, v)
print(dict1.items())

