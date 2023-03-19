import random
result = 0
attempt = 0

gameType = input("Normal 'Heads or Tails' (1) or how many times does the program raffle the same result(2)?")
if gameType == "1":
    if random.randrange(0, 2) == 1:
        print("Head")
    else:
        print("Tail")
elif gameType == "2":
    sameResult = input("How many times do you want to get the same result?")
    firstResult = random.randrange(0, 2)
    while int(sameResult) > result:
        attempt += 1
        secondResult = random.randrange(0, 2)

        if firstResult == secondResult:
            result += 1
        else:
            result = 0
            firstResult = secondResult
    print("It took " + str(attempt) + " attempts")
