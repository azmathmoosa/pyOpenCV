<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en-GB">
<head>
	<title>pyOpenCV</title>
	<link rel="stylesheet" type="text/css" href="webroot/screen.css" media="screen" />
</head>
<body>
<div class="colmask rightmenu">
	<div class="colleft">
		<div class="col1">
			<!-- Column 1 start -->
                <img src="/mjpg" id="liveimg" width="100%">
			<!-- Column 1 end -->
		</div>
		<div class="col2">
			<!-- Column 2 start -->
			<ul>
                % for each in allcv:
                     <li>{{each}}</li>
                % end
            </ul>
			<!-- Column 2 end -->
		</div>
	</div>
</div>


</body>
</html>