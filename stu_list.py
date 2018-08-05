# 开始list 学习
# append() 在列表末尾 添加元素  返回值 None
list1 = [1, 2, 3, 4, 5]
print(list1)
print(list1.append(6))
print(list1)
print("@@" * 20)
# copy() 复制列表
list2 = list1.copy()
list3 = list1
print(list2)
print(id(list1))
print(id(list2))
print(id(list3))
print("@@" * 20)
# count() 计算某个元素作为列表中出现的次数
list1.append(1)
print(list1.count(1))
print("@@" * 20)
# extend() 将一个列表继承到另一个列表后 返回None
list1 = [7, 8, 9]
print(id(list1))
list2 = [1, 2, 3]
list1.extend(list2)
list2.extend(list1)
print(id(list1))
print(list1)
print(list2)
print("@@" * 20)
# index() 获取值在列表中的索引(多个满足条件的值 取第一个)
# index( value,[sta ,end]) 可以指定  查找范围
list1 = [1, 2, 3, 4, 3, 6, 7]
print(list1.index(2))
print(list1.index(3))
print(list1.index(3, 3, 6))
print("@@" * 20)
# insert() 在指定位置钱插入元素 2 个参数
# insert( sta, value)
list1 = [1, 2, 3, 4, 6]
list1.insert(4, 5)
print(list1)
print("@@" * 20)
# pop() 根据索引一处列表内一个元素 , 不给索引默认一处最后一个 返回移除的那个值
list1 = [1, 2, 3, 4, 5, 6]
print(id(list1))
print(list1.pop(2))
print(list1)
print(id(list1))
print("@@" * 20)
# remove() 移除列表中指定的值 返回None
list1 = [1, 2, 3, 4, 5, 6]
print(id(list1))
print(list1.remove(2))
print(list1)
print(id(list1))
print("@@" * 20)
# reverse() 列表反转
list1 = [1, 2, 3, 4]
print(id(list1))
print(list1.reverse())
print(list1)
print(id(list1))
print("@@" * 20)
# sort() 排序 默认从小到大 返回 None
list1 = [2, 3, 4, 6, 5, 1]
print(list1.sort())
print(list1)
# 从大到小
list1.sort(reverse=True)
print(list1)
print("@@" * 20)
# list 结束