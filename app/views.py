from flask import render_template
from app import app
from .request import get_news

#Views
@app.route('/')
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

