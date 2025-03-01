def isPrime(n):
    if n <= 1:
        return False

    # Check divisibility from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False

    return True

if __name__ == "__main__":
  n = 11
  if(isPrime(n)): 
    print("true")
  else:
    print("false")
