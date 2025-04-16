from fetcher import fetch_homepage, get_soup
from parser import extract_article_links
from article_extractor import extract_article_data
import json

def main():
    html = fetch_homepage()
    soup = get_soup(html)
    links = extract_article_links(soup)
    articles = []

    for link in links:
        data = extract_article_data(link)
        if data:
            articles.append(data)

    print(json.dumps(articles, indent=2, default=str))

if __name__ == "__main__":
    main()
