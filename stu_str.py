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
#  capitalize*()首字母大写 其余小写
s3 = "i love You "
print(s3.capitalize())

# title()每个单词首字母大写
s4 = "i love you"
print(s4.title())
# upper()字母全部大写
s5 = "i love you"
print(s5.upper())
# lower()字母全部小写
s6 = "I LOVE YOU"
print(s6.lower())

# swapcase() 字母小写变大写 大写变小写
s7 = "I love YOU"
print(s7.swapcase())
# len 字符串长度空格也占位
print(len(s7))
# find() 查找指定字符串,找不到返回-1 第一次找到返回第一次索引值
# index() 查找制定字符串, 找不到报错
print(s7.find("w"))
#  print(s7.index("w"))
# count 计算字符串出现的次数, 返回整形
print(s7.count("o"))

# startswith()  检测是否以指定字母开头  返回布尔值
# endswith() 检测是否以指定字母结束
print(s7.startswith("I"))
print(s7.startswith("i"))
print(s7.endswith("u"))
print(s7.endswith("U"))
print("==" * 10)
# isupper() 检测所有字母是否为大写字母 返回布尔值
s8 = "L LOVE YOU"
s9 = "L love you"
s10 = "i love you"
print(s8.isupper())
print(s9.isupper())
print("==" * 10)
# islower() 检测所有字符串是否 为小写 返回布尔值
print(s8.islower())
print(s9.islower())
print(s10.islower())
print("==" * 10)
# istitle() 检测是否 每个单词首字母大写 返回布尔值
s11 = "I Love 你"
s12 = "I Love You"
print(s8.istitle())
print(s9.istitle())
print(s10.istitle())
print(s11.istitle())
print(s12.istitle())
print("==" * 10)

# isspace() 检测字符串是否是空字符串
s13 = "i love you"
s14 = " "
# 至少要有一个空字符,不然返回 Flase
s15 = ""
print(s13.isspace())
print(s14.isspace())
print(s15.isspace())
print("==" * 10)
# isalpha() 检测字符串 是否全部是字母组成 返回布尔值
# 有字符串 返回 Flase
s16 = "i love you"
s17 = "ilove你"
s18 = "i爱 you "
s19 = "我爱你"
print(s16.isalpha())
print(s17.isalpha())
print(s18.isalpha())
print(s19.isalpha())
print("==" * 10)
# isalnum() 检测字符串里面是否 仅有字母或者数字(汉字算是字母)组成 返回布尔值
# 有空字符串 就为 Flase
s20 = "iloveyou"
s21 = "ilove12314"
s22 = "12313"
s23 = "ilove#"
print(s20.isalnum())
print(s21.isalnum())
print(s22.isalnum())
print(s23.isalnum())
print("##" * 10)
# isdigit() 检测字符串是否只有数字组成
# isdecimal() 检测字符串是否 只包含十进制 字符
# isnumeric() 检测字符串是否 值由数字组成
s24 ="12314"
s25 ="123b"
s26 = "一二三"
print(s24.isdigit())
print(s25.isdigit())
print(s26.isdigit())
print("*" * 20)
print(s24.isdecimal())
print(s25.isdecimal())
print(s26.isdecimal())
print("*" * 20)
print(s24.isnumeric())
print(s25.isnumeric())
print(s26.isnumeric())
print("##" * 10)
# split() 用指定字符 切割字符串 返回有字符串 组成的列表
s27 = "i love you"
list1 = s27.split(" ")
print(list1)
print("##" * 10)
# splitline() 与换行 切割字符 返回字符串 组成的列表
s28 = """i
love
you
"""
print(s28.splitlines())
print("##" * 10)
# join() 将列表按照指定 字符串连接 返回连接后的字符串
list2 = ["i", "love", "you"]
print(" ".join(list2))
# ljust() 指定字符串的长度, 原字符串靠左边 不足的位置用指定字符填充 默认空格 返回字符串
# 指定字符串 长度 低于 原本字符串长度 返回原字符串
s29 = "i love you"
print(s29.ljust(50, "*"))
print("##" * 10)
# conter() 指定字符串长度 , 内容居中, 不足的位置 用指定字符填充, 默认空格 返回字符串
s30 = "i love you"
print(s30.center(50, "*"))
print(s30.center(50))
print("##" * 10)
# rjust()指定字符串的长度, 原字符串靠右边 不足的位置用指定字符填充 默认空格 返回字符串
print(s29.rjust(50, "*"))
print("##" * 10)
# strip() 去掉左右两边的指定字符,默认是去掉空格(有就去除 没有就默认)
s31 = "**i love you**"
s32 = "**i love you"
s33 = "i love you**"
s34 = "aaa*ccc"
print(s31.strip("*"))
print(s32.strip("*"))
print(s33.strip("*"))
print(s34.strip("*"))
print("**" * 10)
# lstrip() 去掉左边的指定字符,默认去掉空格
print(s31.lstrip("*"))
print(s32.lstrip("*"))
print(s33.lstrip("*"))
print(s34.lstrip("*"))
print("**" * 10)
# rstrip() 去掉右边的指定字符, 默认去掉空格
print(s31.rstrip("*"))
print(s32.rstrip("*"))
print(s33.rstrip("*"))
print(s34.rstrip("*"))
print("##" * 10)
# zfill() 指定字符串长度 原字符串 靠右 不足的位置用0 填充 超过指定长度 返回原字符串
s35 = "i love you"
print(s35.zfill(50))
print(s35.zfill(5))
print("##" * 10)
# maketrans() 生成用于字符串替换的映射表
# translete() 进行字符串的替换( 注:替换的字符要原字符长度一样)
s36 = "i love you"
table = s36.maketrans("you", "her")
print(s36.translate(table))
