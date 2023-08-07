import requests
import time


from libs.openexchange import OpenExchangeClient

APP_ID = "38ec7f69b651466dbb0078d054a7ca05"

client = OpenExchangeClient(APP_ID)

usd_amount = 1000

start = time.time()
gbp_amount = client.convert(usd_amount, "USD", "GBP")
print("Time Taken : ",time.time()-start)

start = time.time()
gbp_amount = client.convert(usd_amount, "USD", "GBP")
print("Time Taken : ",time.time()-start)

start = time.time()
gbp_amount = client.convert(usd_amount, "USD", "GBP")
print("Time Taken : ",time.time()-start)

print(f"USD {usd_amount} is GBP {gbp_amount}")
