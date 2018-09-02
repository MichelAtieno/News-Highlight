from flask import render_template, redirect, url_for, request
from . import main
from ..request import get_news, get_articles, search_articles
from ..models import Articles

#Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    #Getting news
    general_news = get_news('general')
    business_news = get_news('business')
    entertainment_news = get_news('entertainment')  
    health_news = get_news('health')
    science_news = get_news('science')
    sports_news = get_news('sports')
    technology_news = get_news('technology')


    title = 'Get the latest news in the World'
    return render_template('index.html', title = title, general = general_news, business = business_news, entertainment = entertainment_news, health = health_news, science = science_news, sports= sports_news,technology = technology_news )

@main.route('/articles/<source_id>&<int:per_page>')
def articles(source_id,per_page):
    '''
    Function that returns articles
    '''

    news_source = get_articles(source_id, per_page)
    title = f'{source_id} | ARTICLES ' 
    return render_template('articles.html', title= title, name=source_id, all_news = news_source)

@main.route('/search/<topic>')
def search(topic):
    '''
    Function that returns result of search topic
    '''
    per_page = 40
    search_name = topic.split(' ')
    search_name_format = "+".join(search_name)
    search_all = search_articles(per_page,search_name_format)

    title = f'search results for {search_name_format}'

    return render_template('search.html', title = title, all_news = search_all)

