from collections import namedtuple

Account = namedtuple("Account_in_bank",["name","balance"])

account = Account('checking',1850.50)

print(account.name)
print(account.balance)
print(account)