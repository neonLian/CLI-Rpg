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
		print(type(self.player_weapons))
	def shop_state(self):
		u.s2c(self.conn,'we have %s %s' % (self.shop_money,self.m_type))
		u.s2c(self.conn,'we also have the folowing IN stock')
		for x in self.stock:
			u.s2c(self.conn,x.name)
	def buy(self):
		u.s2c(self.conn,' what WOULD you like!?(input a number)')
		num = -1
		for x in self.stock:
			num += 1
			u.s2c(self.conn,'%s . %s this costs %s %s' % (str(num),x.name,str(x.price),self.m_type))
		pick = u.rfc(self.conn)
		pick = int(pick)
		self.temp_wep = self.stock[pick].name
		self.Player_money -= self.stock[pick].price
		u.s2c(self.conn,'you have %s %s.' % (str(self.Player_money),self.m_type))
	def sell(self):
		u.s2c(self.conn,'what would YOU like to sell!?')
		num = 0
		for x in self.player_weapons.values():
			u.s2c(self.conn,'%s. you CAN sell %s for %s %s' % (str(num),x.name, str(x.price),self.m_type))
			num += 1
		pick = u.rfc(self.conn)
		pick = int(pick)
		self.Player_money += list(self.player_weapons.values())[pick].price
		list(self.player_weapons.values()).pop(pick)
		u.s2c(self.conn,'you have %s %s.' % (str(self.Player_money),self.m_type))
