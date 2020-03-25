fn main() {
  let mut s: u64 = 0;
  for x in 0..1001 as u64 {
    s = s + x.pow(x.try_into().unwrap());
  }
  let s_str: String = s.to_string();
  println!("last 10 digits: {}", &s_str[10..]);
}

