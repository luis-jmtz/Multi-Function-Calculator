import math
import sympy
from sympy import symbols
from sympy.solvers import solve
from fractions import Fraction


# Write your code here
def add_subtrat_multiply_divide(equation):
  return eval(equation)

# print(add_subtrat_multiply_divide("2 * (3 + 5) - 1"))

# --------------------------------------------------------------------------------------------

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
# ----------------------------------------------------------------------------------------------

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

# -------------------------------------------------------------------------------------------

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
# -----------------------------------------------------------------------------------------

def solve_for_var(user_input):
  x = symbols('x')
  eq = user_input
  print("x = ", solve(eq,x)[0])

# ---------------------------------------------------------------------------------------
def convert_decimal(user_input):
  clean_input = float(user_input)
  frac = str(Fraction(clean_input))
  print(f"Fraction: {frac}")

  temp = 100*clean_input
  dec = f"Percentage: {temp}%"
  print(dec)

#--------------------------------------------------------------------------
def convert_percentage(user_input):
  clean_input = float(user_input)

  temp = clean_input/100
  dec = f"Decimal: {temp}"
  print(dec)

  frac = str(Fraction(temp))
  print(f"Fraction: {frac}")

convert_percentage(25)
# -------------------------------------------
def convert_fraction(user_input):
  clean_input = eval(user_input)
  print(f"Decimal: {clean_input}")

  temp = 100*clean_input
  dec = f"Percentage: {temp}%"
  print(dec)


#--------------- 