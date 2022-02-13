from bs4 import BeautifulSoup
import requests
import fake_useragent

URL = 'https://tjournal.ru/'
USER = fake_useragent.FakeUserAgent().random
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'user_agent': USER
}


def get_html(url, params=''):
    html = requests.get(url, headers=HEADERS, params=params)
    return html


def get_content(html):
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all('div', class_='news_item l-flex l-fa-baseline lm-block l-mv-9 lm-mv-8')
    data = []
    for item in items:
        data.append(
            {
                'time': item.find('time').get_text(strip=True),
                'title': item.find('a').get_text(strip=True),
                'href': item.find('a').get('href')


            }
        )
    return data


html = get_html(URL)
tjournal = get_content(html.text)