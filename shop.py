from player import Player
import util as u
stockL = ['sword','bow','axe','staff']


class Shop():
	def __init__(self,money,stock,c,money_type):
		self.Player_money = money
		self.shop_money = 300
		self.stock = stock
		self.conn = c
		self.m_type = money_type
	def intro(self):
		print('Hello, wellcome to the shop.')
	def shop_state(self):
		u.s2c(self.conn,'we have %s %s' % (self.shop_money,self.m_type))
		u.s2c(self.conn,'we also have the folowing in stock')
		for x in self.stock:
			u.s2c(self.conn,x.name)

