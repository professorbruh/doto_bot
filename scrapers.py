from urllib.request import urlopen , Request
from bs4 import BeautifulSoup as soup

def hero_call(name):
    url = 'https://www.dotabuff.com/heroes/' + name
    hdr = {'User-Agent': 'super happy flair bot'}
    uClient = Request(url,headers=hdr)
    page_html = urlopen(uClient).read()
    parsed_page = soup(page_html,"html.parser")
    win_rate = parsed_page.find("span",class_ = 'lost')
    print(type(win_rate.text))
    if win_rate.text is None:
        win_rate = parsed_page.find('span',class_='won')

    return win_rate.text

