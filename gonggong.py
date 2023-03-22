str1 = input('请输入第一个字符串：')
str2 = input('请输入第二个字符串：')
str3 = ''
for i in str1:
    if i in str2:
        if i not in str3:
            str3 += i
print("公共字符有："+str3)
