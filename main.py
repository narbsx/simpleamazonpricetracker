import requests
from bs4 import BeautifulSoup
import pprint
from twilio.rest import Client
import os
import lxml

# URL = "https://www.amazon.com/Arzopa-Portable-100-SRGB-External-Speakers/dp/B093GCL18V/ref=sr_1_3?keywords=Laptop" \
#       "+Monitor&qid=1645476673&sr=8-3 "
# TARGET_PRICE = float(100)
URL = input("Copy and paste the link of the product you wish to keep track of: ")
TARGET_PRICE = float(input("What price do you want to buy the item at?: Enter a number: "))
response = requests.get(URL, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
                                      "Accept-Language": "en-US,en;q=0.9"})
amazon_page = response.text
pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(amazon_page)
soup = BeautifulSoup(amazon_page, "lxml")
price_whole = soup.find(name="span", class_="a-offscreen")
name = soup.find(name="span", class_="a-size-large product-title-word-break")
product_name = name.getText().strip()
price = float(price_whole.get_text().split("$")[1])

account_sid = os.environ["account_sid"]
auth_token = os.environ["auth_token"]

if price < TARGET_PRICE:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=f"{product_name} is now {price}.\n{URL}.",
        from_="+18548889151",
        to="+18582088079"
    )