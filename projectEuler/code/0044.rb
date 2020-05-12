#!/usr/bin/env ruby

def pen(n)
   if n.nil?
      return nil
   else
      return (3*n*n - n)/2
   end
end

def isPenta(n)
   m = 24*n + 1
   if Math.sqrt(m) == Math.sqrt(m).to_i
      i = 0
      until pen(i+1) > n
         i += 1
      end
   else
      false
   end
   
   if pen(i) == n
      true
   else
      false
   end
end

min_diff = 10000000

(1..100000).each do |a|
   x = pen(a)
   ((a+1)..100000).each do |b|
      y = pen(b)
      sum = x + y
      diff = y - x
      # puts sum
      if isPenta(sum) && isPenta(diff)
         if diff < min_diff
            # puts x.to_s + ", " + y.to_s + ", " + sum.to_s + ", " + diff.to_s
            puts "new diff: " + diff.to_s
            sleep(3)
            min_diff = diff
         end
      end
   end
end

puts min_diff
