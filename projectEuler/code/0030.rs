fn main() {
  let mut ss: i32 = 0;
  for i in 2..1000000 {
    let i_str: String =  i.to_string();
    let mut s: i32 = 0;
    for d in i_str.chars() {
      let di: i32 = d.to_string().parse().unwrap();
      s += di.pow(5)
    }
    if s == i {
      println!("{} has this property", i);
      ss += i;
    }
  }
  println!("{}", ss);
}

