import os
from datetime import date
import time
from animation import animationList

def main():
	try:
		day, month, year = getInput()
		formatAnimations()

		i = 0
		while True:
			os.system("cls")
			printTitle(year)
			printFrame(i)
			time.sleep(1)
			i += 1
			i %= len(animationList)
	except Exception as e:
		print(e)

def printFrame(i):
	animationList
	frame = "\n".join(animationList[i])
	print(frame)

def formatAnimations():
	for f in animationList:
		for i, line in enumerate(f):
			f[i] = "\u001B[32m" + line + "\u001B[0m"

def getInput():
	currentDate = date.today()
	print(f"Today is {currentDate}")
	print("Enter the date")

	d = int(input("Enter the Day: "))
	m = int(input("Enter the Month: "))
	y = input("Enter the Year (Optional): ")

	if y == "":
		
		y = currentDate.year
	else:
		y = int(y)
	
	if d != 23 or m != 9:
		raise Exception("Current Date is not Saudi Day")

	return d, m, y

def printTitle(year):
	numberOfDays = 90 + (-2020 + year)
	print(f"{numberOfDays}" + r" اليوم الوطني السعودي")

if __name__ == "__main__":
	main()