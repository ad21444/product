import os

def read_file(thefile):
	products = []
	if os.path.isfile(thefile):
	#read files
		with open(thefile , 'r' , encoding='utf-8') as f:
			for line in f:
				if '商品,價格' in line:
					continue
				name,price = line.strip().split(',')
				products.append([name,price])
		print(products)
		return products
	else:
		print('找不到檔案，將建立新檔案')
		return products
		
def write_list(products):
	#input and save it
	while True:
		name = input('請輸入商品名稱')
		print('字母q為退出之意')
		if name == 'q':
			break
		price = input('請輸入商品價格')
		price = int(price)
		products.append([name,price])
		print(products)
		return products

def print_list(products):
	for p in products:
		print(p[0],'price is',p[1])		

def write_file(thefile, products):
	with open (thefile, 'w' , encoding='utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
	products = read_file('products.csv')
	products = write_list(products)
	print_list(products)
	write_file('products.csv' , products)

main()
'''
重點:
理想的function應該"只做一件事"
,所以refactor(重構程式)的核心概
念,就是把程式碼不斷的改寫,寫
成越來越小的function,讓
function"盡量"只做一件事。
程式最好有main function 為程
式的進入點
'''