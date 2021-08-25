import os


class Config:
    '''
    import secret keys from os
    set up database uri
    set up mailconfigurations
    
    
    '''
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://moringa:Access@localhost/recipe"


class DevConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    pass


config_options = {
  'development' : DevConfig,
  'production'  : ProdConfig
}