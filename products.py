# python3 products.py
# 记账本

products = []

# 4/25检查是否已有products.csv存在
import os	# 载入operating system操作系统模组，例如windows，android，apple，linux
			# 给这段程序码权限检查电脑文件
if os.path.isfile('products.csv'):	# 查询路径的isfile功能，寻找file
	print('The file already exists...')

# 4/25文件存在的情况下读取档案并切割
	with open('products.csv', 'r', encoding = 'utf-8') as f:
		for line in f: # 将前几天创建的csv文件中的每一行每一行取名为line
			if 'name, price' in line:
				continue	# 跳过name和price，读取下一行
				name, price = line.strip().split(',') # 将','当做切割的标志，记得要去掉(strip)换行符号'\n'
		# 不用额外取函数，直接将清单列表[X, X]存入[name, price]
		# print(s), split输出之后是清单格式[]
			products.append([name, price])
	print(products)
else:
	print('The file does not exists... Please enter the name of products and price.')




# 4/23如何将多个清单放在一起
# 让使用者输入
while True:
	name = input('Please enter product name.')
	if name == 'q':
		break
	price = input('Please enter the price of product.')
#	p = []	# 建立小清单
#	p.append(name)	# 将两项分别加入p中
#	p.append(price)
	p = [name, price]
	products.append(p) #将p加入products
	# 简写法: products.append([name, price])
print(products)	# 输出大清单

# 存取清单 
# products[0][0]	# 大清单的第0格 + 小清单的第0格

# 输出购买记录
for p in products:
	print('The price of', p[0], 'is $', p[1])	# 输出每个小清单
	# 假如p[0]是数字，则以str(p[0])写入print
# f.write.py

# String 可以合并
# 'abc' + '123' = 'abc123'
# 'abc' * 3 = 'abcabcabc'

# 将购买记录写成csv or txt文件
with open ('products.csv', 'w', encoding = 'utf-8') as f: # 也可以用txt等等
								# 使用utf-8语言编码防止输入中文乱码, 
								# 如果输出显示仍然有问题，需要在excel的data中对读取文件的输出编码进行选择
	f.write('name, price \n')	# 加名称栏

	for p in products:
		f.write(p[0] + ',' + p[1] + '\n') # 每一项都是字串，写入进file
		# ',' 将字串分开存入excel的表中, 记得'\n'必须要加上
# with在loop结束时自动将档案关闭(python独有)













