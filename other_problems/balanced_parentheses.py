def balanced_parentheses(input_string):
  # https://www.youtube.com/watch?v=QZOLb0xHB_Q&index=10&list=PL2_aWCzGMAwLPEZrZIcNEq9ukGWPfLT4A
  # Check that parenthesis are balanced. For every opening brace, there must be exactly one closing brace
  bracket_stack = []

  for c in input_string:
    if c == '{':      
      bracket_stack.append(c)
    
    elif c == '(':
      bracket_stack.append(c)
    
    elif c == '[':
      bracket_stack.append(c)

    elif c == '}':
      if len(bracket_stack) == 0 or bracket_stack[-1:][0] != '{': return False
      bracket_stack.pop()

    elif c == ')':
      if len(bracket_stack) == 0 or bracket_stack[-1:][0] != '(': return False
      bracket_stack.pop()

    elif c == ']':
      
      if len(bracket_stack) == 0 or bracket_stack[-1:][0] != '[': return False
      bracket_stack.pop()


  if len(bracket_stack) == 0:
    return True
  else:
    return False



if __name__ == "__main__":

  expressions = ['[{', '[]', '[( ])', '[[(a + b) + c)] + d]', '[[(a + b) + c] + d]', ')(', '()', '[()()]']

  for expression in expressions:
    print "%s -> %s" %(expression, balanced_parentheses(expression))