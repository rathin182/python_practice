s = 0
while (True):
    p = input("Enter Your number & q for quit")

    if (p != "q"):
        s = s + int(p)
        print(f"your value is {s}")
    elif (p == "q"):
        print("thanx for input")
        break