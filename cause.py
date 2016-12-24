import random

Clist =  ['fighting for your people of the moon.','You hate bad hair and must get rid of all the people with it.','You are salty about john and irene have beter coding skills then you.you will kill all who dont help you in that cause.','you think pot holes are pepole to and fight for their lives.','You are crazy about good grammer.people that dont use it well must die.','you must find the cheez planet,no one will stand in your way.','You woke up on the wrong side of the bed...7 years ago.','You think the world is your lawn and dont want people on it.what you do to get them off is not plesent.','You must pet all the dogs in the world.thats it, your on a quest to do that. ','you have to have all the stuff!']
Money = ['cheez','clumps of dirt','Sea shells','flaming bags of dog poo','rocks','trash','gold','pocket lint','parking tickets','ideas and advise','bacon','shrugs']
class Cause():
	def __init__ (self,cause,M):
		self.cause = cause
		self.Money = M
C = Cause(random.choice(Clist),random.choice(Money))
		
