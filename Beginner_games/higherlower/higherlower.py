from arthigherlower import logo
print(logo)
import random
from game_data import data
lose=False

def rndm(info):
	return random.choice(info)

def format_info(info):
	name = info["name"]
	description = info["description"]
	country = info["country"]
	return(f"{name} , {description} from {country}")

def comparison(info1, info2):
	follower1=info1["follower_count"]
	follower2=info2["follower_count"]
	if follower1>follower2:
		print(f"{format_info(newrandom1)} has more followers {follower1} than {format_info(newrandom2)} with {follower2}")
	else:
		print(f"{format_info(newrandom2)} has more followers {follower2} than {format_info(newrandom1)} with {follower1}")

newrandom1=rndm(data)
newrandom2=rndm(data)
comparison(newrandom1,newrandom2)