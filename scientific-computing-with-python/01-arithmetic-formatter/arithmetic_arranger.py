import re


def get_components(problem):
  operands = re.findall("[\w]+", problem)
        # get all words including non-numeric
  operator = re.findall("[^\w\s]", problem)[0]
  return (operands, operator)

def arithmetic_arranger(problems, solution=False):

  first_line = ""
  operator_line = ""
  second_line = ""
  dash_line = ""
  answer_line = ""

  if len(problems) > 5:
    return "Error: Too many problems."
    
  for i, problem in enumerate(problems):
    operands = get_components(problem)[0]
    operator = get_components(problem)[1]


    if max(map(len, operands)) > 4:
        return "Error: Numbers cannot be more than four digits." 
    
    try: 
        a, b = map(int, operands)
    except ValueError:
        return "Error: Numbers must only contain digits." 

    if operator == "+":
        answer = a + b
    elif operator == "-":
        answer = a - b
    else:
        return "Error: Operator must be '+' or '-'."


    width = max(map(len,map(str,[a,b]))) + 2 
            # add 2 to max width because of "+ " or "- " in the second_line
    
    first_line  += f"{a}".rjust(width)
    second_line += f"{operator}" + f"{b}".rjust(width-1)
    dash_line += "-"*width
    answer_line += f"{answer}".rjust(width)

    if i < len(problems)-1:
        col_width = " "*4
        first_line += col_width
        second_line += col_width
        dash_line += col_width
        answer_line += col_width

  lines = [first_line,
    second_line,
    dash_line,
    answer_line
    ]

  if solution:
    arranged_problems = "\n".join(lines)
    return arranged_problems
  else:
    arranged_problems = "\n".join(lines[:-1])
    return arranged_problems

  return arranged_problems

