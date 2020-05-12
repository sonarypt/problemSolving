#!/usr/bin/env ruby

line_array = []
numerical_array = []

f = File.open("../p099_base_exp.txt", "r")

f.each_line do |line|
   base, exp = line.split(",")
   line_array << [base.to_i, exp.to_i]
   numerical_array << exp.to_i*Math.log(base.to_i)
end
puts "Done calculation"

puts id = numerical_array.index(numerical_array.max)
puts line_array[id]
