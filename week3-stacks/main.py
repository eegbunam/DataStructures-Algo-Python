


"""
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Examples:

Input: s = "1 + 1"
Output: 2

Input: s = " 2-1 + 2 "
Output: 3

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23



Understand:

"1 + 1" = 2 

2-1+2 = 1 + 2 = 3

(1+(4+5+2)-3)+(6+8) = (1+11-3) + 14 = (12-3) + 14 = 9 + 14 = 23



Match:
- Stack


Plan:

- change 1+1(Infix) to 1 1 +(Postfix)
stack  = [+]
finalresult = "1 1 +"

2-1+2
stack = [+]
finalresult = "2 1 - 2 +"

example 3
(1+(4+5+2)-3)+(6+8)

stack = [+(+]
final_string = ((1 ((4 5+) 2 +) +)3-) (6 8 +) +




- evaluatePostfix()
postfix_expression = "1 1 +"

postfix_expression = "2 1 - 2 +"

stack = [3]

return stack [-1]
example 3

postfix_exp = ((1 ((4 5+) 2 +) +)3-) (6 8 +) +

stack = [23]

return stack[-1]

"""





def infix_to_postfix(exp):

  """
  this function takes an infix expression and evalutes that to a postfix expression
  Resources here: https://www.youtube.com/watch?v=jos1Flt21is
  Example:
    (1+(4+5+2)-3)+(6+8) = 1 4 5+ 2 + +3 - 6 8 +  +
  Explanation:
    The trick here is to go through the orginal string remove the parathesis and add the operators accordinly. More details below

    Loop through the string , lets call each value in the string a token
      - if your token is a opening parethesis then add to the stack
      - if your token is a number appened that number to your finalstring
      - if your token is a operator things get a little complicated
          - if your token is an operator  and the top of the stack has an operator on there then pop the top of the stack and append that into your string
          - else add the operator to the stack
      - if your token is a closing parathesis
        - keep poping everthing on the stack and adding that into your finalstring until you  find a opening parathesis to match your closing at the top of the stack then pop that off too
      - then pop the last things of the stack into your final string

  """
  finalString = ""
  stack = []
  exp = exp.strip()
  for numtoken in range(len(exp)):
    token = exp[numtoken]
    if isOperator(token):
      while stack and isOperator(stack[-1]):
        finalString += stack[-1]
        stack.pop()
      stack.append(token)
    elif isOpeningPaenthesis(token):
      stack.append(token)
    elif isClosingPaenthesis(token):
      # pop off the stack and add to string until we see an openeing parathesis
      while stack and (isOpeningPaenthesis(stack[-1]) == False):
        finalString += stack[-1]
        stack.pop()
      stack.pop() # removes opening parathesis
    else:
      # the element is an operand eg 1 and 2 
      finalString += token
  
  while stack: # add everything in stack to string if there is more things in the stack
    finalString += stack[-1]
    stack.pop()
  return finalString

  
    

def evaluate_postfix(postfix):

  """
  This function takes in a postfix expression and evealutaes that to a number

  How this works:

  1) The genral rule of post fix is that there is <operand><operand><operator>. An operand is always going to be a number iin this implementation because whenever we see an opeartor we will evaluate our current operands with that operator. More detils below

  Loop through the expression, lets call each character a token

  if a token is a operand we chnage it to an integer and add it to the stack

  (the somewhat complicate dpart) if a token is an operator then we are guaranteed that we will have two or more operands in the stack to we popo the most recent two operands and pefrom an operation on them using the operator. After calculating that number we push it back into the stack

  once we reach the end of the string we will only have one thing in the stack and we return that
  
  """
  stack = []
  for numtoken in range(len(postfix)):
    token = postfix[numtoken]
    if isOperator(token) == False:
      token = int(token)
      stack.append(token)
    elif stack and isOperator(token):
      val2 = stack.pop()
      val1 = stack.pop()
      value = calculate(val1 , val2 , token)
      stack.append(value)
  return stack[-1]



# Helper methods

def calculate(val1 , val2 , operator):
  if operator == "-":
    return val1 - val2
  if operator == "+":
    return val1 + val2
def isOperator(token):
  if token == "-" or token == "+":
    return True
  return False

def isOpeningPaenthesis(token):
  if token == "(":
    return True
  return False

def isClosingPaenthesis(token):
  if token == ")":
    return True
  return False


"""
Main fucntion that evaluates expressions
"""
def evaluate_exp(exp):
  post_exp = infix_to_postfix(exp)
  return evaluate_postfix(post_exp)




#print(infix_to_postfix("1+1"))
print(evaluate_exp("(1+(4+5+2)-3)+(6+8)"))
