from calclogo import logo
import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def addition(n1,n2):
	return n1+n2
def subtraction(n1,n2):
	return n1-n2
def multiplication(n1,n2):
	return n1*n2
def division(n1,n2):
	return n1/n2

operations={
	"+":addition,
	"-":subtraction,
	"*":multiplication,
	"/":division
}

def calculator():
	print(logo)
	go_on=True

	firstnum=float(input("What's your first number? "))
	for symbol in operations:
		print(symbol)
	while go_on:
		op_symbol=input("Pick your operation:")
		secondnum=float(input("What's your second number? "))

		typeofcalc=operations[op_symbol]
		answer=typeofcalc(firstnum,secondnum)

		print(f"{firstnum} {op_symbol} {secondnum} is equal to {answer}")
		continuation=input(f"Type 'yes' if you want to continue calculations with {answer}, or type 'no' to start again. ")
		if continuation=='no':
			go_on=False
			clearConsole()
		elif continuation=='yes':
			firstnum=answer
calculator()