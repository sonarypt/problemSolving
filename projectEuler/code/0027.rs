fn check_prime(n: i32) -> i32 {
  let mut s: i32 = 1;
  let temp_n = n as f32; 
  if n < 0 || n % 2 == 0 {
    s -= 1;
    // s
  }
  let temp_nn = temp_n.sqrt().ceil();
  let nn = temp_nn as i32;
  for i in (3..nn).step_by(2) {
    if n % i == 0 {
      s -= 1;
      break;
    }
  }
  s
}

fn quad(n: i32, a: i32, b: i32) -> i32 {
  n*n + a*n + b
}

fn main() {
  let mut r_step: i32 = 0;
  let mut r_a: i32 = 0;
  let mut r_b: i32 = 0;

  for a in -999..1001 {
    for b in -1000..1001 {
      let mut step: i32 = 0;
      while check_prime(quad(step, a, b)) == 1 {
        step += 1;
      }
      // if step > 60 {
      //   println!("pair ({}, {}) - step: {}", a, b, step);
      // }
      if step > r_step {
        r_step = step;
        r_a = a;
        r_b = b;
      }
    }
  }
  println!("record: ({}, {}) - step: {}", r_a, r_b, r_step);
}

