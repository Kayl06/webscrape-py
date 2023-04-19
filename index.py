from Scraper import Scraper

scraper_params = {
    'url': 'https://www.bbc.com/news/world-asia-65307858',
    'title_tag': 'h1',
    'title_attr': {'id': 'main-heading'},
    'author_tag': 'div',
    'author_attr': {'class': 'ssrcss-68pt20-Text-TextContributorName'},
    'date_tag': 'time',
    'datetime_attr': {'data-testid': 'timestamp'},
    'date_attr': 'datetime',
    'content_tag': 'main',
    'content_attr': {'id': 'main-content'},
}


scraper = Scraper(scraper_params)

article_data = scraper.scrape_article()

print('Title:', article_data['title'])
print('Author:', article_data['author'])
print('Published Date:', article_data['published_date'])
print('Content:', article_data['content'])
