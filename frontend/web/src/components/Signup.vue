<template>
  <div class="grid">
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
          <form @submit="onSignUp">
            <label><span>*</span>User Name</label>
            <input
              v-model="username.value"
              :ref="username.ref"
              class="box1 border1"
            />
            <p v-if="username.error">{{ username.error.message }}</p>
            <br />
            <label><span>*</span>User Type</label>
            <select v-model="usertype" class="form-control" multiple>
              <option value="Select" disabled>Select</option>
              <option value="0">Patient</option>
              <option value="1">Doctor</option>
              <option value="2">Scientist</option>
            </select>
            <br />
            <label><span>*</span>Email</label>
            <input v-model="useremail.value" :ref="useremail.ref" />
            <br />
            <label><span>*</span>Date Of Birth</label>
            <datepicker :value="state.date" name="dob"></datepicker>
            <br />
            <label><span>*</span>Gender</label>
            <select v-model="gender" class="form-control" multiple>
              <option value="Select" disabled>Select</option>
              <option value="1">Male</option>
              <option value="2">Female</option>
              <option value="0">Trans-Gender</option>
            </select>
            <br />
            <label><span>*</span>Pincode</label>
            <input v-model="pincode.value" :ref="pincode.ref" />
            <br />
            <label><span>*</span>Mobile Number</label>
            <input v-model="phone.value" />
            <br />
            <label><span>*</span>Password</label>
            <input
              v-model="password"
              :ref="password.ref"
              type="password"
              class="box1 border2"
            />
            <p v-if="password.error">{{ password.error.message }}</p>
            <br />
            <button type="submit">Submit</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>
    <style src="{{ url_for('static',filename='css/slickform.css') }}"></style>
<style src="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.5.1/animate.min.css"></style>
    <style src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.5.0/css/font-awesome.min.css"></style>
    <style src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome-animation/0.0.8/font-awesome-animation.min.css"></style>
<script src="https://cdnjs.cloudflare.com/ajax/libs/modernizr/2.8.3/modernizr.min.js"></script>
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <script src="{{ url_for('static',filename='js/jquery.matchHeight-min.js') }}"></script>
    <script src="{{ url_for('static',filename='js/wow.min.js') }}"></script>
    <script src="{{ url_for('static',filename='js/animsition.min.js') }}"></script>
    <script src="{{ url_for('static',filename='js/Slickform.js') }}"></script>
    <script src="{{ url_for('static',filename='js/functions.js') }}"></script>
    <script src="{{ url_for('static',filename='js/val.js') }}"></script>
    <script src="{{ url_for('static',filename='js/vue.js') }}"></script>
<script>
import { useForm } from "vue-hooks-form";

export default {
  setup() {
    const { useField, handleSubmit } = useForm({
      defaultValues: {},
    });
    const username = useField("username", {
      rule: { required: true },
    });
    const password = useField("password", {
      rule: {
        required: true,
        min: 6,
        max: 10,
      },
    });
    const onSignUp = (data) => console.log(data);
    return {
      username,
      password,
      onSignUp: handleSubmit(onSignUp),
    };
  },
};
</script>
