import os


class Config:
    '''
    import secret keys from os
    set up database uri
    set up mailconfigurations
    
    
    '''
    pass


class DevConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    pass


config_options = {
  'development' : DevConfig,
  'production'  : ProdConfig
}