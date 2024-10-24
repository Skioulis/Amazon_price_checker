import requests
from bs4 import BeautifulSoup

practice_url = "https://appbrewery.github.io/instant_pot/"
live_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

response = requests.get(practice_url)
# response = requests.get(live_url)
response.raise_for_status()

static_site = response.text

soup = BeautifulSoup(static_site, 'html.parser')

result = soup.find(name="span", class_="aok-offscreen")

scrapped_price = float(result.getText().replace('$', ''))

print(scrapped_price)
