from urllib.parse import urljoin
from .config import BBC_BASE_URL

def extract_article_links(soup, limit=10):
    links = []
    for tag in soup.find_all("a", href=True):
        href = tag['href']
        if "/news/" in href and not href.startswith("https://") and not any(x in href for x in ["/live", "#"]):
            full_url = urljoin(BBC_BASE_URL, href)
            if full_url not in links:
                links.append(full_url)
        if len(links) >= limit:
            break
    return links
