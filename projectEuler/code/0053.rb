#!/usr/bin/env ruby

# use combinatorial notation with a < b
def com(a, b)
   numerator = 1
   denominator = 1
   ((b-a+1)..b).each do |i|
      numerator *= i
   end
   (1..a).each do |i|
      denominator *= i
   end
   return (numerator/denominator)
end

count = 0

(1..100).each do |n|
   (1..n).each do |r|
      c = com(r, n)
      if c > 1000000
         count += 1
      end
   end
end


puts count
