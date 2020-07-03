<html>
<head>
    <title>Pagination</title>
    <!-- Bootstrap CDN -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

    <link rel="stylesheet" href="main.css" type="text/css">
</head>
<body>
    <?php

        if (isset($_GET['pageno'])) {
            $pageno = $_GET['pageno'];
        } else {
            $pageno = 1;
        }

        $conn=mysqli_connect("localhost","user","user","sample_blogs");
        // Check connection
        if (mysqli_connect_errno()){
            echo "Failed to connect to MySQL: " . mysqli_connect_error();
            die();
        }

        $total_pages_sql = "SELECT COUNT(*) FROM posts";
        $result = mysqli_query($conn,$total_pages_sql);
        $total_rows = mysqli_fetch_array($result)[0];

        if (isset($_GET["items_number"])){
            if ($_GET["items_number"] == "all") {
                $no_of_records_per_page = $total_rows;
            } else {
                $no_of_records_per_page = $_GET["items_number"];
            }
        } else {
            $no_of_records_per_page = 5;
        }

        $offset = ($pageno-1) * $no_of_records_per_page;

        $total_pages = ceil($total_rows / $no_of_records_per_page);

        $sql = "SELECT * FROM posts LIMIT $offset, $no_of_records_per_page";
        $res_data = mysqli_query($conn,$sql);

        echo "<h1> Manage </h1>";

        echo "<table class='table'>\n";
        echo "<thead>\n";
        echo "<tr><td>ID</td> <td>Thumbnail</td> <td>Title</td> <td>Status</td> <td>Action</td> </tr>\n";
        echo "</thead>\n";

        echo "<tbody>\n";
        while($row = mysqli_fetch_array($res_data)){
            if ($row[4] == 1) {
                $status = "Enabled";
            } else {
                $status = "Disabled";
            }
            echo "<tr><td>" . $row[0] . "</td> <td><img border='0' alt='Thumbnail' src='" . $row[1] . "' width='100' height='100'></td> <td>" . $row[2] . "</td> <td>" . $status . "</td> <td> <a href='show.php?id=" . $row [0] . "'>Show</a> | <a href='form_edit.php?id=" . $row[0] . "'>Edit</a> | <a target='_blank' href='delete.php?title=" . $row[2] . "'>Delete</a> </td></tr> \n";
        }

        echo "</tbody>\n";
        echo "</table>\n";

        mysqli_close($conn);
    ?>
    <form>
        <label for="page">Page:</label>
        <select name="items_number" onchange="this.form.submit()">
            <!-- <option value="5">5</option> 
            <option value="10">10</option>
            <option value="50">50</option>
            <option value="all">All</option> -->
            <option value="5" <?php if ($_GET['items_number'] == '5') echo 'selected="selected"'; ?> >5</option> 
            <option value="10" <?php if ($_GET['items_number'] == '10') echo 'selected="selected"'; ?> >10</option>
            <option value="50" <?php if ($_GET['items_number'] == '50') echo 'selected="selected"'; ?> >50</option>
            <option value="all" <?php if ($_GET['items_number'] == 'all') echo 'selected="selected"'; ?> >All</option>
        </select>
   </form>
    <ul class="pagination justify-content-center">
        <li class="page-item"><a href="?pageno=1">First</a></li>
        <li class="page-item <?php if($pageno <= 1){ echo 'disabled'; } ?>">
            <a href="<?php if($pageno <= 1){ echo '#'; } else { echo "?items_number=" . $no_of_records_per_page . "&pageno=".($pageno - 1); } ?>">Prev</a>
        </li>
        <li class="page-item <?php if($pageno >= $total_pages){ echo 'disabled'; } ?>">
            <a href="<?php if($pageno >= $total_pages){ echo '#'; } else { echo "?items_number=" . $no_of_records_per_page . "&pageno=".($pageno + 1); } ?>">Next</a>
        </li>
        <li class="page-item"><a href="?pageno=<?php echo $total_pages; ?>">Last</a></li>
    </ul>
</body>
</html>

