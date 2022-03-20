import random

def getQuestions(sub):
    path = "data/Questions/" + sub + ".txt"
    data = open(path, "r")
    val = data.read()
    val = val.split("\n")
    qnum = random.randint(0,10)
    print(val[qnum])
getQuestions("CSS")
getQuestions("CSS")
getQuestions("CSS")