<?php

$id = $_GET["id"];

$conn = mysqli_connect("localhost", "user", "user", "sample_blogs");

$get_info = "SELECT * FROM posts WHERE id=" . $id;

echo $get_info;

$get_data = mysqli_query($conn, $get_info);

$row = mysqli_fetch_array($get_data);

echo "<h2> Detail information </h2>";
echo "<button type='button' class='btn btn-default' onclick='history.back()'> Back </button> <br>";

echo "<form action='/edit.php'>
    <label for='title'>Title:</label><br>
    <input type='text' id='title' name='title' value='" . $row[2] . "'><br>
    <label for='description'>Description:</label><br>
    <input type='text' id='description' name='description' value='" . $row[3] . "' size='125' maxlength='100'><br><br>
    <label for='myfile'> Thumbnail file </label>
    <input type='file' id='myfile' name='myfile'> 
    <label for='status'> Status </label>
    <select id='status' name='status'>
        <option value='1'> Enabled </option>
        <option value='2'> Disabled </option>
    </select>
    <input type='submit' value='Submit'>
</form> "

?>

