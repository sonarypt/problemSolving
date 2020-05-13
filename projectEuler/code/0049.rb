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

def perm(n)
   d_list = n.to_s.split("")
   output_list = []
   d_list.permutation().to_a.each do |d|
      ds = d.join.to_i
      unless output_list.include?(ds)
         output_list << ds
      end
   end
   return output_list - [n]
end

def extent(n, m)
   return 2*m-n
end

range = (1001..9999).step(2)
range.each do |n|
   if isPrime(n)
      pn = perm(n)
      pn.each do |m|
         if isPrime(m)
            e = extent(n, m)
            if pn.include?(e) && isPrime(e)
               puts "Found: " + n.to_s + " " + m.to_s + " " + e.to_s
            end
         end
      end
   else
      next
   end
end
