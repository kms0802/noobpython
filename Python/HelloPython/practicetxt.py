class Product:
    def __init__(self,name, stock):
        self.name = name
        self._stock = stock
    
class Book(Product):
    def __init__(self, name, stock):
        super().__init__(name, stock)
        self._stock -= 1
    
    def show_stock(self):
        print(f"{self.name} {self._stock}")

book = Book("파이썬 마스터", 10)
book.show_stock()