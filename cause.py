import random

Clist =  ['fighting for your people of the moon.','You hate bad hair and must get rid of all the people with it.','You are salty about john and irene have beter coding skills then you.you will kill all who dont help you in that cause.','you think pot holes are pepole to and fight for their lives.','You are crazy about good grammer.people that dont use it well must die.','you must find the cheez planet,no one will stand in your way.','You woke up on the wrong side of the bed...7 years ago.','You think the world is your lawn and dont want people on it.what you do to get them off is not plesent.','You must pet all the dogs in the world.thats it, your on a quest to do that. ','you have to have all the stuff!','you dont realy know what your doing...just go with the flow i guess.','you are mad in more ways then one,now go out there and KILL!!! you sily goose.']
Money = ['cheez','clumps of dirt','Sea shells','flaming bags of dog poo','rocks','trash','gold','pocket lint','parking tickets','ideas and advise','bacon','shrugs','unicorn fats','leprocon hats','counterfit bills','the souls of the damned','funny quotes','ships in a bottle','"rare"air','pounds of fat','strands of hair','gossip',]
class Cause():
	def __init__ (self,cause,M):
		self.cause = cause
		self.Money = M
C = Cause(random.choice(Clist),random.choice(Money))
		
Test = C.cause
Money_type = C.Money
