# python3 products.py
# 如何将多个清单放在一起
# 如何写入档案

products = []

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
products[0][0]	# 大清单的第0格 + 小清单的第0格

for p in products:
	print('The price of', p[0], 'is $', p[1])	# 输出每个小清单
	# 假如p[0]是数字，则以str(p[0])写入print
# f.write.py

# String 可以合并
# 'abc' + '123' = 'abc123'
# 'abc' * 3 = 'abcabcabc'

with open ('products.csv', 'w', encoding = 'utf-8') as f: # 也可以用txt等等
								# 使用utf-8语言编码防止输入中文乱码, 
								# 如果输出显示仍然有问题，需要在excel的data中对读取文件的输出编码进行选择
	f.write('products, price \n')	# 加名称栏

	for p in products:
		f.write(p[0] + ',' + p[1] + '\n') # 每一项都是字串，写入进file
		# ',' 将字串分开存入excel的表中, 记得'\n'必须要加上
# with在loop结束时自动将档案关闭(python独有)












