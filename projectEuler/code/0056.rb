#!/usr/bin/env ruby

def sumDigit(n)
   nr = n.to_s.split("").map{|x| x.to_i}
   return nr.inject(0, :+)
end

record = 0

(1..100).each do |a|
   (1..100).each do |b|
      s = sumDigit(a**b)
      if s > record
         record = s
         puts "Found: " + a.to_s + "^" + b.to_s + " with sum of digits " + s.to_s
      end
   end
end

