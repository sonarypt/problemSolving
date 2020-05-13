#!/usr/bin/env ruby

# only need to test from hexagonal back to pentagonal

range = (2..100000)

def hexa(n)
   return n*(2*n - 1)
end

def isInteger(k)
   if k == k.to_i
      return true
   else
      return false
   end
end

range.each do |n|
   nn = hexa(n)
   m = Math.sqrt(24*nn+1)
   if isInteger(m) 
      if (m-5)%6==0
         puts "Found hexagonal number " + n.to_s + "th: " + nn.to_s
      else
         next
      end
   else
      next
   end
end
