
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Facebook App Vulnerability Tester</title>

    <!-- Bootstrap Core CSS -->
    <link href="css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom CSS -->
    <link href="css/landing-page.css" rel="stylesheet">

    <!-- Custom Fonts -->
    <link href="font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">
    <link href="http://fonts.googleapis.com/css?family=Lato:300,400,700,300italic,400italic,700italic" rel="stylesheet" type="text/css">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->
    <script>
        function handleClick()
          {

            // write waiting script

            // document.getElementById("intro-header").innerHTML='<object type="text/html" data="main.html" ></object>';
            // window.location.href = "http://localhost/auto/main.html"
            // alert("Submit");
            // var div = document.getElementById('intro-header');
            // div.innerHTML = div.innerHTML + "<h2>YYYYYYYYYYYYYYYYYYYYYYYYY</h2>";

            return true;
          }
    </script>

    <style>
        div.row {
            margin-top: -200px;
            /*position: relative;*/
            /*top: -140px;*/
            /*right: 150;*/
            /*width: 1200px;*/
            /*height: 300px;*/
        }
    }
    </style>
</head>

<body>

    <!-- Navigation -->
    <nav class="navbar navbar-default navbar-fixed-top topnav" role="navigation">
        <div class="container topnav">
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand topnav" href="index.html">Facebook Application Vulnerability Tester</a>
            </div>
            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul class="nav navbar-nav navbar-right">
                    <li>
                        <a href="about.html">About</a>
                    </li>
                    <li>
                        <a href="contact.html">Contact</a>
                    </li>
                    
                </ul>
            </div>
            <!-- /.navbar-collapse -->
        </div>
        <!-- /.container -->
    </nav>


    <!-- Header -->
    <a name="about"></a>
    <div class="intro-header">
        <div class="container">

            <div class="row">
                <div class="col-lg-12">
                    <div class="intro-message">
                        <h2>Application Test Completed.</h2>
                        <!-- <h3>Put your application's security to the test</h3> -->
                        <!-- <hr class="intro-divider"> -->
                        <!-- <h4>Application ID</h4> -->
                        <?php
                            // echo "<br>";
                            $vul_1 = -1;
                            $vul_2 = -1;
                            $file = fopen("app-result.csv","r");
                                $arr = fgetcsv($file);
                                $vul_1 = $arr[0];
                                $vul_2 = $arr[1];
                            fclose($file);
                            $appid = -1;
                            $file = fopen("app-id.csv","r");
                                $arr = fgetcsv($file);
                                $appid = $arr[0];
                            fclose($file);
                            
                            if ($vul_1 == 0) {
                                $vstr1 = "Not Present";
                            }
                            if ($vul_1 == 1) {
                                $vstr1 = "Present";
                            }
                            if ($vul_1 == -1) {
                                $vstr1 = "Not Applicable since app ID is not valid";
                                $appid = $appid." is Not Valid";

                            }
                            if ($vul_2 == 0) {
                                $vstr2 = "Not Present";
                            }
                            if ($vul_2 == 1) {
                                $vstr2 = "Present";
                            }
                            if ($vul_2 == -1) {
                                $vstr2 = "Not Applicable since app ID is not valid";
                            }

                            echo "<h3>Application ID:  <FONT COLOR='ffff00'>".$appid."</FONT></h3>";
                            echo "<hr class='intro-divider'>";
                            echo "<h3>Redirect Vulnerability:  <FONT COLOR='ffff00'>".$vstr1."</FONT></h3>";
                            echo "<hr class='intro-divider'>";
                            echo "<h3>API Call Vulnerability:  <FONT COLOR='ffff00'>".$vstr2."</FONT></h3>";
                            echo "<hr class='intro-divider'>";
                        ?>
                    </div>
                </div>
            </div>

        </div>
        <!-- /.container -->

    </div>
    <?php
    $count = 0;
    echo "<DIV class='alltable' STYLE='position:absolute; top:310px; left:50px; width:1250px; height:50px'>";
    echo "<table class='table table-bordered'>";
    echo "<caption><strong><FONT SIZE='+2' COLOR='ffffff'> Application's Record </FONT></strong></caption>";
    echo "<thead>";
    echo "<tr> <th><FONT SIZE='+0.5' COLOR='ffffff'>Redirect Vulnerability</FONT></th>";
    echo "<th><FONT SIZE='+0.5' COLOR='ffffff'>API Call Vulnerability</FONT></th>";
    echo "<th><FONT SIZE='+0.5' COLOR='ffffff'>Timestamp</FONT></th> </tr>";
    echo "</thead>";
    echo "<tbody>";
    $app_id = 0;
    $f1 = fopen("app-id.csv","r");
        $arr = fgetcsv($f1);
        $app_id = $arr[0];
    fclose($f1);
    
    $file = fopen("app-record.csv","r");
        while(! feof($file))
          {
            $arr = fgetcsv($file);
            // $count = $count + 1;
            if ($count == 6) {
                break;
            }
            $a1 = "Not Present";
            $a2 = "Not Present";
            if ($arr[0] == "1") {
                $a1 = "Present";
            }
            if ($arr[1] == "1") {
                $a2 = "Present";
            }
            if ($arr[2] == $app_id){
                if ($arr[0] == "1" or $arr[0] == "0") {
                    $count = $count + 1;
                    echo "<tr>";
                    echo "<td><FONT COLOR='ffffff'>". $a1. "</FONT></td>";
                    echo "<td><FONT COLOR='ffffff'>". $a2. "</FONT></td>";
                    echo "<td><FONT COLOR='ffffff'>". $arr[3]. "</FONT></td>";
                    // echo "<td>". gmdate('m/d/Y H:i:s', $arr[2]). "</td>";
                    echo "</tr>"; 
                }
            }
          }

    fclose($file);
    echo  "</tbody>";
    echo "</table>";
    echo "</DIV>";
    ?>

    
    <!-- jQuery -->
    <script src="js/jquery.js"></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="js/bootstrap.min.js"></script>

</body>

</html>
