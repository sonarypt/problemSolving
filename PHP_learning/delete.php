<?php

$title = $_GET["title"];

$conn = mysqli_connect("localhost", "user", "user", "sample_blogs");

$delete_query = "DELETE FROM posts where title='" . $title . "'";

if (mysqli_query($conn, $delete_query)) {
    echo "Record deleted successfully post " . $title;
} else {
    echo "Error deleting record: " . mysqli_error($conn);
}

mysqli_close($conn);

?>



