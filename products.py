# python3 products.py
# 如何将多个清单放在一起

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
