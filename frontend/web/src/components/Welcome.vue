<template>
  <div class="animsition-overlay">
    <icon name></icon>
    <div id="section-1">
      <header class="main_h">
        <div class="menufix">
          <router-link v-bind:to="'/welcome'" class="logo">
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
                <router-link v-bind:to="'/welcome'" class="out active animsition-link">HOME</router-link>
              </li>
              <li class="line">
                <router-link v-bind:to="'/login'" class="out animsition-link">SIGNIN</router-link>
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
