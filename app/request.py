from app import app
import urllib.request,json
from .models import news

News = news.News
Articles = 

#Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the news base url
base_url = app.config['NEWS_API_BASE_URL']

def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        news_results = None
        
        if get_news_response['sources']:
            news_results = process_results(get_news_response['sources'])
    
    return news_results

def process_results(news_list):
    '''
    Function that processes json results
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item['url']
        category = news_item['category']
        country = news_item['country']
        #print(url)
        if url:
            news_object = News(id, name, description, url, category, country)
            news_results.append(news_object)

    return news_results  

def get_articles(id):
    '''
    Function that gets articles 
    '''
    get_articles_url = articles_url.format(id,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']


            