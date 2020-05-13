#!/usr/bin/env ruby

def isPrime(n)
   cases = [2,3,5,7]
   if n%2 == 0 && n > 2
      return false
   end
   if n < 9
      if cases.includes?(n)
         return true
      else
         return false
      end
   elsif n > 9
      (3..(Math.sqrt(n).to_i)).step(2).each do |d|
         if n%d == 0
            return false
         end
      end
      return true
   end
end

def isSerial(n)
   output = 1
   subrange = (1..Math.sqrt(n).to_i)
   subrange.each do |d|
      if n % d == 0
         unless isPrime(d + n/d)
            output = output - 1
            break
         end
      end
   end
   if output == 1
      return true
   else
      return false
   end
end

sum_count = 0_u64

range = (1..100_000_000)
range.each do |n|
   if isSerial(n)
      puts "Got: " + n.to_s
      sum_count += n
   end
end
puts "Total sum: " + sum_count.to_s


