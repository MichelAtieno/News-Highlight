import urllib.request,json
from .models import News, Articles

#Getting api key
api_key= None
#Getting the news base url
base_url = None
#Getting the articles url
articles_url = None
#Getting the search url
articles_search_url = None

def configure_request(app):
    global api_key,base_url,articles_url,articles_search_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    articles_url = app.config['ARTICLES_BASE_URL']
    articles_search_url = app.config ['ARTICLES_SEARCH_URL']

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

def get_articles(source_id, per_page):
    '''
    Function that gets articles 
    '''
    get_articles_url = articles_url.format(source_id,per_page,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results=process_articles(get_articles_response['articles'])

    return articles_results

def process_articles(all_articles):
    '''
    Function that processes the json result and transforms them to a list of objects 
    '''
    articles_list = []

    for article in all_articles:
        id = article.get('id')
        name = article.get('name')
        author = article.get('description')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')        
        urlToImage = article.get('urlToImage')
        publishedAt = article.get('publishedAt')

        if urlToImage:
            article_object = Articles(id,name,author,title,description,url,urlToImage,publishedAt)
            articles_list.append(article_object)
            
    return articles_list

def search_articles(per_page, query):
    '''
    Function that looks for articles
    '''
    search_articles_url = articles_search_url.format(query, per_page, api_key)
    with urllib.request.urlopen(search_articles_url) as url:
        search_articles_data = url.read()
        search_articles_response = json.loads(search_articles_data)

        search_articles_results = []

        if search_articles_response['articles']:
            search_articles_results = process_articles(search_articles_response['articles'])

    return search_articles_results