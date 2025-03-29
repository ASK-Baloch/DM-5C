def swap_variables(a, b):
  """Swaps the values of two variables without using a third variable.
  """
  print(f"Initial values: a = {a}, b = {b}") 

  a = a + b  
  b = a - b  
  a = a - b  

  print(f"Swapped values: a = {a}, b = {b}")  
  return a, b
# Example usage:
x = 10
y = 5
x, y = swap_variables(x, y)  # Call the function and unpack the returned tuple
