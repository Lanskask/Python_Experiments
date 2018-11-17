# print ("Hello World")

class Card(object):
	def __init__(self, suit, val):
		self.suit = suit
		self.value  = val

	def show(self):
		print ('{} of {}'.format(self.value, self.suit))


class Deck(object):
	"""docstring for Deck"""
	def __init__(self):
		super(Deck, self).__init__()
		self.build()

	def build(self):
		for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
			for v in range(1, 14):
				print ('{} of {}'.format(v, s))

class Player(object):
	"""docstring for Player"""
	def __init__(self, arg):
		super(Player, self).__init__()
		self.arg = arg
		

# card = Card("clubs", 6)
# card.show()

deck = Deck()
