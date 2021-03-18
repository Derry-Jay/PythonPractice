<template>
  <div class="animsition-overlay">
    <div id="section-1">
      <header class="main_h">
        <div class="menufix">
          <a class="logo" href="index.html"
            ><img src="images/logo.png" alt="Hello"
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
                <a class="out active animsition-link" href="login.jsp"
                  >SIGNIN</a
                >
              </li>
              <li class="line">
                <a class="out animsition-link" href="signup.html">SIGNUP</a>
              </li>
            </ul>
          </nav>
        </div>
      </header>
      <div class="hero">
        <div class="main-wrap" style="height: -10px">
          <form @submit="onLogin">
            <div class="login-main">
              <input
                :ref="useremail.ref"
                v-model="useremail.value"
                class="box1 border1"
              />
              <input
                v-model="password"
                :ref="password.ref"
                type="password"
                class="box1 border2"
              />
              <button type="submit">Submit</button>
            </div>
          </form>
        </div>
      </div>
      <div class="fixbottarro">
        <a class="scroll" href="#section-2">Scroll for more</a>
      </div>
    </div>
    <div class="colw_6 paddbott100 spec-r"></div>
  </div>
</template>
<script type="text/javascript">
export default{
  mounted () {
    let script1 = document.createElement('script')
    let script2 = document.createElement('script')
    let script3 = document.createElement('script')
    script1.setAttribute('src', 'https://cdnjs.cloudflare.com/ajax/libs/modernizr/2.8.3/modernizr.min.js')
    script2.setAttribute('src', 'http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js')
    script3.setAttribute('src', 'http://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.3/jquery.easing.min.js')
  }
}
</script>
<style lang="css or less">
@import "../assets/css/menu.css";
@import "../assets/css/style.css";
@import "../assets/css/overlay.css";
@import "../assets/css/grid.min.css";
@import "../assets/css/owl.carousel.css";
@import "../assets/css/lightgallery.min.css";
@import "https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.5.1/animate.min.css";
@import "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.5.0/css/font-awesome.min.css";
</style>
