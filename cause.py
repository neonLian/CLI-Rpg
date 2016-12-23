import random

Clist =  ['fighting for your people of the moon.','You hate bad hair.','You are salty about john and irene have beter codeing skills then you.','you think pot holes are pepole to and fight for their lives.','You are crazy about good grammer.','you must find the cheez planet.','You woke up on the wrong side of the bed...7 years ago.','You think the world is your lawn and dont want people on it.','You must pet all the dogs in the world.','you have to have all the stuff!' ]
Money = ['cheez','clumps of dirt','Sea shells','flaming bags of dog poo','rocks','trash','gold','pocket lint','parking tikets']
class Cause():
	def __init__ (self,cause,M):
		self.cause = cause
		self.Money = M
C = Cause(random.choice(Clist),random.choice(Money))
		
