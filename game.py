from player import *
from battle import *
from weapon import *
bob = Player("Bob")
billy = Player("Billy")
crsn = Player("C.rs.n")
players = [bob, billy, crsn]
weapons = [Sword, Fireball, Heal, RegenMana]
for p in players:
	for w in weapons:
		p.add_weapon(w(p))
for l in range(100):
	bob.level_up()
Battle(players)
