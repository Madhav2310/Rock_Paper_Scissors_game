import random
print("**********Rock**********")
print("**********Paper*********")
print("********Scissors********\n\n")
mode = input("How would you like to play? Player vs Player or Computer vs Player? (p/c) : ").lower()

if mode=="c":
	print("\nYou represent all of humanity, It's you against the wretched Computers!!")
	ys=0
	cs=0
	while True:
		print(f"Your score: {ys}  Computer's score: {cs}")
		pm = input("Your move: ").lower()
		cm = random.randint(1,3)
		if cm == 1:
			cm="rock"
		elif cm==2:
			cm="paper"
		else:
			cm="scissors"
		print(f"Computer's move: {cm}")

		if cm==pm:
			print("Its a Tie..")
		elif pm =="rock":
			if cm == "paper":
				print("Computer wins...")
				cs+=1
			else:
				print("You win!")
				ys+=1
		elif pm =="paper":
			if cm == "rock":
				print("You win!")
				ys+=1
			else: 
				print("Computer wins...")
				cs+=1
		elif pm == "scissors":
			if cm == "paper":
				print("You win!")
				ys+=1
			else:
				print("Computer wins...")
				cs+=1
		else:
			print("Enter valid move >:(")
		conti = input("Want to continue playing? (y/n) : ").lower()
		if conti== "n":
			break
	print(f"Your score: {ys}  Computer's score: {cs}")
	if cs>ys:
		print("\nThe computers win :(\n")
	elif ys>cs:
		print("\nIts humanity's hero's win!\n")
	else:
		print("\nIt was a tie..\n")
else:

	print("\nPlayer vs Player it is!")
	print("SHOOT!!!")
	p1s=0
	p2s=0
	conti="y"
	while conti=="y":
		print(f"Player 1's score: {p1s}  Player 2's score: {p2s}")
		p1 = input("Player 1's move: ").lower()
		print("     NO CHEATING     \n" * 100)
		p2 = input("Player 2's move: ").lower()
		if p1==p2:
			print("Its a TIE!")
		elif p1 =="rock":
			if p2 == "paper":
				print("Player 2 WINS!")
				p2s+=1
			elif p2 == "scissors":
				print("Player 1 WINS!")
				p1s+=1
		elif p1 =="paper":
			if p2 == "rock":
				print("Player 1 WINS!")
				p1s+=1
			elif p2 == "scissors":
				print("Player 2 WINS!")
				p2s+=1
		elif p2 =="scissors":
			if p2 == "paper":
				print("Player 1 WINS!")
				p1s+=1
			elif p2 == "rock":
				print("Player 2 WINS!")
				p2s+=1
		else:
			print("Invalid moves detected !!")
		conti = input("Want to play more? (y/n)").lower()
	print(f"\nPlayer 1's score: {p1s}  Player 2's score: {p2s}\n")
	if p1s>p2s:
		print("Its Player 1's win!")
	elif p2s>p1s:
		print("Its Player 2's win!")
	else:
		print("It was a tie..")

