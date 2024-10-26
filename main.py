import requests
from bs4 import BeautifulSoup
import sent_email as se

practice_url = "https://appbrewery.github.io/instant_pot/"
live_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GR,en;q=0.9,el-GR;q=0.8,el;q=0.7,en-GB;q=0.6,en-US;q=0.5",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
}

# Scraping
response = requests.get(practice_url, headers=header)
# response = requests.get(live_url, headers=header)
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
