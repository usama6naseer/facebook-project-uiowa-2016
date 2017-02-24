<?php
// check if other job is running
$file = fopen("working_on_another_job.csv","r");
$arr = fgetcsv($file);
fclose($file);

if (intval($arr[0]) == 0) {
	$list = array();
	array_push($list, 1);
	$file = fopen("working_on_another_job.csv","w");
	foreach ($list as $line) {
  	  fputcsv($file,explode(',',$line));
    }
	fclose($file);
}
else if (intval($arr[0]) == 1) {
	// header ( 'location: http://localhost/auto1/wait.php' ); 
	header ( 'location: wait.php' ); 
	exit (); 
}

$id = $_POST["name"];

$list = array();
array_push($list, $id);

$file = fopen("app-id.csv","w");

foreach ($list as $line)
  {
  fputcsv($file,explode(',',$line));
  }

fclose($file);

ini_set('max_execution_time', 1000000);
// $python = passthru('python testcode.py');
$python = system('python3 testcode.py > exe_result.txt');

session_start ();
$_SESSION['appid'] = $id;
session_write_close (); 

// header ( 'location: http://localhost/auto1/app_result.php' ); 
header ( 'location: app_result.php' ); 
exit (); 

?>

