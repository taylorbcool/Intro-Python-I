user_num = int(input("Enter number to test: \n"))

def is_prime(num):
  if num <= 1:
    return False
  else:
    for i in range(2, num):
      if num % i == 0:
        return False
    return True

def return_prime(num):
  if is_prime(num) == True:
    print("That number is prime.")
  elif is_prime(num) == False:
    print("That number is not prime.")
  else:
    print("I had trouble with that number, please try again.")

return_prime(user_num)