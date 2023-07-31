from datetime import datetime,timezone, timedelta

print(datetime.now())

today = datetime.now(timezone.utc)
print(today)

tomorrow = today + timedelta(days=1)
print(tomorrow)

print(today.strftime('%d-%m-%Y, %H:%M:%S'))

user_date = input("Enter data in YYYY-mm-dd format : ")

user_date = datetime.strptime(user_date,"%Y-%m-%d")
print(user_date)