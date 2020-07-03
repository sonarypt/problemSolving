<?php

$id = $_GET["id"];

$conn = mysqli_connect("localhost", "user", "user", "sample_blogs");

$show_query = "SELECT * FROM posts where id=" . $id;

echo "<h2> Detail information </h2>";
echo "<button type='button' class='btn btn-default' onclick='history.back()'> Back </button> <br>";

$show_data = mysqli_query($conn, $show_query);

while($r = mysqli_fetch_array($show_data)) {
    echo "<img border='0' alt='Thumbnail' src='" . $r[1] . "'> " . $r[3];
}

?>
