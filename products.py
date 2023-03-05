import os 

#讀取檔案
def read_file(filename):
    products = []
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue #跳到下一輪迴圈
            name, price = line.strip('\n').split(',')
            products.append([name, price])
    return products
        
#請使用者輸入
def user_input(products):
    while True:
        name = input("請輸入商品名稱: ")
        if name == "q":
            break
        price = input("請輸入價格: ")        
        products.append([name,price])
    print(products) 
    return products   

#印出購買紀錄
def print_products(products):
    for p in products:
        print("商品名稱為" + p[0] + ", 價格為" + p[1])

#寫入檔案
def write_file(filename, products):
    with open(filename, 'w', encoding = 'utf-8') as f:
         f.write('商品,價格\n')
         for p in products:        
            f.write(p[0] + ',' + p[1] + '\n')
def main():
    filename = 'product.csv'
    if os.path.isfile(filename) : #檢查檔案在不在
        print('Find the file')
        products = read_file(filename)        
    else:
        print("It can't find the file.")  

    products = user_input(products)
    print_products(products)
    write_file('product.csv', products)


if __name__ == '__main__':
    main()

