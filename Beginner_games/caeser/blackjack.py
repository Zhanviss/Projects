cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import random
from bjlogo import logo
play=True
number=len(cards)-1
def sum(card1,card2):
	return card1+card2
while play:
	agreement=input("Do you want to play a game of Blackjack? Type 'y' or 'n' :")
	if agreement=='n':
		play=False
	elif agreement=='y':
		print(logo)
		
		firstcard=cards[random.randint(0,number)]
		secondcard=cards[random.randint(0,number)]
		thirdcard=cards[random.randint(0,number)]
		print(f"Your cards are {firstcard}, {secondcard}")
		computer_cards1=cards[random.randint(0,number)]
		print(f"Computer's first card is {computer_cards1}")
		computer_cards2=cards[random.randint(0,number)]
		anothercard=input("Type 'y' to get another card, type 'n' to pass: ")
		if anothercard=='n':
			print(f"Your final hand is {firstcard}, {secondcard}")
			print(f"Computer's final hand is {computer_cards1}, {computer_cards2}")
			if sum(firstcard,secondcard)>sum(computer_cards1,computer_cards2):
				if sum(firstcard,secondcard)==21:
					print("BLACKJACK!!!You win!")
				elif sum(firstcard,secondcard)<21:
					print("You win")
				else:
					print("You lose")
					play=False
			elif sum(firstcard,secondcard)==sum(computer_cards1,computer_cards2):
				print("DRAW")
				play=False
			else:
				print("You lose")
				play=False
		elif anothercard=='y':
			print(f"Your final hand is {firstcard}, {secondcard}, {thirdcard}")
			print(f"Computer's final hand is {computer_cards1}, {computer_cards2}")
			if sum(firstcard,secondcard)+thirdcard>sum(computer_cards1,computer_cards2):
				if sum(firstcard,secondcard)+thirdcard<21:
					print("You win")
				else:
					print("You lose")
					play=False
			else:
				print("You lose")
				play=False