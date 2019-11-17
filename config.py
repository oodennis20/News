import os

class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_SOURCE_URL='https://newsapi.org/v2/sources?apiKey={}'
    CAT_API_URL='https://newsapi.org/v2/everything?q={}&sortBy=relevancy&apiKey={}'
    NEWS_API_KEY=os.environ.get('NEWS_API_KEY')

    
class ProdConfig(Config):
    '''
    Production  configuration child class
    '''
    pass

class DevConfig(Config):
    '''
    Development  configuration child class
    '''
    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}