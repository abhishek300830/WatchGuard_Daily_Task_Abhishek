accounts = {
    'checking':1959.00,
    'saving':3695

}

def add_balance(amount:float,name:str = 'checking') -> float:
    accounts[name] += amount
    return accounts[name]

# add_balance(500.00,'saving')
add_balance(500.00)

# print(accounts['saving'])
print(accounts['checking'])