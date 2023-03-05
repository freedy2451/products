#讀取檔案
products = []
with open('product.csv', 'r', encoding = 'utf-8') as f:
    for line in f:
        if '商品,價格' in line:
            continue #跳到下一輪迴圈
        name, price = line.strip('\n').split(',')
        products.append([name, price])
print(products)        

while True:
    name = input("請輸入商品名稱: ")
    if name == "q":
        break
    price = input("請輸入價格: ")        
    products.append([name,price])

for p in products:
    print("商品名稱為" + p[0] + ", 價格為" + p[1])

    
with open('product.csv', 'w', encoding = 'utf-8') as f:
     f.write('商品,價格\n')
     for p in products:        
        f.write(p[0] + ',' + p[1] + '\n')

