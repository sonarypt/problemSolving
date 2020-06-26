<?php

// This script is intended to use generate random data for testing

include("./secret.php");

echo $servername . "\n";
echo $username . "\n";
echo $password . "\n";
echo $database . "\n";

$conn = mysqli_connect($servername, $username, $password, $database);

if (!$conn) {
  die("Connection failed: " . mysqli_connect_error());
}
echo "Connected successfully \n";

# check the existence of table named "posts", if not then create
$check_table = "SELECT 1 FROM posts LIMIT 1";
$create_table = "CREATE TABLE posts (id INT NOT NULL AUTO_INCREMENT, thumb_link VARCHAR(90), title VARCHAR(90), status VARCHAR(90), )";

if (mysqli_query($conn, $check_table) == FALSE) {
   echo "Table does not exist. Created new one \n";
   mysqli_query($conn, $create_table);
} else {
   echo "Table exists. Do nothing.\n";
}

// query for random insert, use lorem ipsum image for random images
function insert_randomly($conn) {
   $raw_title = file_get_contents('https://loripsum.net/api/1/short');
   $title = str_replace(array("\r", "\n"), '', (string) $raw_title);
   $random_insert = "INSERT INTO posts (thumb_link, title, status) VALUES ('https://picsum.photos/200', '" . $title . "', 'Enabled')";
   if (mysqli_query($conn, $random_insert) == TRUE) {
      echo "New record created successfully\n";
   } else {
      echo "Error: " . $random_insert . ". " . mysqli_error($conn) . "\n";
   }
}

// create 100 samples
for($i = 1; $i<=100; $i++) {
   insert_randomly($conn);
}

// query to show all data from table
$show_table = "SELECT * FROM " . $table_name;

$result = mysqli_query($conn, $sql);

if (mysqli_num_rows($result) > 0) {
   while ($row = mysqli_fetch_array($result)) {
      echo $row["customerid"] . "\n";
   }
} else {
   echo "0 results";
}

mysqli_close($conn);

?>

