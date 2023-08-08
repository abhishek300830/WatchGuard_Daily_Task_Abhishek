def add_all(*args):
    return sum(args)

sum_of_all = add_all(1,2,3,4,5)
print(sum_of_all)

def preety_print(**kwargs):
    for k,v in kwargs.items():
        print(f"for {k} we have {v}")

preety_print(**{'username':'abhishek','access_level':'admin'})

preety_print(username='abhishek',access_level='admin')