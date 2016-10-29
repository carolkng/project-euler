def pyth(a,b,c) 
    a2 = a*a
    b2 = b*b
    c2 = c*c

    puts "a2: #{a2}"
    puts "b2: #{b2}"
    puts "c2: #{b2}"

    return a2 + b2 == c2
end

a = 1
b = 2
c = 1000 - a - b

while !pyth(a,b,c)
  if (b+1) > c
    a += 1
    b = a + 1
    c = 1000 - a - b
  else
    b += 1
    c -= 1
  end
end

puts "a: #{a}"
puts "b: #{b}"
puts "c: #{c}"
puts "abc: #{a*b*c}"
