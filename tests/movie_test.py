import unittest
from app.models import Movie

class MovieTest(unittest.TestCase):
	"""
	Test clas to test the behavior of the Movie clas
	"""
	def setUp(self):
		"""
		set up  method  will run before every test
		"""
		self.new_movie = Movie(1234,'Flask is an adventure','A thrilling new python series','https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993)

	def test_instance(self):
		self.assertTrue(isinstance(self.new_movie,Movie))
