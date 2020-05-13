#!/usr/bin/env ruby

def revInt(n)
   return n.to_s.split("").reverse.join.to_i
end

def isPalin(n)
   nr = revInt(n)
   if nr == n
      return true
   else
      return false
   end
end

def palinRoute(n)
   count = 0
   n = n + revInt(n)
   if isPalin(n)
      count = 1
   end
   until isPalin(n)
      n = n + revInt(n)
      if count < 51
         count += 1
      else
         count = 0
         break
      end
   end
   return count
end

range = (10..9999)
lychrel_count = 0
range.each do |n|
   pr = palinRoute(n)
   if pr == 0
      puts n.to_s + " with " + pr.to_s + " steps."
      lychrel_count += 1
   end
end

# puts palinRoute(47)

puts lychrel_count
