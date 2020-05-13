def gcd(a, b)
   b == 0 ? a : gcd(b, a.modulo(b))
end

def ext(n)
   ext = 0_u64
   subrange = (2..n-1)
   subrange.each do |s|
      unless gcd(s, n) == 1
         ext += 6
      end
   end
   return ext
end

def ring(n)
   if n == 1
      return 0
   else
      return 6
   end
end

def hexa(n)
   hx = 0_u64   # number of points hidden from center
   range = (1..n)
   range.each do |r|
      hx = hx + ring(r) + ext(r)
   end
   return hx
end

puts hexa(100_000_000)
