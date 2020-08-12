<script type="text/module">
import { VueMeta } from "vue-meta";
import { VueRouter } from "vue-router";
import { Vue } from "vue";
import { VueLink } from "vue-link";
export default {
    name: "welcome",
    metaInfo: {
        title: "Welcome",
        meta: [
            { charset: "utf-8" },
            { name: "viewport", content: "width=device-width, initial-scale=1.0" },
            { property: "og:url", content: "http://www.valeron.net/index.html" },
            { property: "og:type", content: "website" },
            { property: "og:title", content: "Free responsive web template Istria" },
            {
                property: "og:description",
                content:
                    "Free responsive web template Istria 1 by Valeron design studio",
            },
            {
                property: "og:image",
                content: "http://www.valeron.net/img/valeron-artist.jpg",
            },
            {
                name: "description",
                content:
                    "Free responsive web template Istria 1 by Valeron design studio",
            },
            { name: "msapplication-tap-highlight", content: "no" },
            { name: "robots", content: "index,follow,all" },
            { name: "keywords", content: "Izrada web stranica, web studio Istra" },
            { name: "author", content: "Valeron design studio" },
            { name: "msapplication-TileColor", content: "#da532c" },
            { name: "msapplication-TileImage", content: "img/mstile-144x144.png" },
            { name: "theme-color", content: "#ffffff" },
        ],
    },
};
const router = new VueRouter({
    routes: [{ path: "/welcome" }, { path: "/login" }, { path: "/signup" }],
});
$(document).ready(function () {
  $("#owl-partners").owlCarousel({
    autoPlay: 4000,
    stopOnHover: true,
    pagination: false,
    items: 5,
    itemsDesktop: [1199, 4],
    itemsDesktopSmall: [959, 3],
  });
});
$(function () {
  $("#cbp-qtrotator").cbpQTRotator();
});
var _gaq = _gaq || [];
_gaq.push(["_setAccount", "UA-15815880-3"]);
_gaq.push(["_trackPageview"]);
(function () {
  var ga = document.createElement("script");
  ga.type = "text/javascript";
  ga.async = true;
  ga.src =
    ("https:" == document.location.protocol ? "https://ssl" : "http://www") +
    ".google-analytics.com/ga.js";
  var s = document.getElementsByTagName("script")[0];
  s.parentNode.insertBefore(ga, s);
})();
</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/modernizr/2.8.3/modernizr.min.js"></script>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
<script src="http://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.3/jquery.easing.min.js"></script>
<script src="{{ url_for('static',filename='js/jquery.matchHeight-min.js') }}"></script>
<script src="{{ url_for('static',filename='js/wow.min.js') }}"></script>
<script src="{{ url_for('static',filename='js/import.js') }}"></script>
<script src="{{ url_for('static',filename='js/jquery.parallax-scroll.js') }}"></script>
<script src="{{ url_for('static',filename='js/owl.carousel.min.js') }}"></script>
<script src="{{ url_for('static',filename='js/jquery.cbpQTRotator.min.js') }}"></script>
<script src="{{ url_for('static',filename='js/functions.js') }}"></script>
<script src="{{ url_for('static',filename='js/particle.js') }}"></script>
<script src="{{ url_for('static',filename='js/vue.js') }}"></script>
<style src="{{ url_for('static',filename='css/grid.min.css') }}"></style>
<style src="{{ url_for('static',filename='css/style.css') }}"></style>
<style src="{{ url_for('static',filename='css/menu.css') }}"></style>
<style src="{{ url_for('static',filename='css/overlay.css') }}"></style>
<style src="{{ url_for('static',filename='css/owl.carousel.css') }}"></style>
<style src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.5.0/css/font-awesome.min.css"></style>
<style src="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.5.1/animate.min.css"></style>
<!-- 
<html lang="en">
<head>9www.123musiq.com -  ® Riya collections ®12 - www.123musiq.com -  ® Riya collections ® - www.123musiq.com -  ® Riya collections ® - www.123musiq.com -  ® Riya collections ®; www.123musiq.com -  ® Riya collections ®13
<title>Ontology</title>
<meta ="" ="" />
<meta ="" ="" />
<meta ="" ="" />
<meta ="" ="" />
<meta ="" ="" />
<meta ="" ="" />
<meta ="" ="" />
<link rel="stylesheet" href="">
<link rel="stylesheet" type="text/css" href="" />
<link rel="stylesheet" type="text/css" href="" />
<link rel="stylesheet" type="text/css" href="" />
<link rel="stylesheet" type="text/css" href="" />
<link rel="stylesheet" type="text/css" href="">
<link rel="stylesheet" href="">
<link rel="stylesheet" href="">
</head>
<body>
<a href="http://localhost:5000"></a>
<a href="http://localhost:5000"></a>
<a href="http://localhost:5000"></a>
<a href="http://localhost:5000"></a>
</body>
</html>
<link ="" ="" href="{{ url_for('static',filename='img/apple-touch-icon-57x57.png') }}">
<link ="" ="" href="{{ url_for('static',filename='img/apple-touch-icon-60x60.png') }}">
<link rel="apple-touch-icon" sizes="72x72" href="{{ url_for('static',filename='img/apple-touch-icon-72x72.png') }}">
<link rel="apple-touch-icon" sizes="76x76" href="{{ url_for('static',filename='img/apple-touch-icon-76x76.png') }}">
<link rel="apple-touch-icon" sizes="114x114" href="{{ url_for('static',filename='img/apple-touch-icon-114x114.png') }}">
<link rel="apple-touch-icon" sizes="120x120" href="{{ url_for('static',filename='img/apple-touch-icon-120x120.png') }}">
<link rel="apple-touch-icon" sizes="144x144" href="{{ url_for('static',filename='img/apple-touch-icon-144x144.png') }}">
<link rel="apple-touch-icon" sizes="152x152" href="{{ url_for('static',filename='img/apple-touch-icon-152x152.png') }}">
<link rel="apple-touch-icon" sizes="180x180" href="{{ url_for('static',filename='img/apple-touch-icon-180x180.png') }}">
<link rel="icon" type="image/png" href="{{ url_for('static',filename='img/favicon-32x32.png') }}" sizes="32x32">
<link rel="icon" type="image/png" href="{{ url_for('static',filename='img/android-chrome-192x192.png') }}" sizes="192x192">
<link rel="icon" type="image/png" href="{{ url_for('static',filename='img/favicon-96x96.png') }}" sizes="96x96">
<link rel="icon" type="image/png" href="{{ url_for('static',filename='img/favicon-16x16.png') }}" sizes="16x16">
<style src="{{ url_for('static',filename='css/animsition.min.css') }}"></style>
<link rel="manifest" href="{{ url_for('static',filename='img/manifest.json') }}"> -->
<template>
  <div class="animsition-overlay">
    <p>Hi</p>
    <icon name></icon>
    <div id="section-1">
      <header class="main_h">
        <div class="menufix">
          <router-link to="/welcome" class="logo">
            <img src="{{ url_for('static',filename='images/logo.jpg') }}" alt="Hello" />
          </router-link>
          <div class="mobile-toggle">
            <span></span>
            <span></span>
            <span></span>
          </div>
          <nav>
            <ul>
              <li>
                <router-link to="/welcome" class="out active animsition-link">HOME</router-link>
              </li>
              <li class="line">
                <router-link to="/login" class="out animsition-link">SIGNIN</router-link>
              </li>
              <li class="line">
                <router-link to="/signup" class="out animsition-link">SIGNUP</router-link>
              </li>
            </ul>
          </nav>
        </div>
      </header>
      <div class="hero">
        <h1 id="title-1">
          GENE
          <em>
            <span>M</span>iRNA
          </em>
        </h1>
        <div class="fixbottarro">
          <a class="scroll" href="#section-2">Scroll for more</a>
        </div>
      </div>
    </div>
    <div class="colw_6 paddbott100 spec-r">
      <p class="dolje" id="section-2"></p>
    </div>
  </div>
</template>
