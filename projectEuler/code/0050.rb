#!/usr/bin/env ruby

def isPrime(n)
   if n%2 == 0
      return false
   else
      (3..n-1).step(2).each do |d|
         if n%d == 0
            return false
         end
      end
      return true
   end
end

p_array = [2]

range = (3..10000).step(2)
range.each do |d|
   if isPrime(d)
      p_array << d
   end
end

# sum_record = 2
num_record = 2
l = p_array.length()

n_cons_test = (1..1000)
n_cons_test.each do |nc|
   (0..(l-1-nc)).each do |ncc|
      test_array = p_array[ncc, nc]
      sum = test_array.inject(0, :+)
      if sum > 1000000
         break
      end
      if nc > num_record && isPrime(sum)
         # sum_record = sum
         num_record = nc
         puts "Found sum: " + sum.to_s + " with " + nc.to_s + " primes"
      end
   end
end

