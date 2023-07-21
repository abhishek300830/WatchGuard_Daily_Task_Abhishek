class FixedFloat:
    def __init__(self, amount):
        self.amount = amount
    
    def __repr__(self):
        return f"<FixedFloat {self.amount:.2f}>"

    @classmethod
    def sum(cls, value1, value2):
        return cls(value1+value2)

new_number = FixedFloat.sum(19,10)
print(new_number)

class Euro(FixedFloat):
    def __init__(self,amount):
        super().__init__(amount)
        self.symbol = "€"

    def __repr__(self):
        return f"<Euro {self.symbol}{self.amount:.2f}>"

money = Euro.sum(18.23243,121.1212)
print(money)