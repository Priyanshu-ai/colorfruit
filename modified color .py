print("Hello!! Here i am your chatbot with a calculative brain !!")
print("I'll tell u that which fruit you are thinking abount only by knowing it's color")
while True:
	def color_fruit(colour):
		trans = ""
		for letter in colour:
			if letter[0] in "r":
				if letter[2] in "d":
					if letter[1] in "e":
						trans = "red"
					else:
						trans = "red"
						print("oops!! you want to type it red")
			elif letter[0] in "y":
				if letter[5] in "w":
					if letter[1,2,3,4] in "ello":
						trans = "yellow"
					else:
						trans = "yellow"
						print("i think you want to type it yellow")
		if trans == "red":
			print("BTW your fruit name is Apple")
		elif trans == "yellow":
			print("fruit name Banana")
		else:
			print("fruit not found")
	print(color_fruit(input("Enter color of fruit::  ")))