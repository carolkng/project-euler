def fact(num):
  if num < 1:
    return 1
  return reduce(lambda x,y: x*y, range(1,num+1))
 
def choose(num, ber):
  if num > ber:
    return fact(num) / fact(ber) / fact(num-ber)
  elif num == ber:
    return 1
  else:
    return "ERROR: NchooseN(x,y) must have x > y (x choose y)"

def combinations(num):
  return reduce(lambda x,y: x+y, map(lambda x: choose(num, x), xrange(1,num+1)), 0)
  
def isPrime(num):
  if num == 2:
    return True
  
  div = 2
  
  isPrime = True
  while div <= num ** 0.5:
    if (num % div) == 0:
      isPrime = False
      break
    div += 1

  return isPrime

# Returns the next prime number bigger than num
def nextPrime(num):
  num += 1
  if num == 2:
    return 3  
  while not isPrime(num):
    num += 1
 
  return num

def factors_help(num, factor):
  count = 0
  while (num % factor) == 0:
    count += 1
    num = num / factor
   
  return count

def factors(num):
  factor = 2
  factorlist = []
  count_factor = 0
 
  while not isPrime(num):
    count_factor = factors_help(num, factor)
    for i in xrange(0,count_factor):
      factorlist.append(factor)
    num = num / (factor**count_factor)
    factor = nextPrime(factor)
  
  if num != 1:
    factorlist.append(num)
   
  return factorlist


i = 10
num = 1
while combinations(len(factors(num))) < 1000:
  num = i*(i+1)/2
  i += 1

print num
# print factors(num)