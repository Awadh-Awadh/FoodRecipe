import os


class Config:
    '''
    import secret keys from os
    set up database uri
    set up mailconfigurations
    
    
    '''
    RECIPE_URL= 'https://api.spoonacular.com/recipes/findByIngredients?apiKey={}&ingredients={},+{},+{}&number=10'
    RECIPE_API_KEY= os.environ.get('RECIPE_API_KEY')
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://moringa:Access@localhost/recipe"
    SECRET_KEY=os.environ.get('SECRET_KEY')


class DevConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    pass


config_options = {
  'development' : DevConfig,
  'production'  : ProdConfig
}