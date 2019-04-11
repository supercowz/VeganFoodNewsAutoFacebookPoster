<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">

  <title>Chris Bednar's Vegan Food News Posts</title>
  <meta name="description" content="Chris Bednar's Vegan Food News Posts">
  <meta name="author" content="Chris bednar">

  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

</head>

<body>
	<div class="container">
		<div class="col-xs-12">
		<h1>Potential Vegan Food News Posts</h1>
		<br>
		<br>
		<table class="table">
		  <thead>
			<tr>
			  <th scope="col">Date</th>
			  <th scope="col">Headline</th>
			</tr>
		  </thead>
		  <tbody>
			<?php
			$dir = 'sqlite:../vegan_food_news_links.sqlite';
			$dbh  = new PDO($dir) or die("cannot open the database");
			$query =  "SELECT headline, url, published_date FROM rss_feed_item where is_posted = 0 order by published_date desc";
			foreach ($dbh->query($query) as $row)
			{
				$st = $row[2];
				$dt = new DateTime("@$st"); 
				echo '<tr>';
				echo '<td>' .date("F d, Y", $row[2]) . '</td>';
				echo '<td><a target="_blank" href="'. $row[1] . '">'. $row[0]. '</a></td>';
				echo '</tr>';
			}
			$dbh = null;
			?>
		  </tbody>
		</table>
		</div>
	</div>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</body>
</html>