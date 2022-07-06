import random

l = ["s", "w", "g"]
you_play = 0
computer_point = 0
human_point = 0

print("Welcome Snake Water Gun Game")

a = int(input("Enter How much time you want to play!: "))
r = random.choice(l)
print(r)

while a > you_play:
    print("Snake (S), Water (W), Gun(G):-\n")
    i = str(input("Enter Your Choice:\n"))
    i = i.lower()

    if i == r:
        print("Tie Both Valure same")

    elif i == "s" and r == "w":
        print("Human Win")
        human_point += 1
        print(f"your point is {human_point} and computer point is {computer_point}\n ")

    elif i == "w" and r == "s":
        print("Computer Win")
        computer_point += 1
        print(f"your point is {human_point} and computer point is {computer_point} \n")

    elif i == "s" and r == "g":
        print("Computer Win")
        computer_point += 1
        print(f"your point is {human_point} and computer point is {computer_point} \n")

    elif i == "g" and r == "s":
        print("Human Win")
        human_point += 1
        print(f"Your point is {human_point} and Computer point is {computer_point}\n")

    elif i == "w" and r == "g":
        print("Human Win")
        human_point +=1
        print(f"Your points is {human_point} and Computer point is {computer_point}\n")
    elif i == "g" and "w":
        print("Human Win")
        print(f"Your points is {human_point} and Computer point is {computer_point}\n")
    else:
        print("Write Vlue")
    you_play +=1