<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <script type="text/javascript" src="val.js"></script>
    <title>Signup</title>
    <meta property="og:url" content="http://www.valeron.net/index.html" />
    <meta property="og:type" content="website" />
    <meta
      property="og:title"
      content="Free responsive web template Istria - Contact"
    />
    <meta
      property="og:description"
      content="Free responsive web template Istria by Valeron design studio - Contact"
    />
    <meta
      property="og:image"
      content="http://www.valeron.net/img/valeron-artist.jpg"
    />
    <meta
      name="description"
      content="Free responsive web template Istria by Valeron design studio - Contact"
    />
    <meta name="msapplication-tap-highlight" content="no" />
    <meta name="robots" content="index,follow,all" />
    <meta name="keywords" content="Izrada web stranica, web studio Istra" />
    <meta name="author" content="Valeron design studio" />
    <link
      rel="apple-touch-icon"
      sizes="57x57"
      href="img/apple-touch-icon-57x57.png"
    />
    <link
      rel="apple-touch-icon"
      sizes="60x60"
      href="img/apple-touch-icon-60x60.png"
    />
    <link
      rel="apple-touch-icon"
      sizes="72x72"
      href="img/apple-touch-icon-72x72.png"
    />
    <link
      rel="apple-touch-icon"
      sizes="76x76"
      href="img/apple-touch-icon-76x76.png"
    />
    <link
      rel="apple-touch-icon"
      sizes="114x114"
      href="img/apple-touch-icon-114x114.png"
    />
    <link
      rel="apple-touch-icon"
      sizes="120x120"
      href="img/apple-touch-icon-120x120.png"
    />
    <link
      rel="apple-touch-icon"
      sizes="144x144"
      href="img/apple-touch-icon-144x144.png"
    />
    <link
      rel="apple-touch-icon"
      sizes="152x152"
      href="img/apple-touch-icon-152x152.png"
    />
    <link
      rel="apple-touch-icon"
      sizes="180x180"
      href="img/apple-touch-icon-180x180.png"
    />
    <link
      rel="icon"
      type="image/png"
      href="img/favicon-32x32.png"
      sizes="32x32"
    />
    <link
      rel="icon"
      type="image/png"
      href="img/android-chrome-192x192.png"
      sizes="192x192"
    />
    <link
      rel="icon"
      type="image/png"
      href="img/favicon-96x96.png"
      sizes="96x96"
    />
    <link
      rel="icon"
      type="image/png"
      href="img/favicon-16x16.png"
      sizes="16x16"
    />
    <link rel="manifest" href="img/manifest.json" />
    <meta name="msapplication-TileColor" content="#da532c" />
    <meta name="msapplication-TileImage" content="img/mstile-144x144.png" />
    <meta name="theme-color" content="#ffffff" />
    <link rel="stylesheet" href="css/animsition.min.css" />
    <link rel="stylesheet" type="text/css" href="css/grid.min.css" />
    <link rel="stylesheet" type="text/css" href="css/style.css" />
    <link rel="stylesheet" type="text/css" href="css/menu.css" />
    <link rel="stylesheet" type="text/css" href="css/social.css" />
    <link rel="stylesheet" type="text/css" href="css/slickform.css" />
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.5.1/animate.min.css"
    />
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.5.0/css/font-awesome.min.css"
    />
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome-animation/0.0.8/font-awesome-animation.min.css"
    />
    <script src="https://cdnjs.cloudflare.com/ajax/libs/modernizr/2.8.3/modernizr.min.js"></script>
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <script type="text/javascript" src="js/jquery.matchHeight-min.js"></script>
    <script src="js/wow.min.js"></script>
    <script src="js/animsition.min.js"></script>
    <script src="js/Slickform.js"></script>
    <script src="js/functions.js"></script>
  </head>
  <body>
    <div class="animsition-overlay">
      <div class="horBar2Bxx wow fadeInLeftBig" data-wow-duration="3s"></div>
      <header class="main_h">
        <div class="menufix">
          <a class="logo" href="index.html"
            ><img src="images/logo.jpg" alt="Hello"
          /></a>
          <div class="mobile-toggle">
            <span></span> <span></span> <span></span>
          </div>
          <nav>
            <ul>
              <li class="line">
                <a class="out animsition-link" href="index.html">HOME</a>
              </li>
              <li>
                <a class="out animsition-link" href="login.jsp">SIGN IN</a>
              </li>
              <li class="line">
                <a class="out animsition-link" href="signup.html">SIGNUP</a>
              </li>
            </ul>
          </nav>
        </div>
      </header>
    </div>
    <div class="grid">
      <div class="row paddtop100">
        <div class="colw_6 spec-l-cont border-right">
          <h3>GENE INFO</h3>
          <a><img src="img/gen.png" alt="Google Maps" class="full-width" /></a>
        </div>
        <div class="colw_6 paddbott100 spec-r-cont">
          <h3>REGISTER FORM</h3>
          <div class="slickwrap">
            <div class="slickreporting">
              <div class="successcontainer"></div>
              <div class="errorcontainer">
                <div class="errorshutter"></div>
                <div class="slickerror"></div>
              </div>
            </div>
            <form method="post" action="register">
              <fieldset>
                <label><span>*</span>User Name</label>
                <input
                  id="name"
                  name="name"
                  class="name"
                  type="text"
                  value=""
                  onblur="isname(this.value)"
                  id="username"
                  required=""
                />
                <br />
                <label><span>*</span>User Type</label>
                <input
                  id="email"
                  name="utype"
                  class="utype"
                  type="text"
                  value=""
                />
                <br />
                <label><span>*</span>Email</label>
                <input
                  id="email"
                  name="email"
                  class="email"
                  type="email"
                  value=""
                  onblur="ismail(this.value)"
                  id="mailid"
                  required=""
                />
                <br />
                <label><span>*</span>Date Of Birth</label>
                <input id="dob" name="dob" type="date" value="" />
                <br />
                <label><span>*</span>Gender</label>
                <select name="gender" class="form-control">
                  <option value="Select" disabled>Select</option>
                  <option value="Male">Male</option>
                  <option value="Female">Female</option>
                </select>
                <br />
                <label><span>*</span>City</label>
                <input
                  id="email"
                  name="city"
                  type="text"
                  value=""
                  onblur="iscity(this.value)"
                  id="textfield5"
                  required=""
                />
                <br />
                <label><span>*</span>Phone</label>
                <input
                  id="phone"
                  name="phone"
                  type="number"
                  value=""
                  maxlength="10"
                  onblur="ismobile(this.value)"
                  id="mobile"
                  required=""
                />
                <br />
                <label><span>*</span>Password</label>
                <input
                  id="email"
                  name="psw"
                  type="password"
                  value=""
                  onblur="ispass(this.value)"
                  id="password1"
                  required=""
                />
                <br />
                <input type="submit" value="Register" />
              </fieldset>
            </form>
          </div>
        </div>
      </div>
    </div>
    <script type="text/javascript">
      var _gaq = _gaq || [];
      _gaq.push(["_setAccount", "UA-15815880-3"]);
      _gaq.push(["_trackPageview"]);
      (function () {
        var ga = document.createElement("script");
        ga.type = "text/javascript";
        ga.async = true;
        ga.src =
          ("https:" == document.location.protocol
            ? "https://ssl"
            : "http://www") + ".google-analytics.com/ga.js";
        var s = document.getElementsByTagName("script")[0];
        s.parentNode.insertBefore(ga, s);
      })();
      function isdob() {
        var date = document.getElementById("dob");
        var pattern = /^([0-3]{1})([0-9]{1})\/([0-1]{1})([0-9]{1})\/([0-9]{4})$/;
        if (!pattern.test(date.value)) {
          document.getElementById("dob").value = "";
          return false;
        } else {
        }
      }
      function isname(name) {
        for (var i = 0; i < name.length; i++) {
          var oneChar = name.substring(i, i + 1);
          if (oneChar < "A" || oneChar > "z") {
            document.getElementById("username").value = "";
            return false;
          } else {
          }
        }
      }
      function ispass(name) {
        var len = name.length;
        if (
          8 > len ||
          len > 10 ||
          name.includes("=") ||
          name.includes(";") ||
          name.includes(",") ||
          name.includes("'") ||
          name.includes(" or ") ||
          name.includes("+")
        ) {
          document.getElementById("password1").value = "";
        }
      }
      function ismail() {
        var email = document.getElementById("mailid");
        var filter = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
        if (!filter.test(email.value)) {
          document.getElementById("mailid").value = "";
          return false;
        }
      }
      function isid1(name) {
        for (var i = 0; i < name.length; i++) {
          var oneChar = name.substring(i, i + 1);
          if (oneChar < "0" || oneChar > "9") {
            document.getElementById("userid1").value = "";
            return false;
          } else {
            if (name.length >= 4 && name.length <= 8) {
            } else {
              document.getElementById("userid1").value = "";
              return false;
            }
          }
        }
      }
      function isid(name) {
        for (var i = 0; i < name.length; i++) {
          var oneChar = name.substring(i, i + 1);
          if (oneChar < "0" || oneChar > "9") {
            document.getElementById("userid").value = "";
            return false;
          } else {
            if (name.length >= 4 && name.length <= 8) {
            } else {
              document.getElementById("userid").value = "";
              return false;
            }
          }
        }
      }
      function ispass1(name) {
        var name1 = document.getElementById("password1").value;
        if (name !== "") {
          if (name !== name1) {
            document.getElementById("password1").value = "";
            document.getElementById("password2").value = "";
          }
        } else {
          document.getElementById("password1").value = "";
          document.getElementById("password2").value = "";
        }
      }
      function iscity(name) {
        for (var i = 0; i < name.length; i++) {
          var oneChar = name.substring(i, i + 1);
          if (oneChar < "A" || oneChar > "z") {
            document.getElementById("textfield5").value = "";
            return false;
          } else {
          }
        }
      }
      function iscountry(name) {
        for (var i = 0; i < name.length; i++) {
          var oneChar = name.substring(i, i + 1);
          if (oneChar < "A" || oneChar > "z") {
            document.getElementById("textfield6").value = "";
            return false;
          } else {
          }
        }
      }
      function ismobile(mno) {
        alert(mno);
        var uid_len = mno.length;
        for (var i = 0; i < mno.length; i++) {
          var oneChar = mno.substring(i, i + 1);
          if (oneChar < "0" || oneChar > "9") {
            document.getElementById("mobile").value = "";
            return false;
          }
          if (uid_len !== 10) {
            document.getElementById("mobile").value = "";
          }
        }
        return true;
      }
      function like(str, str1) {
        var d = 2;
        var xmlhttp;
        if (str == "") {
          document.getElementById("hmint").innerHTML = "";
          return;
        }
        if (window.XMLHttpRequest) {
          xmlhttp = new XMLHttpRequest();
        } else {
          xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
        }
        xmlhttp.onreadystatechange = function () {
          if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            document.getElementById("hmint").innerHTML = xmlhttp.responseText;
          }
        };
        xmlhttp.open("GET", "like.jsp?dit=" + str + "&d=" + str1, true);
        xmlhttp.send();
      }
      function dislike(str, str1) {
        var xmlhttp;
        if (str == "") {
          document.getElementById("hmint").innerHTML = "";
          return;
        }
        if (window.XMLHttpRequest) {
          xmlhttp = new XMLHttpRequest();
        } else {
          xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
        }
        xmlhttp.onreadystatechange = function () {
          if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            document.getElementById("hmint").innerHTML = xmlhttp.responseText;
          }
        };
        xmlhttp.open("GET", "dislike.jsp?dit=" + str + "&d=" + str1, true);
        xmlhttp.send();
      }
      function rate(str, str1, str2) {
        var xmlhttp;
        if (str == "") {
          document.getElementById("hmint").innerHTML = "";
          return;
        }
        if (window.XMLHttpRequest) {
          xmlhttp = new XMLHttpRequest();
        } else {
          xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
        }
        xmlhttp.onreadystatechange = function () {
          if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            document.getElementById("hmint").innerHTML = xmlhttp.responseText;
          }
        };
        xmlhttp.open(
          "GET",
          "rate.jsp?dit=" + str + "&d=" + str1 + "&&str2=" + str2,
          true
        );
        xmlhttp.send();
      }
      function disable() {
        var btn = document.getElementById("lik");
        btn.disabled = true;
        var btn1 = document.getElementById("lik1");
        btn.disabled = true;
        var btn2 = document.getElementById("lik2");
        btn.disabled = true;
        var btn3 = document.getElementById("lik3");
        btn.disabled = true;
        var btn4 = document.getElementById("lik4");
        btn.disabled = true;
      }
      function isfile(id) {
        alert(id);
        var d = 2;
        var xmlhttp;
        if (id == "") {
          document.getElementById("hii").innerHTML = "";
          return;
        }
        if (window.XMLHttpRequest) {
          xmlhttp = new XMLHttpRequest();
        } else {
          xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
        }
        xmlhttp.onreadystatechange = function () {
          if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            document.getElementById("hii").innerHTML = xmlhttp.responseText;
          }
        };
        xmlhttp.open("GET", "product.jsp?fileid=" + id, true);
        xmlhttp.send();
      }
      function loginid(name) {
        var letterNumber = /^[0-9a-zA-Z]+$/;
        if (letterNumber.test(name)) {
        } else {
          document.getElementById("userid").value = "";
        }
      }
      function iskey(name) {
        for (var i = 0; i < name.length; i++) {
          var oneChar = name.substring(i, i + 1);
          if (oneChar < "0" || oneChar > "9") {
            document.getElementById("ekeyy").value = "";
            return false;
          } else {
            if (name.length >= 4 && name.length <= 8) {
            } else {
              document.getElementById("ekeyy").value = "";
              return false;
            }
          }
        }
      }
      function iskey1(name) {
        for (var i = 0; i < name.length; i++) {
          var oneChar = name.substring(i, i + 1);
          if (oneChar < "0" || oneChar > "9") {
            document.getElementById("keyy1").value = "";
            return false;
          } else {
            if (name.length >= 4 && name.length <= 8) {
            } else {
              document.getElementById("keyy1").value = "";
              return false;
            }
          }
        }
      }
      function iskey2(name) {
        for (var i = 0; i < name.length; i++) {
          var oneChar = name.substring(i, i + 1);
          if (oneChar < "0" || oneChar > "9") {
            document.getElementById("keyy2").value = "";
            return false;
          } else {
            if (name.length >= 4 && name.length <= 8) {
            } else {
              document.getElementById("keyy2").value = "";
              return false;
            }
          }
        }
      }
      function isfileid(name) {
        for (var i = 0; i < name.length; i++) {
          var oneChar = name.substring(i, i + 1);
          if (oneChar < "0" || oneChar > "9") {
            document.getElementById("fileid").value = "";
            return false;
          }
        }
      }
      function isbuy() {
        alert("Ordered Successfully");
      }
      function isman(id) {
        alert(id);
        var d = 2;
        var xmlhttp;
        if (id == "") {
          document.getElementById("hii").innerHTML = "";
          return;
        }
        if (window.XMLHttpRequest) {
          xmlhttp = new XMLHttpRequest();
        } else {
          xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
        }
        xmlhttp.onreadystatechange = function () {
          if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            document.getElementById("hii").innerHTML = xmlhttp.responseText;
          }
        };
        xmlhttp.open("GET", "productman.jsp?fileid=" + id, true);
        xmlhttp.send();
      }
      function myFunction() {
        var date = document.getElementById("gid").value;
        alert(date);
        var d = 2;
        var xmlhttp;
        if (date == "") {
          document.getElementById("gym1").innerHTML = "";
          return;
        }
        if (window.XMLHttpRequest) {
          xmlhttp = new XMLHttpRequest();
        } else {
          xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
        }
        xmlhttp.onreadystatechange = function () {
          if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            document.getElementById("gym1").innerHTML = xmlhttp.responseText;
          }
        };
        xmlhttp.open("GET", "diesislist.jsp?fileid=" + date, true);
        xmlhttp.send();
      }
    </script>
  </body>
</html>
