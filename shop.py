from player import Player

stockL = ['sword','bow','axe','staff']


class Shop():
	def __init__(self,money,stock):
		self.Player_money = money
		self.shop_money = 300
		self.stock = stock
	def intro(self):
		print('Hello, wellcome to the shop.')
	def shop_state(self):
		print('we have %s %s' % (self.shop_money,Player1.currency))
		print('we also have the folowing in stock')
		for x in self.stock:
			print(x)

Player1 = Player(0,"",'pocket lint','john')			
shop1 = Shop(Player1.money,stockL)		
shop1.intro()
shop1.shop_state()
