#!/usr/bin/env ruby

f = File.open("../p079_keylog.txt", "r")

number_list = []

f.each_line do |line|
   (0..9).each do |dd|
      if line.to_s.include? dd.to_s
         unless number_list.include? dd
            number_list << dd
         end
      end
   end
end

number_list.sort!

pairs_test = []
number_list.each do |d1|
   number_list.each do |d2|
      pairs_test << (d1.to_s + d2.to_s).to_i
   end
end

before_position = {}

number_list.each do |d|
   before_position[d] = []
end

f = File.open("../p079_keylog.txt", "r")

f.each_line do |line|
   # puts line
   pairs_test.each do |order|
      if line.to_s.include? order.to_s
         base = order.to_s[1].to_i
         bf = order.to_s[0].to_i
         unless before_position[base].include? bf
            before_position[base] << bf
         end
      end
   end
end

number_list.each do |d|
   before_position[d].sort!
end

puts before_position

# solution: 731 628 90
