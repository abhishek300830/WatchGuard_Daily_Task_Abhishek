# index Error

friends = ["abhisehek", "Kunal"]
friends[2]

'''
Traceback (most recent call last):
  File "c:\Programming\WatchGuard_daily_task_Abhishek\Python-Complete-Course\July-24-2023\01-build-in-errors.py", line 4, in <module>
    friends[2]
    ~~~~~~~^^^
IndexError: list index out of range
'''

# Key Error
# when we use key which is not present in the dictionary.

dictionary = {
    'name':"abhishek",
}
dictionary["username"]

'''
Traceback (most recent call last):
  File "c:\Programming\WatchGuard_daily_task_Abhishek\Python-Complete-Course\July-24-2023\01-build-in-errors.py", line 20, in <module>
    dictionary["username"]
    ~~~~~~~~~~^^^^^^^^^^^^
KeyError: 'username'
'''


# Attribute Error
list1 = [1,2,3]
list2 = [3,4,5]

result = list1.intersection(list2)

