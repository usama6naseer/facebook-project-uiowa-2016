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
                <h1>The application is busy with another request.</h1>
                <br>
                <h1><u>Wait a minute and then try again.</u></h1>
                <br>
            </div>
            <div class="col-lg-12 text-center">
                <h3> Application Record</h3>
                <?php
                $count = 1;
                echo "<table class='table table-striped table-hover' style='border: 1px solid lightgrey'>";
                echo "<thead>";
                echo "<tr><th>#</th>";
                echo "<th style='text-align:center'>App Name</th>";
                echo "<th style='text-align:center'>App ID</th>";
                echo "<th style='text-align:center'>Redirect Vulnerability</th>";
                echo "<th style='text-align:center'>API Call Vulnerability</th></tr>";
                echo "</thead>";

                echo "<tbody>";
                $file = fopen("checked-apps-record.csv","r");
                    while(! feof($file))
                      {
                        $arr = fgetcsv($file);
                        $a1 = "Not Present";
                        $a2 = "Not Present";
                        if ($arr[4] == "yes" or $arr[4] == "1") {
                            $a1 = "Present";
                        }
                        if ($arr[5] == "yes" or $arr[5] == "1") {
                            $a2 = "Present";
                        }

                        echo "<tr>";
                          echo "<td>".$count."</td>";
                          echo "<td>".$arr[1]."</td>";
                          echo "<td>".$arr[0]."</td>";
                          echo "<td>".$a1."</td>";
                          echo "<td>".$a2."</td>";
                        echo "</tr>";
                        $count = $count + 1;
                    }
                echo "</tbody>";
                echo "</table>";
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
