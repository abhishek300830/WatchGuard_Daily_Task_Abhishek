accounts = {
    'checking':1959.00,
    'saving':3695

}

def add_balance(amount:float,name:str = 'checking') -> float:
    accounts[name] += amount
    return accounts[name]


transactions = {
    (239.0,'checking'),
    (249.0,'checking'),
    (3339.0,'checking'),
    (2539.8,'saving'),
}

for t in transactions:
    add_balance(*t)

print(accounts['saving'])
print(accounts['checking'])