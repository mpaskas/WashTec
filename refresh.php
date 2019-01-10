#!/usr/bin/php
<?php 
// This file should be put in crontab list for execution in order to provide
// update to result.csv 
// The absolute path should be adjusted
$command = escapeshellcmd('python3 /var/sentora/hostdata/zadmin/public_html/4_og_cx/chromeHeadless2.py');
$output = shell_exec($command);
echo $output;
?>
