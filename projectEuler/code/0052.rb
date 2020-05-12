#!/usr/bin/env ruby

range = 1..10000000

range.each do |n|
   a1 = n.to_s.split("").sort!
   a2 = (2*n).to_s.split("").sort!
   unless a1 == a2
      next
   end
   a3 = (3*n).to_s.split("").sort!
   unless a2 == a3
      next
   end
   a4 = (4*n).to_s.split("").sort!
   unless a3 == a4
      next
   end
   a5 = (5*n).to_s.split("").to_a.sort!
   a6 = (6*n).to_s.split("").to_a.sort!
   if a1 == a2 && a2 == a3 && a3 == a4 && a4 == a5 && a5 == a6
      puts "Found: " + n.to_s
   end
end
