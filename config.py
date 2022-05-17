import os
class Config:
  '''
  '''
  SECRET_KEY='1234'
  SQLALCHEMY_TRACK_MODIFICATIONS = False 
  SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://postgres:whalien52@localhost/blogsss'
  
class ProdConfig(Config):
  '''
  '''
  uri = os.getenv("DATABASE_URL")  
  if uri and uri.startswith("postgres://"):
     uri = uri.replace("postgres://", "postgresql://", 1)
     SQLALCHEMY_DATABASE_URI=uri
    
class DevConfig(Config):
  '''
  '''
  SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://postgres:whalien52@localhost/blogsss'
DEBUG=True  

config_options = {
  'development':DevConfig,
  'production' :ProdConfig
}
