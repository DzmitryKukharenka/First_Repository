class product:
    def __init__(self,weight,price,timelife):
        self.weight = weight
        self.price = price
        self.timelife = timelife
    
    
class fruit(product):
        def __init__(self,weight,price,timelife):
            super().__init__(weight,price,timelife)
        def viewWeight(self):
            print(f'Вес продукта:{self.weight} грамм.')
        def viewPrice(self):
            print(f'Стоимость продукта:{self.price} рублей.')
        def viewTimelife(self):
            print(f'Срок годности продукта:{self.timelife} суток.')
class lemonade(product):
        def __init__(self,weight,price,timelife):
            super().__init__(weight,price,timelife)
        def viewWeight(self):
            print(f'Вес продукта:{self.weight} грамм.')
        def viewPrice(self):
            print(f'Стоимость продукта:{self.price} рублей.')
        def viewTimelife(self):
            print(f'Срок годности продукта:{self.timelife} суток.')
class cookie(product):
        def __init__(self,weight,price,timelife):
            super().__init__(weight,price,timelife)
        def viewWeight(self):
            print(f'Вес продукта:{self.weight} грамм.')
        def viewPrice(self):
            print(f'Стоимость продукта:{self.price} рублей.')
        def viewTimelife(self):
            print(f'Срок годности продукта:{self.timelife} суток.')

apple = fruit(200,15,1)
apple.viewWeight()
apple.viewPrice()
apple.viewTimelife()

fanta = lemonade(1000,10,730)
crackers = cookie(500,5,365)