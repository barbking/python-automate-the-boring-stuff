# Price check from Amazon

import bs4
import requests

def getAmazonPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('<span class="a-size-medium a-color-price offer-price a-text-normal">$28.49</span>')
    return elems[0].text.strip()


price = getAmazonPrice('https://www.amazon.com/Automate-Boring-Stuff-Python-2nd/dp/1593279922/ref=dp_ob_title_bk')
print('The price is ' + price)