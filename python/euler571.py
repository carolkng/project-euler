# find the 10 smallest pan digital numbers

num = 1093265784
n = 1
sum_pan10 = 0

# Assumes input of num_b(base)
def isSuperPandigital(num, base):
  while (base > 1):
    str_num = str(num)

    for n in range(0,base):
      if str(n) not in str_num:
        return False

    # num(b) > str(b), str(b) > num10, num10 > str10, str10 > num(b-1)
    num = int(str(num), base)
    base -= 1

  return True

def baseToN (num, N):
  largestPower = 1

  while (N ** largestPower < num):
    largestPower += 1

  currPower = largestPower-1

  while (currPower >= 0):
    num -= num % currNumPower
    currNumPower = n ** currPower
    digit = (num - (num - num % currNumPower)) / currNumPower

    if (digit > 9):
      print "baseToN encountered an error:"
      print "num: %d  base: %d  output: %d" % (num, N, digit)
      return

    digits.append(digit)
    currPower -= 1

  return int(digits.reverse().join())



