use std::thread;
use std::time::Duration;

fn factorial(n: i32) -> i32 {
  let mut s: i32 = 1;
  for u in 1..(n+1) {
    s *= u;
  }
  s
}

fn main() {
  
  let handle = thread::spawn(|| {
    let mut rs1: i32 = 0;
    for d in 1..(10_i32.pow(6)) {
      let d_str: String = d.to_string();
      let mut s: i32 = 0;
      for j in d_str.chars() {
        let ji: i32 = j.to_string().parse().unwrap();
        s += factorial(ji);
      }
      if s == d {
        println!("number: {}", d);
        rs1 += d;
      }
      thread::sleep(Duration::from_millis(1));
    }
  });
  
  let mut rs2: i32 = 0;
  for d in (10_i32.pow(6))..(10_i32.pow(7)) {
    let d_str: String = d.to_string();
    let mut s: i32 = 0;
    for j in d_str.chars() {
      let ji: i32 = j.to_string().parse().unwrap();
      s += factorial(ji);
    }
    if s == d {
      println!("number: {}", d);
      rs2 += d;
    }
    thread::sleep(Duration::from_millis(1));
  }
  handle.join().unwrap();
  let rs = rs1 + rs2;
  println!("{}", rs);
}

