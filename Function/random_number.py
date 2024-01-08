import random
import string

def getAnswer(answerNumber):
  if answerNumber == 1:
    return "You are beautiful."
  elif answerNumber == 2:
    return "You are cute."
  elif answerNumber == 3:
    return "You are a Banana."
  elif answerNumber == 4:
    return "You are Monkey."
  elif answerNumber == 5:
    return "You are Sexy."
 # this code generates random numbers 
number= random.randint(1,5)
print(number)
input("Let's see what your fortune says... Press ENTER to continue...")

fortune = getAnswer(number)
print(fortune)


#this code genrate random characters
character=random.choice(string.ascii_letters + string.digits)
print(character)