include Math

def isPrime(a)
  a_max = Math.sqrt(a).round
  divide = 3
  while divide <= a_max
    if a % divide == 0
      return false
    end

    divide += 2
  end
  return true
end

max = 2000000
int = 5
sum = 5

while int < 2000000
  if isPrime(int)
    sum += int
  end
  int += 2
end

puts "sum: #{sum}"

