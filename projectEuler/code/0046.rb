#!/usr/bin/env ruby

def isPrime(n)
   if n%2 == 0
      return false
   else
      (3..(n-1)).step(2).each do |d|
         if n%d == 0
            return false
         end
      end
      return true
   end
end

def isPerfect(n)
   root = Math.sqrt(n)
   if root == root.to_i
      return true
   else
      return false
   end
end

def checkGoldback(n)
   subrange = (3..n).step(2)
   stat = 0
   subrange.each do |sd|
      if isPrime(sd)
         val = (n - sd)/2
         if isPerfect(val)
            stat += 1
            break
         else
            next
         end
      else
         next
      end
   end
   case stat
   when 0
      return false
   when 1
      return true
   end
end

range = (3..100000).step(2)
range.each do |n|
   if isPrime(n)
      next
   else
      unless checkGoldback(n)
         puts "Got number: " + n.to_s
      end
   end
end
