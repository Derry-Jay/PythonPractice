<template>
  <form @submit="register" id="register">
    <label><span>*</span>User Name</label>
    <input v-model="body.user_name" class="box1 border1"/>
    <!-- <p v-if="body.user_name.length<3">{{ username.error.message }}</p> -->
    <br />
    <label><span>*</span>User Type</label>
    <select v-model="body.user_type" class="form-control">
      <option value="Select" disabled>Select</option>
      <option value="0">Patient</option>
      <option value="1">Doctor</option>
      <option value="2">Scientist</option>
    </select>
    <br />
    <label><span>*</span>Email</label>
    <input v-model="body.user_email" />
    <br />
    <label><span>*</span>Date Of Birth</label>
    <datepicker v-model="body.date_of_birth" name="datepicker"></datepicker>
    <br />
    <label><span>*</span>Gender</label>
    <select v-model="body.gender" class="form-control">
      <option value="Select" disabled>Select</option>
      <option value="1">Male</option>
      <option value="2">Female</option>
      <option value="0">Trans-Gender</option>
    </select>
    <br />
    <label><span>*</span>Pincode</label>
    <input v-model="body.pincode" />
    <br />
    <label><span>*</span>Mobile Number</label>
    <input v-model="body.mobile_number" />
    <br />
    <label><span>*</span>Password</label>
    <input v-model="body.password" type="password" class="box1 border2"/>
    <!-- <p v-if="password.error">{{ password.error.message }}</p> -->
    <br />
    <button type="submit">Submit</button>
  </form>
</template>
<script>
import Datepicker from 'vuejs-datepicker'
import router from '../router'
export default {
  components: {
    Datepicker
  },
  data () {
    return {
      body: {},
      data: {}
    }
  },
  mounted () {
    let script1 = document.createElement('script')
    let script2 = document.createElement('script')
    let script3 = document.createElement('script')
    script1.setAttribute(
      'src',
      'https://cdnjs.cloudflare.com/ajax/libs/modernizr/2.8.3/modernizr.min.js'
    )
    script2.setAttribute(
      'src',
      'http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js'
    )
    script3.setAttribute(
      'src',
      'http://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.3/jquery.easing.min.js'
    )
    document.head.appendChild(script1)
    document.head.appendChild(script2)
    document.head.appendChild(script3)
  },
  methods: {
    async register () {
      console.log(this.body)
      const request = new Request('http://localhost:8000/register', {
        method: 'POST',
        mode: 'cors',
        cache: 'default',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.body)
      })
      const res = await fetch(request)
      if (res.ok) {
        const data = await res.json()
        this.data = data
        console.log(this.data)
        if (this.data.success && this.data.status && this.data.user_id != null) {
          const passData = {'name': 'Login'}
          router.push(passData)
        } else {
          console.log('hi')
        }
      } else {
        console.log('hi')
      }
    }
  }
}
</script>
