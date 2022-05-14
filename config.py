from distutils.debug import DEBUG
import os
class Config:
  '''
  '''
  SECRET_KEY='1234'
  SQLALCHEMY_TRACK_MODIFICATIONS = False 
  # SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://postgres:whalien52@localhost/blog'
  
class ProdConfig(Config):
  '''
  '''
  SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL").replace(':///',"ql:///", 1)
 

class DevConfig(Config):
  '''
  '''
  # SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://postgres:whalien52@localhost/blog'
DEBUG=True  

config_options = {
  'development':DevConfig,
  'production' :ProdConfig
}
