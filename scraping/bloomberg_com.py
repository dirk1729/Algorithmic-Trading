from bs4 import BeautifulSoup
import pandas as pd
import requests

def get_article(data):
    return dict(
        headline=data.get_text(),
        link='https://www.bloomberg.com' + data['href']
    )

def bloomberg_com():
    
    headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
    "referer": "https;//google.com",
    "Accept-Encoding": "gzip, deflate, br",
    "Pragma":"no-cache"
    }

    resp = requests.get("https://www.bloomberg.com/fx-center", headers=headers)

    print(resp.content)
    print(resp.status_code)

    soup = BeautifulSoup(resp.content, 'html.parser')

    all_links = []

    headline = soup.select_one(".single-story-module__headline-link")
    all_links.append(get_article(headline))

    grid_articles = soup.select(".grid-module-story__headline-link")
    [all_links.append(get_article(x)) for x in grid_articles]

    side_articles = soup.select(".story-list-story__info__headline-link")
    [all_links.append(get_article(x)) for x in side_articles]

    return all_links
