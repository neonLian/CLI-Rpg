from player import *
from battle import *
from weapon import *
bob = Player("Bob")
billy = Player("Billy")
crsn = Player("C.rs.n")
players = [bob, billy, crsn]
for p in players:
	p.add_weapon(Sword(p))
	p.add_weapon(Fireball(p))
Battle(players)
