from guesslogo import logo
print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ")
import random
finished=False
guessed_number=random.randint(0,100)
print(f"pss, guessed number is {guessed_number}")
def attempts(difficulty):
	if difficulty=='easy':
		attempts=10
	elif difficulty=='hard':
		attempts=5
	return attempts
attempts_remaining=attempts(difficulty)

while not finished:
	print(f"You have {attempts_remaining} attempts remaining to guess the number")
	guess=int(input("Make a guess: "))
	if guess!=guessed_number:
		if guess<guessed_number:
			print("Too low. Guess again")
			attempts_remaining-=1
			if attempts_remaining==0:
				print("You are out of attempts. You lose")
				finished=True
		elif guess>guessed_number:
			print("Too high. Guess again.")
			attempts_remaining-=1
			if attempts_remaining==0:
				print("You are out of attempts. You lose")
				finished=True
		
	elif guess==guessed_number:
		print("You guessed a number!")
		finished=True



