from bs4 import BeautifulSoup
import requests

# headers helps to get the actual website
url = "https://www.amazon.com/dp/B084RTQ3Y9/ref=va_live_carousel?pf_rd_r=CEPA7CXHSS9737SY7PWW&pf_rd_p=14936841-ca05-4835-b3bf-87617ecd98a6&pf_rd_m=ATVPDKIKX0DER&pf_rd_t=Detail&pf_rd_i=B09V9QZY9J&pf_rd_s=desktop-dp-sims&pd_rd_w=bgJdC&pd_rd_r=c3eadac3-e1d0-4d00-afa2-b7ceb8e14fc4&pd_rd_wg=6L4Ly&linkCode=ilv&tag=onamzfkx-20&ascsubtag=Christmas_Shopping_221227022554&asc_contentid=amzn1.amazonlive.broadcast.f6936b93-bab7-4171-9306-f14f6ab813f5&pd_rd_i=B084RTQ3Y9&th=1&psc=1"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,ar-AE;q=0.8,ar;q=0.7,zh-CN;q=0.6,zh;q=0.5"
}
response = requests.get(url=url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
product_title = soup.find(name="span", id="productTitle").getText().strip()
price = soup.find(name="span", class_="a-offscreen")
price_float = float(price.getText()[1:])

# if current price is lower than targeted price, send a mail
BUY_PRICE = 100
if price_float < BUY_PRICE:
    message = f"{product_title} is now {price_float}"
    print(message)