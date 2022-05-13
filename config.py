import os
class Config:
  '''
  '''
  SECRET_KEY='1234'
  SQLALCHEMY_TRACK_MODIFICATIONS = False 
  SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://postgres:whalien52@localhost/blog'

class ProdConfig(Config):
  '''
  '''
  pass

class DevConfig(Config):
  '''
  '''
  pass

config_options = {
  'development':DevConfig,
  'production' :ProdConfig
}
