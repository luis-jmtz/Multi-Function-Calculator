import math
import sympy
from sympy import symbols
from sympy.solvers import solve
from fractions import Fraction


# ----------------- Caluculation Functions ---------- #

def add_subtrat_multiply_divide(equation):
  return eval(equation)

# ------------------------------------

def is_prime_number(user_input):
  factor_array = []
  for x in range (1, user_input+1):
      if user_input % x==0:
          #print(x)
          factor_array.append(x)

  #print(factor_array)
  if len(factor_array) > 2:
    return False
  return True

# print(is_prime_number(5))
# --------------------------

def gen_prime_factors(user_input):
  factor_array = []
  prime_array = []
  for x in range (1, user_input+1):
      if user_input % x==0:
          ##print(x)
          factor_array.append(x)

  for x in factor_array:
    if is_prime_number(x):
      prime_array.append(x)

  return prime_array

# ---------------------------

def simplify_square_root(n):
  upper_limit = math.floor(math.sqrt(n)) + 1
  max_factor = 1
  other_factor = 1
  square_root = 1

  for maybe_factor in range(1, upper_limit):
      if n % (maybe_factor**2) == 0:
          max_factor = maybe_factor**2

  other_factor = n/max_factor

  square_root = int(math.sqrt(max_factor))
  other_factor = int(other_factor)
  # output = f"{square_root}\u221A{other_factor}"
  output = square_root*sympy.sqrt(other_factor)

  return output

# print(simplify_square_root(20))
# ------------------------------

def solve_for_var(user_input):
  x = symbols('x')
  eq = user_input
  print("x = ", solve(eq,x)[0])

# ----------------------------
def convert_decimal(user_input):
  clean_input = float(user_input)
  frac = str(Fraction(clean_input))
  print(f"Fraction: {frac}")

  temp = 100*clean_input
  dec = f"Percentage: {temp}%"
  print(dec)

#------------------------
def convert_percentage(user_input):
  clean_input = float(user_input)

  temp = clean_input/100
  dec = f"Decimal: {temp}"
  print(dec)

  frac = str(Fraction(temp))
  print(f"Fraction: {frac}")

# --------------------

def convert_fraction(user_input):
  clean_input = eval(user_input)
  print(f"Decimal: {clean_input}")

  temp = 100*clean_input
  dec = f"Percentage: {temp}%"
  print(dec)


#--------------- Menu Functions -----------------#

def open_menu():
  operation_string = "Enter the number for the operation you would like to comlpete:\n"
  operation_string += "1. Add, subtract, multiply, divide\n"
  operation_string += "2. Detect Prime numbers\n"
  operation_string += "3. Generate prime factors of a number\n"
  operation_string += "4. Simplify square roots\n"
  operation_string += "5. Solve for x\n"
  operation_string += "6. Convert decimal to fractions and percents\n"
  operation_string += "7. Convert fraction to decimals and percents\n"
  operation_string += "8. Convert percent to decimals and fractions\n"

  op = int(input(operation_string))

  if op == 1:
    user_input = str(input("Please add the problem you would like me to calculate: "))
    print("Here is your solution: ",add_subtrat_multiply_divide(user_input))
    reopen_menu()
  elif op == 2:
    user_input = int(input("Enter a number to see if it Prime: "))
    if is_prime_number(user_input):
      print(f"{user_input} is Prime")
    else:
      print(f"{user_input} is Not a Prime Number")
    reopen_menu()
  elif op == 3:
    user_input = int(input("Enter a number to find its Prime Factors: "))
    print(gen_prime_factors(user_input))
    reopen_menu()
  elif op == 4:
    user_input = int(input("Enter a number that you want to find the Square Root of: "))
    temp = str(simplify_square_root(user_input))
    i = temp.find("*")
    outer = temp[:i]
    open = temp.find("(")
    close = temp.find(")")
    inner = temp[open+1:close]
    solution = f"{outer}\u221A{inner}"
    print("The Simplified Square Root is: ",solution)
    reopen_menu()
  elif op == 5:
    user_input = input('Enter an equation to solve for x: 0 = ')
    solve_for_var(user_input)
    reopen_menu()
  elif op == 6:
    user_input = input("Enter your Decimal: ")
    convert_decimal(user_input)
    reopen_menu()
  elif op == 7:
    user_input = input("Enter your Fraction: ")
    convert_fraction(user_input)
    reopen_menu()
  elif op == 8:
    user_input = input("Enter your Percentage (do not add '%'): ")
    convert_percentage(user_input)
    reopen_menu()
  else:
    print("Improper Input")
    open_menu()



def reopen_menu():
  y_n = input("Would you like to do another operation? y/n?")
  if y_n == "y":
    open_menu()
  else:
    print("Have a nice day")



