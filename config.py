import os

class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&pageSize={}&apiKey={}'
    ARTICLES_SEARCH_URL = 'https://newsapi.org/v2/everything?q={}&pageSize={}&apiKey={}'

    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig:
    '''
    Production Configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
