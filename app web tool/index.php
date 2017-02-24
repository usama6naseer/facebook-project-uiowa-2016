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
            margin-top: -140px;
            /*position: relative;*/
            /*top: -140px;*/
            /*right: 150;*/
            /*width: 1200px;*/
            /*height: 300px;*/
        }
        body {
            background-image: none !important;
            background-color: darkblue;
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
                <a class="navbar-brand topnav" href="#">Facebook Application Vulnerability Tester</a>
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
                        <h2>Put your Facebook application's security to the test</h2>
                        <!-- <h3>Put your application's security to the test</h3> -->
                        <!-- <hr class="intro-divider"> -->
                        <h4>Enter Facebook application I.D below</h4>
                        <hr class="intro-divider">

                        <!-- <div class="col-xs-4"> -->
                        <!-- <div class="span8" style="float:none; margin:0 auto"> -->
                            <form role="form" action="http://localhost/auto/run_python.php" method="post" onSubmit="return handleClick()">
                              <div class="form-group">
                                <label for="appID">App ID:</label>
                                <input type="text" name="name" class="form-control" id="appID">
                              </div>
                              <button type="submit" class="btn btn-default">Submit</button>
                            </form>
                        <br>
                        <hr class="intro-divider">
                        <h4>After hitting the submit button, wait a few moments.</h4>
                        <!-- <hr class="intro-divider"> -->
                        <!-- </div> -->
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
    $file = fopen("app-record.csv","r");
        while(! feof($file))
          {
            $arr = fgetcsv($file);
            $a1 = "Not Present";
            $a2 = "Not Present";
            if ($arr[0] == "1") {
                $a1 = "Present";
            }
            if ($arr[1] == "1") {
                $a2 = "Present";
            }
            if ($arr[0] == "1" or $arr[0] == "0") {
                $count = $count + 1;
                echo "<tr>";
                echo "<td><FONT COLOR='ffffff'>". $a1. "</FONT></td>";
                echo "<td><FONT COLOR='ffffff'>". $a2. "</FONT></td>";
                echo "<td><FONT COLOR='ffffff'>". $arr[3]. "</FONT></td>";
                echo "</tr>"; 
            }
          }

    fclose($file);
    echo  "</tbody>";
    echo "</table>";
    echo "</DIV>";
    ?>

    <!-- /.intro-header -->

    <!-- Page Content -->
<!-- 
	<a  name="contact"></a>
    <div class="banner">

        <div class="container">

            <div class="row">
                <div class="col-lg-6">
                    <h2>Connect to Start Bootstrap:</h2>
                </div>
                <div class="col-lg-6">
                    <ul class="list-inline banner-social-buttons">
                        <li>
                            <a href="https://twitter.com/SBootstrap" class="btn btn-default btn-lg"><i class="fa fa-twitter fa-fw"></i> <span class="network-name">Twitter</span></a>
                        </li>
                        <li>
                            <a href="https://github.com/IronSummitMedia/startbootstrap" class="btn btn-default btn-lg"><i class="fa fa-github fa-fw"></i> <span class="network-name">Github</span></a>
                        </li>
                        <li>
                            <a href="#" class="btn btn-default btn-lg"><i class="fa fa-linkedin fa-fw"></i> <span class="network-name">Linkedin</span></a>
                        </li>
                    </ul>
                </div>
            </div>

        </div>

    </div>
 -->    <!-- /.banner -->

    <!-- Footer -->
<!--     <footer>
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                    <ul class="list-inline">
                        <li>
                            <a href="#">Home</a>
                        </li>
                        <li class="footer-menu-divider">&sdot;</li>
                        <li>
                            <a href="#about">About</a>
                        </li>
                        <li class="footer-menu-divider">&sdot;</li>
                        <li>
                            <a href="#services">Services</a>
                        </li>
                        <li class="footer-menu-divider">&sdot;</li>
                        <li>
                            <a href="#contact">Contact</a>
                        </li>
                    </ul>
                    <p class="copyright text-muted small">Copyright &copy; Your Company 2014. All Rights Reserved</p>
                </div>
            </div>
        </div>
    </footer> -->

    <!-- jQuery -->
    <script src="js/jquery.js"></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="js/bootstrap.min.js"></script>

</body>

</html>
