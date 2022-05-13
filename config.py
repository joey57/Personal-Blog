import os
class Config:
  '''
  '''
  SECRET_KEY='1234'

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
