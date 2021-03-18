<template>
  <form @submit="login" id="login" method="post">
    <input
        v-model="body.user_email"
        class="box1 border1"
        type="email"
      />
    <input
        v-model="body.password"
        type="password"
        class="box1 border2"
      />
    <button type="submit">Submit</button>
  </form>
</template>
<script type="text/javascript">
export default {
  el: '#login',
  // mounted() {
  //   let script1 = document.createElement("script");
  //   let script2 = document.createElement("script");
  //   let script3 = document.createElement("script");
  //   script1.setAttribute(
  //     "src",
  //     "https://cdnjs.cloudflare.com/ajax/libs/modernizr/2.8.3/modernizr.min.js"
  //   );
  //   script2.setAttribute(
  //     "src",
  //     "http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"
  //   );
  //   script3.setAttribute(
  //     "src",
  //     "http://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.3/jquery.easing.min.js"
  //   );
  //   document.head.appendChild(script1);
  //   document.head.appendChild(script2);
  //   document.head.appendChild(script3);
  // },
  methods: {
    async login () {
      console.log(this.body)
      const request = new Request('http://localhost:8000/login', {
        method: 'POST',
        mode: 'cors',
        cache: 'default',
        body: JSON.stringify(this.body)
      })
      const res = await fetch(request)
      const data = await res.json()
      this.data = data
      console.log(this.data)
    }
  },
  data () {
    return {
      body: {},
      data: {}
    }
  }
}
</script>
<style scoped>
#login{
  background-color: blue;
}
</style>
<!--<style scoped src="../assets/css/menu.css"></style>
<style scoped src="../assets/css/style.css"></style>
<style scoped src="../assets/css/overlay.css"></style>
<style scoped src="../assets/css/grid.min.css"></style>
<style scoped src="../assets/css/owl.carousel.css"></style>
<style scoped src="../assets/css/lightgallery.min.css"></style>
<style scoped src="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.5.1/animate.min.css"></style>
<style scoped src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.5.0/css/font-awesome.min.css"></style> -->
