<?php


$id = $_POST["name"];

$list = array();
array_push($list, $id);

$file = fopen("app-id.csv","w");

foreach ($list as $line)
  {
  fputcsv($file,explode(',',$line));
  }

fclose($file);

// 41158896424
// $python = exec('C:\xampp\htdocs\cgi-bin\test.py');
// $python = system('python ..\..\cgi-bin\test.py');
// echo shell_exec('python ..\..\cgi-bin\test.py');

ini_set('max_execution_time', 1000000);
// $python = system('python testcode.py > exe_result.txt');
// $python = exec('python testcode.py');
$python = passthru('python testcode.py');

// $vul_1 = -1;
// $vul_2 = -1;
// $file = fopen("app-result.csv","r");
// 	$arr = fgetcsv($file);
// 	$vul_1 = $arr[0];
// 	$vul_2 = $arr[1];
// fclose($file);

// echo $vul_1;
// echo $vul_2;
// $res1 = "";
// $res2 = "";
// if ($vul_1==1){
// 	$res1 = "Present";
// }
// else if ($vul_1==0){
// 	$res1 = "Not Present";
// }
// else {
// 	$res1 = "Not Applicable since app ID is not valid";	
// }
// if ($vul_2==1){
// 	$res2 = "Present";
// }
// else if ($vul_2==0){
// 	$res2 = "Not Present";
// }
// else {
// 	$res2 = "Not Applicable since app ID is not valid";	
// }

// session_id('myID');
session_start ();
// if ($vul_1==-1) {
// 	$_SESSION['appid'] = strval($id)." IS NOT VALID";
// }
// else{
$_SESSION['appid'] = $id;
// }
// // $_SESSION['appid'] = $id;
// $_SESSION['vul1'] = $res1;
// $_SESSION['vul2'] = $res2; 
session_write_close (); 
header ( 'location: http://localhost/auto/app_result.php' ); 
exit (); 

?>

