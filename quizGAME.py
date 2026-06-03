#Quiz Game
questions =[
    ["2 + 2","4"],
    ["Capital of India","Delhi"],
    ["1 4 6 8 ?","10"]
    ]
score = 0
for question in questions:
    answer = input(question[0] + ": ")
    if answer== question[1]:
        print("Correct")
        score = score + 1
    else:
        print("Wrong")
print("Your score is : ", str(score))
