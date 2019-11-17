class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_SOURCE_URL='https://newsapi.org/v2/sources?apiKey={}'
    CAT_API_URL='https://newsapi.org/v2/everything?q={}&sortBy=relevancy&apiKey={}'
    API_KEY=os.environ.get('API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
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