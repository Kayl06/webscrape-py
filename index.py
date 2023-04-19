from Scraper import Scraper

scraper_params_arr = [
    {
        'url': 'https://www.newyorker.com/news/annals-of-communications/the-stunning-end-of-dominions-case-against-fox-news',
        'title_tag': 'h1',
        'title_attr': {'data-testid': 'ContentHeaderHed'},
        'author_tag': 'a',
        'author_attr': {'class': 'byline__name-link'},
        'date_tag': 'time',
        'datetime_attr': {'data-testid': 'ContentHeaderPublishDate'},
        'date_attr': 'datetime',
        'content_tag': 'main',
        'content_attr': {'id': 'main-content'},
    },
    {
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
    },
    {
        'url': 'https://edition.cnn.com/2023/04/18/media/fox-dominion-settlement/index.html',
        'title_tag': 'h1',
        'title_attr': {'class': 'headline__text'},
        'author_tag': 'div',
        'author_attr': {'class': 'ssrcss-68pt20-Text-TextContributorName'},
        'date_tag': 'time',
        'datetime_attr': {'data-testid': 'timestamp'},
        'date_attr': 'datetime',
        'content_tag': 'main',
        'content_attr': {'id': 'main-content'},
    }

]

for idx, scraper in enumerate(scraper_params_arr):
    scraper = Scraper(scraper)
    article_data = scraper.scrape_article()
    idx+=1;

    print('\n================ Article #' + str(idx) + ': ' + article_data['title'] + ' ================')
    print('\n')
    print('Title:', article_data['title'])
    print('Author:', article_data['author'])
    print('Published Date:', article_data['published_date'])
    print('Content:', article_data['content'])
    print('\n================ End of Article #' + str(idx) + ' ================')
    print('\n')
