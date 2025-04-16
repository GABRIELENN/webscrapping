from newspaper import Article

def extract_article_data(url):
    article = Article(url)
    try:
        article.download()
        article.parse()
        return {
            "title": article.title,
            "author": article.authors,
            "publish_date": article.publish_date,
            "text": article.text,
            "url": url
        }
    except Exception as e:
        print(f"Failed to extract {url}: {e}")
        return None
