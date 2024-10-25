import requests
from bs4 import BeautifulSoup
import sent_email as se

practice_url = "https://appbrewery.github.io/instant_pot/"
live_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

# Scraping
response = requests.get(practice_url)
# response = requests.get(live_url)
response.raise_for_status()
static_site = response.text

soup = BeautifulSoup(static_site, 'html.parser')

# getting the curent price
result_price = soup.find(name="span", class_="aok-offscreen")
scrapped_price = float(result_price.getText().replace('$', ''))
item = soup.find(id="productTitle").get_text().strip(' ').replace("  ", '').split('\n')[0]

target_price= 100

if scrapped_price <target_price:
    se.sent_email(f"{item} is below to target price: {target_price}$ at {scrapped_price}$")
    print("its lower") # TODO: Delete
else: print("not lower") # TODO: Delete



print("ok")
