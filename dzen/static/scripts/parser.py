from bs4 import BeautifulSoup
import requests
import fake_useragent

URL = 'https://m.lenta.ru'
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
    items = soup.find_all('a', class_='card-mini')
    data = []
    for item in items:
        if 'moslenta' not in item.get('href'):
            data.append(
                {
                    'href': URL + item.get('href'),
                    'time': item.find('time', class_="card-mini__date").get_text(strip=True),
                    'title': item.find('div', class_="card-mini__title").get_text(strip=True),
                }
            )
    return data


html = get_html(URL)
lenta = get_content(html.text)