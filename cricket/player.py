from random import randrange


class Player(object):
	"""docstring for Player"""
	def __init__(self, score=0):
		self.score = 0
		self.strike = 0

	def player_score_update(self, new_score):
		self.score += new_score

	def make_strike(self):
		self.strike = randrange(6)

	def reset_player_score(self):
		self.score = 0