fn pentagon(n: u32) -> u32 {
   let c = n*(3*n-1)/2 as u32;
   c
}

fn is_pentagon(n: u32) -> bool {
   let mm = 24*n+1;
   let m = mm as f32;
   // let id:u32;
   if m.sqrt().fract() == 0.0 {
      // id = 0;
      // while pentagon(id+1) < n {
      //    id += 1
      // }
      let ms = m.sqrt() as u32;
      if ms % 6 == 5 {
         return true;
      } else {
         return false;
      }
   } else {
      return false;
   }

   // if pentagon(id) == n {
   //    return true;
   // } else {
   //    return false;
   // }
}

fn main() {
   let mut rec: u32 = 0;
   for i in 1..(10_u32.pow(3)) {
      for j in 1..i {
         println!("{}, {}", i, j);
         // let pi = pentagon(i) as u32;
         // let pj = pentagon(j) as u32;
         // println!(pi);
         // let s: u32 = pi + pj;
         // let d: u32 = pi - pj;
         // println!("good pair: {} {} with sum {} and diff {}", pi, pj, s, d);
         // if is_pentagon(s) && is_pentagon(d) {
         //    println!("good pair: {} {} with sum {} and diff {}", pi, pj, s, d);
         //    if rec == 0 || d < rec {
         //       rec = d;
         //    }
         // }
      }
   }
}

