import math
import random
import copy
import turtle


_WINDOW_SIZE = [800,800]
_PEN_SIZE = 4
_DRAW_SPEED = 100

_AXIOM_LIMIT = 5
_RULE_LIMIT = 10
_CURRENT_ANGLE = 0
_LINE_LENGTH = 25

_AXIOM = ""
_RULES = {}
_ITERATION = -1
_ANGLE = -1
_STRING = ""

_ALPHABETS = ['A','B','C','D','E','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
_VARIABLES = ['F']
_CONTROL = ['F',']','+','-']
_ANGLES = [30,45,60,90, math.floor(random.random()*360), math.floor(random.random()*360)]
_ITERATIONS = [4,5,6,8,9]


def getRandomNo(limit):
  return math.floor(random.random()*limit)


def getMoreVariables(limit, variables = _VARIABLES):
  moreVarsCount = getRandomNo(limit -1) + 1  

  for _ in range(moreVarsCount):
    index = getRandomNo(len(_ALPHABETS))
    variables.append(_ALPHABETS[index]);

  return variables


def getStartString(limit, variables = _VARIABLES):
  length = getRandomNo(limit - 1) + 1
  startStr = ''

  for _ in range(length):
    startStr += variables[getRandomNo(len(variables))]

  return startStr

  
def getRulesStringMap(limit, variables = _VARIABLES, controlSet = _CONTROL):
  totalVars = copy.deepcopy(variables)
  totalVars.extend(controlSet)
  rules = {}
  for char in variables:
    length = getRandomNo(limit - 1) + 1
    ruleStr = ''

    for _ in range(length):
      appendChar =  totalVars[getRandomNo(len(totalVars))]
      if appendChar == ']':
        insertIndex = getRandomNo(len(ruleStr));
        ruleStr = ruleStr[0 : insertIndex] + "[" + ruleStr[insertIndex :];
      
      ruleStr += appendChar

    rules[char] = ruleStr

  return rules


def getNoOfIterations(iter = _ITERATIONS):
  return _ITERATIONS[getRandomNo(len(_ITERATIONS))]


def getAngle(angles = _ANGLES):
  return _ANGLES[getRandomNo(len(_ANGLES))]                                 


def getGrammer():
  global _AXIOM, _RULES, _ITERATION, _ANGLE
  getMoreVariables(_AXIOM_LIMIT, _VARIABLES)
  _AXIOM = getStartString(_AXIOM_LIMIT, _VARIABLES)
  _RULES = getRulesStringMap(_RULE_LIMIT, _VARIABLES, _CONTROL)
  _ITERATION = getNoOfIterations(_ITERATIONS)
  _ANGLE = getAngle(_ANGLES)


def generateStringFromGrammer():
  string = _AXIOM

  for _ in range(_ITERATION):
    newString = ''
    for char in split(string):
      ruleOutput = _RULES.get(char)
      if ruleOutput == None:
        newString += char
      else:
        newString += ruleOutput
    
    string = newString

  return string    
      

def split(word): 
    return [char for char in word]
   

def draw(axiom, currentAngle, length):

    stack  = []           
    screen = turtle.Screen()
    alex   = turtle.Turtle()

    screen.screensize(_WINDOW_SIZE[0], _WINDOW_SIZE[1])

    alex.hideturtle()
    alex.speed(_DRAW_SPEED)  
    alex.left(currentAngle)     

    for i in range(len(axiom)):
        c = axiom[i]

        if c == 'F':
            alex.pensize(_PEN_SIZE)
            alex.forward(length)

        if c == '+':
            currentAngle -= _ANGLE
            alex.left(currentAngle)

        if c == '-':
            currentAngle += _ANGLE
            alex.right(currentAngle)

        if c == '[':
            stack.append((alex.heading(), alex.pos()))

        if c == ']':
            heading, position = stack.pop()
            alex.penup()
            alex.goto(position)
            alex.setheading(heading)
            alex.pendown()

    screen.onkey(screen.bye, 'q')
    screen.listen()
    turtle.mainloop()


def main():
  global _STRING
  getGrammer()
  _STRING = generateStringFromGrammer()
  
  draw(_STRING, _CURRENT_ANGLE, _LINE_LENGTH)

if __name__ == "__main__":
  main()
