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
# 首字母大写 其余小写
s3 = "i love You "
print(s3.capitalize())
# 每个单词首字母大写
s4 = "i love you"
print(s4.title())
# 字母全部大写
s5 = "i love you"
print(s5.upper())
# 字母全部小写
s6 = "I LOVE YOU"
print(s6.lower())
# 字母小写变大写 大写变小写
s7 = "I love YOU"
print(s7.swapcase())


