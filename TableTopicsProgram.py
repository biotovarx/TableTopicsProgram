
import sys
import random




def welcomeMessage():
    response = "N"
    print("This program with give a topic a table topics speech. A clock will start for 2:00 minutes. Keeps practicing!")
    while(response.upper() != "Y"):
        response = input("Are you ready? Y/N or (Q)uit: ")
        if response.upper() == "Q":
            exit


def readInParseFile():

    topicList = [None] * 365
    with open('TM-365-sample-table-topics-questions.txt', 'r') as fp:
        lines = (line.rstrip() for line in fp) # All lines including the blank ones
        lines = (line for line in lines if line) # Non-blank lines

        for line in lines:
            (number, topic) = line.strip().split(". ")
            topicList[int(number)-1] = topic

    return topicList

def chooseQuestionNumber(topicList):
    qNumber = input("Which topic do you want? Pick number 1-365: ")
    print("\n\n\n\n\n%s\n\n\n\n\n" % topicList[int(qNumber)-1])




welcomeMessage()
topicList = readInParseFile()
chooseQuestionNumber(topicList)





