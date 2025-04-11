def greet_programmer():
  """Greets the programmer with a simple message."""
  print("Hello, programmer!")

def greet(name):
  """Greets the given name."""
  print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
  """Greets the given name, or 'programmer' if no name is provided."""
  print(f"Hello, {name}!")

def add(num1, num2):
  """Returns the sum of two numbers."""
  return num1 + num2

def halve(number):
  """Returns half the value of the given number."""
  return number / 2

# Let's test them out!
greet_programmer()
greet("Alice")
greet_with_default()
greet_with_default("Bob")
sum_result = add(5, 3)
print(f"The sum is: {sum_result}")
half_result = halve(10)
print(f"Half of 10 is: {half_result}")