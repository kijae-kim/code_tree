class Product:
    def __init__(self, product_code=50, product_name="codetree"):
        self.code = product_code
        self.name = product_name
    
    def ans(self):
        print(f"product {self.code} is {self.name}")

product_name, product_code = input().split()
product_code = int(product_code)

tmp1 = Product()
tmp2 = Product(product_code, product_name)
tmp1.ans()
tmp2.ans()