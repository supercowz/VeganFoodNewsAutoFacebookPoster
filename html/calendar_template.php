<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">

  <title>Chris Bednar's Tools</title>
  <meta name="description" content="Chris Bednar's Tools">
  <meta name="author" content="Chris bednar">

  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

</head>

<body>
	<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>

  	<script src="https://code.jquery.com/jquery-3.4.0.min.js" integrity="sha256-BJeo0qm959uMBGb65z40ejJYGSgR7REI4+CW1fNKwOg=" crossorigin="anonymous"></script>

	<div id="fb-root"></div>
	<script async defer crossorigin="anonymous" src="https://connect.facebook.net/en_US/sdk.js#xfbml=1&version=v4.0&appId=467632353674600&autoLogAppEvents=1"></script>

	<div class="container">
		<div class="col-xs-12">
		<h1>Potential Vegan Food News Posts</h1>
		<br>
		<br>
		<table class="table">
		  <thead>
			<tr>
			  <th scope="col">Start Date</th>
			  <th scope="col">End Date</th>
			  <th scope="col">Event Title</th>
			  <th scope="col">Description</th>
			</tr>
		  </thead>
		  <tbody>
			<?php
			ini_set('display_errors', 'On');
			$dir = 'sqlite:/var/www/vegan_food_news_links.sqlite';
			$dbh  = new PDO($dir) or die("cannot open the database");
			
			$query =  "SELECT date_start, date_end, summary, description FROM calendar_event order by date_start desc limit 20";
			foreach ($dbh->query($query) as $row)
			{
				echo '<tr>';
				echo '<td>' . $row[0] . '</td>';
				echo '<td>' . $row[1] . '</td>';
				echo '<td>' . $row[2] . '</td>';
				echo '<td>' . $row[3] . '</td>';
				echo '</tr>';
			}
			$dbh = null;
			?>
		  </tbody>
		</table>
		</div>
	</div>
</body>
</html>
