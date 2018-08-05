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
# items() 将字典变成类似元组的形式方便遍历
dict1 = {"a": 1, "b": 2, "c": 3}
for k, v in dict1.items():
    print(k, v)
print(dict1.items())
print("@@" * 20)
# pop() 移除字典中指定的键 返回键所对应的值, 如果键不存在 则返回默认值, 如果键找不到,没设默认值就会报错
dict1 = {"a": 1, "b": 2, "c": 3}
print(dict1.pop("a"))
print(dict1)
print(dict1.pop("d", 4))
# print(dict1.pop("d"))
print("@@" * 20)
# popitem() 移除字典键值对 返回移除的键和值
dict1 = {"a": 1, "b": 2, "c": 3}
print(dict1.popitem())
print(dict1)
print(dict1.popitem())
print(dict1)
print("@@" * 20)
# setdefault() 在字典去一对键值对,返回该默认值,如果不在字典里则向字典添加该键值对
dict1 = {"a": 1, "b": 2, "c": 3}
print(dict1.setdefault("d", 5))
print(dict1)
print(dict1.setdefault("c"))

print("@@" * 20)
# update() 修改字典里的值
dict1 = {"a": 1, "b": 2, "c": 3}
print(id(dict1))
dict1.update({"a": 2, "d" :4})
print(id(dict1))
print(dict1)
dict1["a"] = 111
print(dict1)
print("@@" * 20)
# set 学习 里面数据没有重复的 且无序
a = set()
print(a)
list1 = [1, 2, 1, 4]
a = set(list1)
print(a)
list2 = ["ai", "ai", "爱", "爱"]
a = set(list2)
print(a)
print("@@" * 20)
# add() 向集合中添加元素
a = {1, 2, 4, 5, 3, "a", "c", "b"}
a.add(6)
print(a)
print(type(a))
a.add("A")
print(a)
print("@@" * 20)
# clear() 清空集合 返回 None
# copy() 复制集合
# pop() 随机弹出一个元素
a = {1, 2, 4, 5, 3, "a", "c", "b"}
print(a.clear())
a = {1, 2, 4, 5, 3, "a", "c", "b"}
b = a.copy()
print(b)
print(a.pop())
print(a)
print("@@" * 20)
# remove() 删除集合中的某个值 如果这个值不再集合中会报错
a = {1, 2, 4, 5, 3, "a", "c", "b"}
print(a)
a.remove(3)
print(a)
# a.remove(3)
print("@@" * 20)
# discard() 删除集合中的某个值, 如果值不存在 也不报错
a = {1, 2, 4, 5, 3, "a", "c", "b"}
print(a)
a.discard(3)
print(a)
a.discard(3)
print("@@" * 20)
# difference() 差集 set1.defference(set2) 返回set1 里面除了与set2 里面也有的 元素
# difference_update() 区别就是第一个返回一个新的集合, 第二个是把原来集合覆盖
a = {2, 3, 4, 7}
b = {2, 4, 6, 8, 7}
c = a.difference(b)
d = b.difference(a)
print(c)
print(d)
print("**" * 20)
a.difference_update(b)
print(a)
