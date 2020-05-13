def isPrime(n)    # must use optimized prime check function
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


def isLT(n)
   an = n.to_s.split("")
   sn = an.size
   (1..(sn-1)).each do |i|   # exclude number n itself
      unless isPrime(an[i..].join.to_i)
         return false
      end
   end
   return true
end

def isRT(n)
   an = n.to_s.split("")
   sn = an.size
   (0..(sn-2)).each do |i|
      unless isPrime(an[..i].join.to_i)
         return false
      end
   end
   return true
end

count = 1
number_test = 11
sum = 0
while count < 12
   if isPrime(number_test) && isLT(number_test) && isRT(number_test)
      puts "Found: " + number_test.to_s + " - " + count.to_s + " th number"
      count += 1
      sum += number_test
   end
   number_test += 2
end

puts "Total sum: " + sum.to_s
