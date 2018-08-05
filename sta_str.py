# 字符串得简单操作
# 连接操作
s1 = "i love"
s2 = " "
s3 = s1 + s2
print(s3)
print(s1 + " " + s2)

#  字符串得乘法

print(s1 * 5)

# 字符串当成列表
print(s1[1])
print(s1[-1])
print(s1[2:4])
print(s1[:])
#  capitalize首字母大写 其余小写
s3 = "i love You "
print(s3.capitalize())

# title每个单词首字母大写
s4 = "i love you"
print(s4.title())
# upper字母全部大写
s5 = "i love you"
print(s5.upper())
# lower字母全部小写
s6 = "I LOVE YOU"
print(s6.lower())
# swapcase字母小写变大写 大写变小写
s7 = "I love YOU"
print(s7.swapcase())
# len 字符串长度空格也占位
print(len(s7))
# find() 查找指定字符串,找不到返回-1 第一次找到返回第一次索引值
# index() 查找制定字符串, 找不到报错
print(s7.find("w"))
print(s7.index("w"))

