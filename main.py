#Try to run code.
#If error, return friendlier message
#this is to code defensively

"""
try:
  x = int(input("what's x? "))
  print(f"x is {x}")

except ValueError:
  print("x is not an integer.")

##

#this runs same as above but the above
#surely prints out everything in f fn
#hence, above won't raise ValueError
#but below will 
while True:
  try:
    x = int(input("What's x? "))
  except ValueError:
    print("X is not an integer.")
  else:
    break

print(f"X is {x}")


##
#pass is to catch the bug but not fierce


def main():
  x = get_int()
  print(f"X is {x}")

def get_int():
  while True:
    try:
      return int(input("What's X?"))
    except ValueError:
      pass

main()

"""

def main():
  x = get_int("what's x?")
  print(f"x is {x}")

#this helps if make below more reusable
#eg if change to y or z
def get_int(prompt):
  while True:
    try:
      return int(input(prompt))
    except ValueError:
      pass
  
main()