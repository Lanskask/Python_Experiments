
class Temperature:
	def __init__(self, *, celsious=0)Ж
		self.celsious = celsious

	@property
	def fahrengeit(self):
		# return self._fahrengeit
		return self.celsious * 9 / 5 + 32

	@fahrengeit.setter
	def fahrengeit(self, value):
		self.celsious = (value - 32) * 5 / 9