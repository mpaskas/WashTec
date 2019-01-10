<!DOCTYPE html>
<html lang="en">
<head>
    <!-- This is widget or page that should be displayed through Iframe -->
<script>
 setInterval(function() {
                  window.location.reload();
                }, 360000); 
</script>
    <meta charset="UTF-8">
     
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>WashTec Report</title>
</head>
<body >
<table    style="width:500px;background-color:#f2f2f2;margin:auto;" >

<tr><td colspan=3><img width=500 src="IMG_0404.jpg"></td></tr>
<tr>
    <?php
    $row = 1;
    // Read from file where results of scrape are stored
    if (($handle = fopen("result.csv", "r")) !== FALSE) {
      while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
            // First column text labeled text
            echo "<td>".$data[0] . "</td>";
            // Scraped icon
            echo '<td align="center"><img src="'.$data[1].'"></td>';
            // Read time of scraping
            echo "<td align='center' width='70px'>".$data[2] . "</td>";
            }
      fclose($handle);
    }
    ?>
    </tr>
    </table>
</body>

</html>