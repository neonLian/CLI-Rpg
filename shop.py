from player import Player
import util as u
stockL = ['sword','bow','axe','staff']


class Shop():
	def __init__(self,money,stock,c,money_type,player_weapons,player):
		self.Player_money = money
		self.shop_money = 300
		self.stock = stock
		self.conn = c
		self.m_type = money_type
		self.player_weapons = player_weapons
		self.player = player
	def shop_state(self):
		u.s2c(self.conn,'we have %s %s' % (self.shop_money,self.m_type))
		u.s2c(self.conn,'we also have the folowing in stock')
		for x in self.stock:
			u.s2c(self.conn,x.name)
	def buy(self):
		u.s2c(self.conn,' what WOULD you like!?(input a number)')
		num = 0
		for x in self.stock:
			num += 1
			u.s2c(self.conn,'%s . %s this cost %s' % (str(num),x.name,str(x.price)))
		pick = u.rfc(self.conn)
		int(pick)
		player.add_weapon(stock[pick]).name
		player.money -= stock[pick].price
		

		

