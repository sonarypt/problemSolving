#!/usr/bin/env ruby

diff = 4000

(1..2000).each do |w|
   (w..2000).each do |h|
      d = (w*(w+1)*h*(h+1)/4 - 2000000).abs
      if d < diff
         area = w*h
         puts w.to_s + " " + h.to_s + " : a = " + area.to_s + " , diff = " + d.to_s
         diff = d
      end
   end
end
