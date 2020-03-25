use roots::Roots;
use roots::find_roots_quadratic;

use std::thread;
use std::time::Duration;

fn pentagon(n: i32) -> i32 {
  let c = n*(3n-1)/2 as i32;
  c
}

fn check_pentagon(n: i32) -> i8 {
  let roots = find_roots_quadratic(3f32, -1f32, -2*(nf32));

}

fn main() {
  let mut rec: i32 = 0;
  for i in 1..(10_i32.pow(7)) {
    for i in 1..i {
      pi = pentagon(i);
      pj = pentagon(j);
      let mut s: i32 = pi + pj;
      let mut d: i32 = pi - pj;
      if check_pentagon(s) && check_pentagon(d) {
        println!("good pair: {} {} with sum {} and diff {}", pi, pj, s, d);
        if rec == 0 || d < rec {
          rec = d;
        }
      }
    }
  }
}

