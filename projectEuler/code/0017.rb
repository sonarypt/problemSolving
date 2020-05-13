#!/usr/bin/env ruby

letters = { # use zero here for convenience
   0 => 0, 1 => 3, 2 => 3, 3 => 5, 4 => 4, 5 => 4, 6 => 3, 7 => 5, 8 => 5, 9 => 4,
   10 => 3, 11 => 6, 12 => 6, 13 => 8, 14 => 8, 15 => 7, 16 => 7, 17 => 9, 18 => 8, 19 => 8,
   20 => 6, 30 => 6, 40 => 5, 50 => 5, 60 => 5, 70 => 7, 80 => 6, 90 => 6
}

(1..999).each do |d|
   unless letters.key?(d)
      if d < 100
         d1 = d/10
         d2 = d - d1*10
         letters[d] = letters[d1*10] + letters[d2]
      else
         d1 = d/100
         d2 = d - d1*100
         if d2 == 0
            letters[d] = letters[d1] + 10       # "hundred and" contains 10 letters
         else
            letters[d] = letters[d1*100] + letters[d2]
         end
      end
   end
end

letters[1000] = 11

puts letters
puts letters.values.inject(0, :+)

