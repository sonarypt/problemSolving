<?php

// This script is intended to use generate random data for testing

include("./secret.php");

echo $servername . "\n";
echo $username . "\n";
echo $password . "\n";
echo $database . "\n";
echo $table_name . "\n";

$conn = mysqli_connect($servername, $username, $password, $database);

if (!$conn) {
  die("Connection failed: " . mysqli_connect_error());
}
echo "Connected successfully \n";

# check the existence of table named "posts", if not then create
$check_table = "SELECT 1 FROM " . $table_name . " LIMIT 1";
$create_table = "CREATE TABLE " . $table_name . " (id INT NOT NULL AUTO_INCREMENT, thumb_link VARCHAR(90), title VARCHAR(90), status VARCHAR(90), PRIMARY KEY (id))";

if (mysqli_query($conn, $check_table) == FALSE) {
   echo "Table does not exist. Created new one \n";
   mysqli_query($conn, $create_table);
   echo mysqli_error($conn) . "\n";
} else {
   echo "Table exists. Do nothing.\n";
}

// query for random insert, use lorem ipsum image for random images
function insert_randomly($conn, $table_name) {
   $title = rand(10000000000, 99999999999);
   $random_insert = "INSERT INTO " . $table_name . " (thumb_link, title, status) VALUES ('https://picsum.photos/200', '" . $title . "', 'Enabled')";
   if (mysqli_query($conn, $random_insert) == TRUE) {
      echo "New record created successfully\n";
   } else {
      echo "Error: " . $random_insert . ". " . mysqli_error($conn) . "\n";
   }
}

// create next 100 samples
for($i = 1; $i<=100; $i++) {
   insert_randomly($conn, $table_name);
}

?>

