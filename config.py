import os


class Config:
    '''
    import secret keys from os
    set up database uri
    set up mailconfigurations
    
    
    '''
    RECIPE_URL= 'https://api.spoonacular.com/recipes/findByIngredients?apiKey={}&ingredients={},+{},+{}&number=10'
    RECIPE_API_KEY= os.environ.get('RECIPE_API_KEY')
    
    SECRET_KEY=os.environ.get('SECRET_KEY')


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://moringa:Access@localhost/recipe"
    DEBUG = True


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "")
    if SQLALCHEMY_DATABASE_URI.startswith('postgres://'):
           SQLALCHEMY_DATABASE_URI=SQLALCHEMY_DATABASE_URI.replace('postgres://','postgresql://',1)


config_options = {
  'development' : DevConfig,
  'production'  : ProdConfig
}