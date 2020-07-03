<?php

include("../secret.php");

$conn = mysqli_connect($servername, $username, $password, $database);

if (!$conn) {
  die("Connection failed: " . mysqli_connect_error());
}
echo "Connected successfully \n";

// query to show all data from table
$show_table = "SELECT * FROM " . $table_name;

$result = mysqli_query($conn, $show_table);

echo '<table> \n';
echo '<tr><td>ID</td> <td>Thumbnail</td> <td>Title</td> <td>Status</td> <td>Action</td> </tr> \n';

if (mysqli_num_rows($result) > 0) {
   while ($row = mysqli_fetch_array($result)) {
      echo "<tr><td>" . $row[0] . "</td> <td><img border='0' alt='Thumbnail' src='" . $row[1] . "'width='100' height='100'></td> <td>" . $row[2] . "</td> <td>" . $row[3] . "</td></tr> \n";
   }
} else {
   echo "0 results";
}

echo '</table>';

mysqli_close($conn);

?>

