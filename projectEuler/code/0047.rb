#!/usr/bin/env ruby

def isPrime(n)
   if n == 2
      return true
   elsif n>2 && n%2 == 0
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

def pfSet(n)
   r = (3..n).step(2)
   r = r + [2]
   pfs = []       # prime factors set 
   while n>4
      r.each do |p|
         if isPrime(p) && n%p==0
            n = n/p
            unless pfs.include?(p)
               pfs << p
            end
         end
      end
   end
   return pfs.sort!
end

range = (1..10000)
range.each do |n1|
   puts "Test: " + n1.to_s
   n2 = n1+1
   n3 = n1+2
   n4 = n1+3
   p1 = pfSet(n1)
   p2 = pfSet(n2)
   p3 = pfSet(n3)
   p4 = pfSet(n4)
   unless p1.length() == 4
      next
   end
   unless p2.length() == 4
      next
   end
   unless p3.length() == 4
      next
   end
   unless p4.length() == 4
      next
   end
   puts "Found:\n" + n1.to_s + " " + n2.to_s + " " + n3.to_s + " " + n4.to_s
   break
end


