 # 📰 BBC News Scraper

A modular and scalable Python project to scrape articles from the [BBC News](https://www.bbc.com/news) homepage using `requests`, `BeautifulSoup`, and `newspaper3k`.

---

## 📦 Features

- Modular architecture for easy maintenance and extension
- Extracts article links and full content
- Retrieves article metadata (title, author, publish date)
- Cleans and structures scraped data
- Outputs results as JSON
- Easily extendable to support other news sources

---

## 📁 Project Structure

```
.
├── article_extractor.py
├── config.py
├── fetcher.py
├── __init__.py
├── main.py
└── parser.py
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/GABRIELENN/webscrapping.git
cd webscraping
```
## install dependencies
```
pip install requests beautifulsoup4 newspaper3k
```
## Run Scarpper
```
python main.py
```
## 🛠️ Future Improvements
Add database integration (e.g., SQLite, MongoDB)

- Build a REST API with Flask or FastAPI
- Add CLI interface for custom scrapes
- Schedule with cron or APScheduler
- Extend to other BBC sections or other news sources

## 🤝 Contributing
Contributions are welcome! Please open an issue or submit a pull request with improvements, bug fixes, or suggestions.

## 📄 License
This project is licensed under the MIT License.

## ✨ Acknowledgements
BBC News
     
                       
                           
                         
                  
              
      
               
               
         
 
