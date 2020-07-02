<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Ontology</title>
<meta property="og:url" content="http://www.valeron.net/index.html" />
<meta property="og:type" content="website" />
<meta property="og:title" content="Free responsive web template Istria" />
<meta property="og:description" content="Free responsive web template Istria 1 by Valeron design studio" />
<meta property="og:image" content="http://www.valeron.net/img/valeron-artist.jpg" />
<meta name="description" content="Free responsive web template Istria 1 by Valeron design studio" />
<meta name="msapplication-tap-highlight" content="no" />
<meta name="robots" content="index,follow,all" />
<meta name="keywords" content="Izrada web stranica, web studio Istra" />
<meta name="author" content="Valeron design studio" />
<link rel="apple-touch-icon" sizes="57x57" href="img/apple-touch-icon-57x57.png">
<link rel="apple-touch-icon" sizes="60x60" href="img/apple-touch-icon-60x60.png">
<link rel="apple-touch-icon" sizes="72x72" href="img/apple-touch-icon-72x72.png">
<link rel="apple-touch-icon" sizes="76x76" href="img/apple-touch-icon-76x76.png">
<link rel="apple-touch-icon" sizes="114x114" href="img/apple-touch-icon-114x114.png">
<link rel="apple-touch-icon" sizes="120x120" href="img/apple-touch-icon-120x120.png">
<link rel="apple-touch-icon" sizes="144x144" href="img/apple-touch-icon-144x144.png">
<link rel="apple-touch-icon" sizes="152x152" href="img/apple-touch-icon-152x152.png">
<link rel="apple-touch-icon" sizes="180x180" href="img/apple-touch-icon-180x180.png">
<link rel="icon" type="image/png" href="img/favicon-32x32.png" sizes="32x32">
<link rel="icon" type="image/png" href="img/android-chrome-192x192.png" sizes="192x192">
<link rel="icon" type="image/png" href="img/favicon-96x96.png" sizes="96x96">
<link rel="icon" type="image/png" href="img/favicon-16x16.png" sizes="16x16">
<link rel="manifest" href="img/manifest.json">
<meta name="msapplication-TileColor" content="#da532c">
<meta name="msapplication-TileImage" content="img/mstile-144x144.png">
<meta name="theme-color" content="#ffffff">
<link rel="stylesheet" href="css/animsition.min.css">
<link rel="stylesheet" type="text/css" href="css/grid.min.css" />
<link rel="stylesheet" type="text/css" href="css/style.css" />
<link rel="stylesheet" type="text/css" href="css/menu.css" />
<link rel="stylesheet" type="text/css" href="css/overlay.css" />
<link rel="stylesheet" type="text/css" href="css/owl.carousel.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.5.1/animate.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.5.0/css/font-awesome.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/modernizr/2.8.3/modernizr.min.js"></script>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
<script src="http://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.3/jquery.easing.min.js"></script>
<script src="js/jquery.matchHeight-min.js"></script>
<script src="js/wow.min.js"></script>
<script src="js/animsition.min.js"></script>
<script src="js/jquery.parallax-scroll.js"></script>
<script src="js/owl.carousel.min.js"></script>
<script src="js/jquery.cbpQTRotator.min.js"></script>
<script src="js/functions.js"></script>
<script src="js/particle.js"></script>
</head>
<body>
  <div class="animsition-overlay">
    <div id="section-1">
      <header class="main_h">
        <div class="menufix"> <a class="logo" href="index.html"><img src="images/logo.png" alt="Hello"></a>
          <div class="mobile-toggle"> <span></span> <span></span> <span></span> </div>
          <nav>
            <ul>
              <li><a class="out active animsition-link" href="admin.jsp">HOME</a></li>
              <li class="line"><a class="out animsition-link" href="asso1.jsp">Gene Disease List</a></li>
              <li class="line"><a class="out animsition-link" href="adminupload.jsp">Update Gene</a></li>
              <li class="line"><a class="out animsition-link" href="login.jsp">LOGOUT</a></li>
            </ul>
          </nav>
        </div>
      </header>
      <div class="hero">
        <h1 id="title-1">WELCOME<em><%=uname%></em></h1>
        <div class="fixbottarro"> <a class="scroll" href="#section-2">Scroll for more</a> </div>
      </div>
    </div>
    <center>
      <h1 style="margin-left: 50px">GENE lIST</h1>
      <table style="margin-left: 100px;width: 1000px;background-color: darkgray;padding: 20px">
          <tr><td><strong>Disease ID</strong></td><td><strong>Disease Name</strong></td><td><strong>Symptoms</strong></td><td><strong>Precaution</strong></td></tr>
          <tr><td><%=did%></td><td><%=d0d%></td><td><%=ddd%></td><td><%=dd%></td></tr>
        </table>
      </center>
      <div class="colw_6 paddbott100 spec-r"></div>
    </div>
    <script type="text/javascript">
        $(document).ready(function() {
          $("#owl-partners").owlCarousel({
              autoPlay: 4000,
              stopOnHover : true,
              pagination : false,
              items : 5,
              itemsDesktop : [1199,4],
              itemsDesktopSmall : [959,3]
          });
        });
        $(function(){
      	$('#cbp-qtrotator').cbpQTRotator();
      	});
        var _gaq = _gaq || [];
        _gaq.push(['_setAccount', 'UA-15815880-3']);
        _gaq.push(['_trackPageview']);
        (function(){
          var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
          ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
          var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
        })();
    </script>
</body>
</html>
