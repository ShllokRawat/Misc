def factorial(n):
     if n == 1:
        return 1
     return n * factorial(n - 1)

def fibonacci(n):
    if n == 0:
      return 0
    elif n == 1:
      return 1
    else:
      return fibonacci(n - 1) + fibonacci(n - 2)

def isPalindrome(word):
      if len(word) <+ 1:
        return True
      if word[0] == word[-1]:
        return isPalindrome(word[1:-1])
      else:
        return False