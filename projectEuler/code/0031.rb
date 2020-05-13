#!/usr/bin/env ruby

# solution_array = []

count = 0

(0..1).each do |p200|
   (0..2).each do |p100|
      (0..4).each do |p50|
         (0..10).each do |p20|
            (0..20).each do |p10|
               (0..40).each do |p5|
                  (0..100).each do |p2|
                     (0..200).each do |p1|
                        sum = 200*p200 + 100*p100 + 50*p50 + 20*p20 + 10*p10 + 5*p5 + 2*p2 + 1*p1
                        # conf = [p200, p100, p50, p20, p10, p5, p2, p1]
                        if sum == 200
                           count += 1
                        end
                        # if sum == 200 && not(solution_array.include?(conf))
                        puts p200.to_s + ", " + p100.to_s + ", " + p50.to_s + ", " + p20.to_s + ", " + p10.to_s + ", " + p5.to_s + ", " + p2.to_s + ", " + p1.to_s
                        #    solution_array << conf
                        # end
                     end
                  end
               end
            end
         end
      end
   end
end

puts "---"

puts count
# puts solution_array.length()
