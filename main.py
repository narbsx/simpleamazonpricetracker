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
response = requests.get(URL, headers={"User-Agent":YOUR USER AGENT,
                                      "Accept-Language": YOUR ACCEPTED LANGUAGE})
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
        from_=YOUR TWILIO PHONE NUMBER,
        to=YOUR PHONE NUMBER
    )
