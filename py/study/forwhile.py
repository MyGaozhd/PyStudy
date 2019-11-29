print("开始while循环")

i = 0
while i < 9:
    print("当前值：", i)
    i += 1
else:
    print("跳出循环:", "当前值：", i, "大于9")
print("结束while循环")

print()

print("开始for循环", "开始")

for letter in "python":
    print("当前字母是：", letter)

let = ["我", "今年", 18]

for k in let:
    print(k)

print("结束for循环", "结束")

print("开始 - - - 索引 - - - for循环", "开始")

fruits = ["banana", "apple", "orange"]

for index in range(len(fruits)):
    print(fruits[index])

print("结束 - - - 索引 - - - for循环", "结束")
