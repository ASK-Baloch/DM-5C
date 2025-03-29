# Data-Mining by sir Tajmir
All the Assignments of Datamining By sir Tajmir

## 1. Variable Swap
```python
def swap_variables(a, b):
  """Swaps the values of two variables without using a third variable.
  """
  print(f"Initial values: a = {a}, b = {b}")  # Print initial values

  a = a + b  # Add b to a
  b = a - b  # Subtract b from a (original a is now a+b, so this gives original a)
  a = a - b  # Subtract new b (original a) from a (a+b) to get original b

  print(f"Swapped values: a = {a}, b = {b}")  # Print swapped values
  return a, b


# Example usage:
x = 10
y = 5
x, y = swap_variables(x, y)  # Call the function and unpack the returned tuple