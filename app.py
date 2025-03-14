from functions import scores
nstudent = int(input("How many number of Students? "))
i = 0
while i < nstudent:
    name = input("Name? ")
    score = float(input('Score? '))
    scores(score)
    i = i + 1