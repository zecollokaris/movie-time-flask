import os

class Config:
	"""
	General configuration parent class
	"""
	MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
	SECRET_KEY = os.environ.get('SECRET_KEY')
	MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
	SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://karis:karis@localhost/watchlist'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	pass

class ProdConfig(Config):
	"""
	Production configuration child class
	Args:
		Config:The parent configuration class with general configuration settings

	"""
	pass

class DevConfig(Config):
	"""
	Development configuration child class

	Args:
		Config: the parent configuration class with general configuration settings
	"""
	DEBUG= True

config_options  = {
'development':DevConfig,
'production':ProdConfig
}
