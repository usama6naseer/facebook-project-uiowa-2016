<?php
session_start();
?>

<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>App Tester</title>

    <!-- Bootstrap Core CSS -->
    <link href="css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom CSS -->
    <style>
    body {
        padding-top: 70px;
        background-color: #eaeae1;
        /*background-color: #d5d5c3;*/
        /* Required padding for .navbar-fixed-top. Remove if using .navbar-static-top. Change if height of navigation changes. */
    }
    h4 { 
        border-bottom: 1px solid #CCC;
        padding-bottom: 1px;
    }
    td:hover {
      background-color: #e6e6e6;
    }

    </style>



</head>

<body>

    <!-- Navigation -->
    <nav class="navbar navbar-inverse navbar-fixed-top topnav" role="navigation">
        <div class="container topnav">
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand topnav" href="index.php">Facebook Application Vulnerability Tester</a>
            </div>
            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul class="nav navbar-nav navbar-right">
                    <li>
                        <a href="about.html">About</a>
                    </li>
<!--                     <li>
                        <a href="#services">Services</a>
                    </li> -->
                </ul>
            </div>
            <!-- /.navbar-collapse -->
        </div>
        <!-- /.container -->
    </nav>


    <!-- Page Content -->
    <div class="container">

        <div class="row">
            <div class="col-lg-12 text-center">
                <h1>Application Test Completed.</h1>
                <!-- <hr class="intro-divider"> -->
                        <?php
                            $vul_1 = -1;
                            $vul_2 = -1;
                            $id = $_SESSION['appid'];
                            $name = strval($id).".csv";

                            $file = fopen($name,"r");
                                $arr = fgetcsv($file);
                                $vul_1 = $arr[0];
                                $vul_2 = $arr[1];
                            fclose($file);
                            $appid = $_SESSION['appid'];
                            
                            // if ($vul_1 == 0) {
                                // $vstr1 = "Not Present";
                            // }
                            $vstr1 = "Not Present";
                            if ($vul_1 == 1) {
                                $vstr1 = "Present";
                            }
                            if ($vul_1 == -1) {
                                $vstr1 = "Not Applicable since app ID is not valid";
                                $appid = $appid." is Not Valid";

                            }
                            // if ($vul_2 == 0) {
                                // $vstr2 = "Not Present";
                            // }
                            $vstr2 = "Not Present";
                            if ($vul_2 == 1) {
                                $vstr2 = "Present";
                            }
                            if ($vul_2 == -1) {
                                $vstr2 = "Not Applicable since app ID is not valid";
                            }
                            $app_name = $arr[3];
                            $dau = $arr[4];
                            $daur = $arr[5];

                            $perm = $arr[6];
                            $prm = 'Not Present';
                            $arr = explode(" ",$perm);
                            foreach ($arr as $st) {
                                if ($st == "publish_actions") {
                                    $prm = 'Present';
                                }
                            }
                            echo "<DIV class='col-lg-12 text-center'>";
                                echo "<table border='1' style='border: 1px solid lightgrey' align='center' width='900'>";
                                // echo "<thead>";
                                    // echo "<tr><th style='text-align:center'>Result</th></tr>";
                                // echo "</thead>";
                                // echo "<tbody>";
                                    echo "<tr>";
                                        echo "<td bgcolor='#ffffff'><h3>Application Name: <u>".$app_name." (".$appid.")"."</u></h3></td>";
                                    echo "</tr>";
                                    echo "<tr>";
                                        echo "<td bgcolor='#ffffff'><h3>Redirect Vulnerability: <u>".$vstr1."</u></h3></td>";
                                    echo "</tr>";
                                    echo "<tr>";
                                        echo "<td bgcolor='#ffffff'><h3>API Call Vulnerability: <u>".$vstr2."</u></h3></td>";
                                    echo "</tr>";
                                    echo "<tr>";
                                        echo "<td bgcolor='#ffffff'><h3>Publish Actions Permission: <u>".$prm."</u></h3></td>";
                                    echo "</tr>";
                                    // echo "<tr>";
                                        // echo "<td bgcolor='#ffffff'><h3>Daily Active Users: <u>".$dau."</u></h3></td>";
                                    // echo "</tr>";
                                    // echo "<tr>";
                                        // echo "<td bgcolor='#ffffff'><h3>Daily Active Users Rank: <u>".$daur."</u></h3></td>";
                                    // echo "</tr>";
                                // echo "</tbody>";
                                echo "</table>";
                                echo "<br>";
                                echo("<h4>".$app_name." has <u>".$dau."</u> Daily Active Users and has a DAU rank of <u>".$daur.".<u/></h4>");
                            echo "</DIV>";
                        ?>
                        
            </div>
            <div class="col-lg-12 text-center">
                <h3> Application's History</h3>
                <?php
                $count = 1;
                echo "<table class='table table-striped table-hover' style='border: 1px solid lightgrey'>";
                echo "<thead>";
                echo "<tr>";
                echo "<th style='text-align:center'>Redirect Vulnerability</th>";
                echo "<th style='text-align:center'>API Call Vulnerability</th>";
                echo "<th style='text-align:center'>Timestamp</th></tr>";
                echo "</thead>";

                echo "<tbody>";

                $app_id = $_SESSION['appid'];
                
                $file = fopen("app-record.csv","r");
                    while(! feof($file))
                      {
                        $arr = fgetcsv($file);
                        // $count = $count + 1;
                        if ($count == 20) {
                            break;
                        }
                        $a1 = "Not Present";
                        $a2 = "Not Present";
                        if ($arr[4] == "1") {
                            $a1 = "Present";
                        }
                        if ($arr[5] == "1") {
                            $a2 = "Present";
                        }
                        if ($arr[0] == $app_id){
                            if ($arr[4] == "1" or $arr[4] == "0") {
                                $count = $count + 1;
                                echo "<tr>";
                                    echo "<td>".$a1."</td>";
                                    echo "<td>".$a2."</td>";
                                    echo "<td>".$arr[6]."</td>";
                                echo "</tr>";
                            }
                        }
                      }

                fclose($file);
                echo  "</tbody>";
                echo "</table>";
                echo "</DIV>";
                $name = strval($app_id).".csv";
                unlink($name);

                if ($count == 1) {
                    echo("<div class='col-lg-12 text-center'>");
                    echo("<h3>No Previous Record Present For This Application </h3>");
                    echo("</div>");
                }

                $li = array();
                array_push($li, 0);
                $file = fopen("working_on_another_job.csv","w");
                foreach ($li as $line) {
                  fputcsv($file,explode(',',$line));
                }
                fclose($file);

                ?>
            </div>
        </div>
    </div>
    <!-- /.container -->


    <!-- jQuery Version 1.11.1 -->
    <script src="js/jquery.js"></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="js/bootstrap.min.js"></script>




</body>

</html>
