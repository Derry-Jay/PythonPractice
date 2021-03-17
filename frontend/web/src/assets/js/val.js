import { VueLink } from 'vue-link'
import { VueRouter } from 'vue-router'
const router = new VueRouter({
  routes: [{ path: '/welcome', component: 'Welcome' }, { path: '/login', component: 'Login'}, { path: '/signup' }]
})
const linker = new VueLink({
  link: [
    { rel: 'apple-touch-icon', sizes: '57x57' },
    { rel: 'apple-touch-icon', sizes: '60x60' }
  ]
})
const meta = new VueMeta()
export default {
  name: 'welcome',
  metaInfo: {
    title: 'Welcome',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1.0' },
      { property: 'og:url', content: 'http://www.valeron.net/index.html' },
      { property: 'og:type', content: 'website' },
      { property: 'og:title', content: 'Free responsive web template Istria' },
      {
        property: 'og:description',
        content:
          'Free responsive web template Istria 1 by Valeron design studio'
      },
      {
        property: 'og:image',
        content: 'http://www.valeron.net/img/valeron-artist.jpg'
      },
      {
        name: 'description',
        content:
          'Free responsive web template Istria 1 by Valeron design studio'
      },
      { name: 'msapplication-tap-highlight', content: 'no' },
      { name: 'robots', content: 'index,follow,all' },
      { name: 'keywords', content: 'Izrada web stranica, web studio Istra' },
      { name: 'author', content: 'Valeron design studio' },
      { name: 'msapplication-TileColor', content: '#da532c' },
      { name: 'msapplication-TileImage', content: 'img/mstile-144x144.png' },
      { name: 'theme-color', content: '#ffffff' }
    ]
  }
}
const router = new VueRouter({
  routes: [{ path: '/welcome' }, { path: '/login' }, { path: '/signup' }]
})
$('.enticlick').click(function () {
  window.location = $(this).find('a').attr('href')
  return false
})
$(document).ready(function () {
  $('#owl-partners').owlCarousel({
    autoPlay: 4000,
    stopOnHover: true,
    pagination: false,
    items: 5,
    itemsDesktop: [1199, 4],
    itemsDesktopSmall: [959, 3]
  })
})
$(function () {
  $('#cbp-qtrotator').cbpQTRotator()
})
$('.enticlick').click(function () {
  window.location = $(this).find('a').attr('href')
  return false
})
$(document).ready(function () {
  $('#lightgallery').lightGallery()
})
$('#lightgallery2').lightGallery({
  thumbnail: true,
  animateThumb: false,
  showThumbByDefault: false,
  speed: 1200
})
$('#gallery-99').lightGallery({
  thumbnail: true,
  animateThumb: false,
  showThumbByDefault: false,
  speed: 1200
})
var _gaq = _gaq || []
_gaq.push(['_setAccount', 'UA-15815880-3'])
_gaq.push(['_trackPageview']);
(function () {
  var ga = document.createElement('script')
  ga.type = 'text/javascript'
  ga.async = true
  ga.src =
    (document.location.protocol == 'https:' ? 'https://ssl' : 'http://www') +
    '.google-analytics.com/ga.js'
  var s = document.getElementsByTagName('script')[0]
  s.parentNode.insertBefore(ga, s)
})()
function isdob () {
  //    alert("jhgjhgjhg");
  var date = document.getElementById('dob')
  var pattern = /^([0-3]{1})([0-9]{1})\/([0-1]{1})([0-9]{1})\/([0-9]{4})$/
  if (!pattern.test(date.value)) {
    document.getElementById('dob').value = ''
    return false
  } else {

  }
}

function isname (name) {
  for (var i = 0; i < name.length; i++) {
    var oneChar = name.substring(i, i + 1)
    if (oneChar < 'A' || oneChar > 'z') {
      document.getElementById('username').value = ''
      return false
    } else {
      // document.getElementById("textfield1").value = "hidden";
    }
  }
}

function ispass (name) {
  var len = name.length
  //                  var patt = new RegExp("=;");
  /// /   var res = patt.test(str);
  if (len < 8 || len > 10 || name.includes('=') || name.includes(';') || name.includes(',') || name.includes("'") || name.includes(' or ') || name.includes('+')) {
    document.getElementById('password1').value = ''
  }
}

function ismail () {
  var email = document.getElementById('mailid')
  var filter = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/

  if (!filter.test(email.value)) {
    document.getElementById('mailid').value = ''
    return false
  }
}
function isid1 (name) {
  //     alert(name);
  for (var i = 0; i < name.length; i++) {
    var oneChar = name.substring(i, i + 1)
    if (oneChar < '0' || oneChar > '9') {
      // document.getElementById("userid1").style.visibility = "visible";
      document.getElementById('userid1').value = ''
      return false
    } else {
      if (name.length >= 4 && name.length <= 8) {
        // document.getElementById("userid1").style.visibility = "hidden";
      } else {
        // document.getElementById("userid1").style.visibility = "visible";
        document.getElementById('userid1').value = ''
        return false
      }
    }
  }
}
function isid (name) {
  //     alert(name);
  for (var i = 0; i < name.length; i++) {
    var oneChar = name.substring(i, i + 1)
    if (oneChar < '0' || oneChar > '9') {
      // document.getElementById("userid1").style.visibility = "visible";
      document.getElementById('userid').value = ''
      return false
    } else {
      if (name.length >= 4 && name.length <= 8) {
        // document.getElementById("userid1").style.visibility = "hidden";
      } else {
        // document.getElementById("userid1").style.visibility = "visible";
        document.getElementById('userid').value = ''
        return false
      }
    }
  }
}

function ispass1 (name) {
  var name1 = document.getElementById('password1').value
  if (name !== '') {
    if (name !== name1) {
      document.getElementById('password1').value = ''
      document.getElementById('password2').value = ''
    }
  } else {
    document.getElementById('password1').value = ''
    document.getElementById('password2').value = ''
  }
}

function iscity (name) {
  for (var i = 0; i < name.length; i++) {
    var oneChar = name.substring(i, i + 1)
    if (oneChar < 'A' || oneChar > 'z') {
      document.getElementById('textfield5').value = ''
      return false
    } else {
      // document.getElementById("textfield1").value = "hidden";
    }
  }
}

function iscountry (name) {
  for (var i = 0; i < name.length; i++) {
    var oneChar = name.substring(i, i + 1)
    if (oneChar < 'A' || oneChar > 'z') {
      document.getElementById('textfield6').value = ''
      return false
    } else {
      // document.getElementById("textfield1").value = "hidden";
    }
  }
}

function ismobile (mno) {
  alert(mno)
  var uid_len = mno.length
  for (var i = 0; i < mno.length; i++) {
    var oneChar = mno.substring(i, i + 1)
    if (oneChar < '0' || oneChar > '9') {
      // document.getElementById("mobile").style.visibility = "visible";
      document.getElementById('mobile').value = ''
      return false
    }
    if (uid_len !== 10) {
      document.getElementById('mobile').value = ''
    }
  }
  return true
}

function like (str, str1) {
  var d = 2
  var xmlhttp
  if (str == '') {
    document.getElementById('hmint').innerHTML = ''
    return
  }
  if (window.XMLHttpRequest) { // code for IE7+, Firefox, Chrome, Opera, Safari
    xmlhttp = new XMLHttpRequest()
  } else { // code for IE6, IE5
    xmlhttp = new ActiveXObject('Microsoft.XMLHTTP')
  }
  xmlhttp.onreadystatechange = function () {
    if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
      document.getElementById('hmint').innerHTML = xmlhttp.responseText
    }
  }

  xmlhttp.open('GET', 'like.jsp?dit=' + str + '&d=' + str1, true)
  xmlhttp.send()
}

function dislike (str, str1) {
  var xmlhttp
  if (str == '') {
    document.getElementById('hmint').innerHTML = ''
    return
  }
  if (window.XMLHttpRequest) { // code for IE7+, Firefox, Chrome, Opera, Safari
    xmlhttp = new XMLHttpRequest()
  } else { // code for IE6, IE5
    xmlhttp = new ActiveXObject('Microsoft.XMLHTTP')
  }
  xmlhttp.onreadystatechange = function () {
    if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
      document.getElementById('hmint').innerHTML = xmlhttp.responseText
    }
  }

  xmlhttp.open('GET', 'dislike.jsp?dit=' + str + '&d=' + str1, true)
  xmlhttp.send()
}

function rate (str, str1, str2) {
  var xmlhttp
  if (str == '') {
    document.getElementById('hmint').innerHTML = ''
    return
  }
  if (window.XMLHttpRequest) { // code for IE7+, Firefox, Chrome, Opera, Safari
    xmlhttp = new XMLHttpRequest()
  } else { // code for IE6, IE5
    xmlhttp = new ActiveXObject('Microsoft.XMLHTTP')
  }
  xmlhttp.onreadystatechange = function () {
    if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
      document.getElementById('hmint').innerHTML = xmlhttp.responseText
    }
  }

  xmlhttp.open('GET', 'rate.jsp?dit=' + str + '&d=' + str1 + '&&str2=' + str2, true)
  xmlhttp.send()
}

function disable () {
  var btn = document.getElementById('lik')
  btn.disabled = true
  var btn1 = document.getElementById('lik1')
  btn.disabled = true
  var btn2 = document.getElementById('lik2')
  btn.disabled = true
  var btn3 = document.getElementById('lik3')
  btn.disabled = true
  var btn4 = document.getElementById('lik4')
  btn.disabled = true
}

function isfile (id) {
  alert(id)
  var d = 2
  var xmlhttp
  if (id == '') {
    document.getElementById('hii').innerHTML = ''
    return
  }
  if (window.XMLHttpRequest) { // code for IE7+, Firefox, Chrome, Opera, Safari
    xmlhttp = new XMLHttpRequest()
  } else { // code for IE6, IE5
    xmlhttp = new ActiveXObject('Microsoft.XMLHTTP')
  }
  xmlhttp.onreadystatechange = function () {
    if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
      document.getElementById('hii').innerHTML = xmlhttp.responseText
    }
  }

  xmlhttp.open('GET', 'product.jsp?fileid=' + id, true)
  xmlhttp.send()
}

function loginid (name) {
  //                  var patt = new RegExp("=;");
  /// /   var res = patt.test(str);
  //      alert(name);
  var letterNumber = /^[0-9a-zA-Z]+$/
  if ((letterNumber.test(name))) {

  } else {
    document.getElementById('userid').value = ''
  }
}

function iskey (name) {
  //       alert(name);
  for (var i = 0; i < name.length; i++) {
    var oneChar = name.substring(i, i + 1)
    if (oneChar < '0' || oneChar > '9') {
      //                            alert(name);
      // document.getElementById("userid1").style.visibility = "visible";
      document.getElementById('ekeyy').value = ''
      return false
    } else {
      if (name.length >= 4 && name.length <= 8) {
        // document.getElementById("userid1").style.visibility = "hidden";
      } else {
        // document.getElementById("userid1").style.visibility = "visible";
        document.getElementById('ekeyy').value = ''
        return false
      }
    }
  }
}

function iskey1 (name) {
  for (var i = 0; i < name.length; i++) {
    var oneChar = name.substring(i, i + 1)
    if (oneChar < '0' || oneChar > '9') {
      // document.getElementById("userid1").style.visibility = "visible";
      document.getElementById('keyy1').value = ''
      return false
    } else {
      if (name.length >= 4 && name.length <= 8) {
        // document.getElementById("userid1").style.visibility = "hidden";
      } else {
        // document.getElementById("userid1").style.visibility = "visible";
        document.getElementById('keyy1').value = ''
        return false
      }
    }
  }
}

function iskey2 (name) {
  for (var i = 0; i < name.length; i++) {
    var oneChar = name.substring(i, i + 1)
    if (oneChar < '0' || oneChar > '9') {
      // document.getElementById("userid1").style.visibility = "visible";
      document.getElementById('keyy2').value = ''
      return false
    } else {
      if (name.length >= 4 && name.length <= 8) {
        // document.getElementById("userid1").style.visibility = "hidden";
      } else {
        // document.getElementById("userid1").style.visibility = "visible";
        document.getElementById('keyy2').value = ''
        return false
      }
    }
  }
}

function isfileid (name) {
  for (var i = 0; i < name.length; i++) {
    var oneChar = name.substring(i, i + 1)
    if (oneChar < '0' || oneChar > '9') {
      // document.getElementById("userid1").style.visibility = "visible";
      document.getElementById('fileid').value = ''
      return false
    }
  }
}

function isbuy () {
  alert('Ordered Successfully')
}

function isman (id) {
  alert(id)
  var d = 2
  var xmlhttp
  if (id == '') {
    document.getElementById('hii').innerHTML = ''
    return
  }
  if (window.XMLHttpRequest) { // code for IE7+, Firefox, Chrome, Opera, Safari
    xmlhttp = new XMLHttpRequest()
  } else { // code for IE6, IE5
    xmlhttp = new ActiveXObject('Microsoft.XMLHTTP')
  }
  xmlhttp.onreadystatechange = function () {
    if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
      document.getElementById('hii').innerHTML = xmlhttp.responseText
    }
  }

  xmlhttp.open('GET', 'productman.jsp?fileid=' + id, true)
  xmlhttp.send()
}

function myFunction () {
  var date = document.getElementById('gid').value
  alert(date)
  var d = 2
  var xmlhttp
  if (date == '') {
    document.getElementById('gym1').innerHTML = ''
    return
  }
  if (window.XMLHttpRequest) { // code for IE7+, Firefox, Chrome, Opera, Safari
    xmlhttp = new XMLHttpRequest()
  } else { // code for IE6, IE5
    xmlhttp = new ActiveXObject('Microsoft.XMLHTTP')
  }
  xmlhttp.onreadystatechange = function () {
    if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
      document.getElementById('gym1').innerHTML = xmlhttp.responseText
    }
  }
  xmlhttp.open('GET', 'diesislist.jsp?fileid=' + date, true)
  xmlhttp.send()
}
