<template>
  <form @submit="register" id="register">
    <label><span>*</span>User Name</label>
    <input v-model="body.user_name" class="box1 border1"/>
    <!-- <p v-if="body.user_name.length<3">{{ username.error.message }}</p> -->
    <br />
    <label><span>*</span>User Type</label>
    <Select v-model="body.user_type" class="form-control">
      <Option value="Select" disabled>Select</Option>
      <Option value="0">Patient</Option>
      <Option value="1">Doctor</Option>
      <Option value="2">Admin</Option>
    </Select>
    <br />
    <label><span>*</span>Email</label>
    <input v-model="body.user_email" />
    <br />
    <label><span>*</span>Date Of Birth</label>
    <datepicker v-model="body.date_of_birth" name="datepicker"></datepicker>
    <br />
    <label><span>*</span>Gender</label>
    <Select v-model="body.gender" class="form-control">
      <Option value="Select" disabled>Select</Option>
      <Option value="1">Male</Option>
      <Option value="2">Female</Option>
      <Option value="0">Trans-Gender</Option>
    </Select>
    <br />
    <label><span>*</span>Country</label>
    <Select v-model="body.country" class="form-control">
      <Option value="select" disabled>Select</Option>
      <Option value="AX">Åland Islands</Option>
      <Option value="DZ">Algeria</Option>
      <Option value="AS">American Samoa</Option>
      <Option value="AD">Andorra</Option>
      <Option value="AR">Argentina</Option>
      <Option value="AT">Austria</Option>
      <Option value="AU">Australia</Option>
      <Option value="BD">Bangladesh</Option>
      <Option value="BY">Belarus</Option>
      <Option value="BE">Belgium</Option>
      <Option value="BM">Bermuda</Option>
      <Option value="BG">Bulgaria</Option>
      <Option value="BR">Brazil</Option>
      <Option value="CA">Canada</Option>
      <Option value="CO">Colombia</Option>
      <Option value="CR">Costa Rica</Option>
      <Option value="HR">Croatia</Option>
      <Option value="CZ">Czechia</Option>
      <Option value="DK">Denmark</Option>
      <Option value="DO">Dominican Republic</Option>
      <Option value="FO">Faroe Islands</Option>
      <Option value="FI">Finland</Option>
      <Option value="FR">France</Option>
      <Option value="GF">French Guiana</Option>
      <Option value="DE">Germany</Option>
      <Option value="GG">Guernsey</Option>
      <Option value="GL">Greenland</Option>
      <Option value="GP">Guadeloupe</Option>
      <Option value="GU">Guam</Option>
      <Option value="GT">Guatemala</Option>
      <Option value="VA">Holy See</Option>
      <Option value="HU">Hungary</Option>
      <Option value="IS">Iceland</Option>
      <Option value="IN">India</Option>
      <Option value="IE">Ireland</Option>
      <Option value="IM">Isle of Man</Option>
      <Option value="IT">Italy</Option>
      <Option value="JP">Japan</Option>
      <Option value="JE">Jersey</Option>
      <Option value="LV">Latvia</Option>
      <Option value="LI">Liechtenstein</Option>
      <Option value="LT">Lithuania</Option>
      <Option value="LU">Luxembourg</Option>
      <Option value="MY">Malaysia</Option>
      <Option value="MT">Malta</Option>
      <Option value="MH">Marshall Islands</Option>
      <Option value="MQ">Martinique</Option>
      <Option value="YT">Mayotte</Option>
      <Option value="MX">Mexico</Option>
      <Option value="MC">Monaco</Option>
      <Option value="NL">Netherlands</Option>
      <Option value="NC">New Caledonia</Option>
      <Option value="NZ">New Zealand</Option>
      <Option value="NO">Norway</Option>
      <Option value="MP">Northern Mariana Islands</Option>
      <Option value="PK">Pakistan</Option>
      <Option value="PH">Philippines</Option>
      <Option value="PL">Poland</Option>
      <Option value="PT">Portugal</Option>
      <Option value="PR">Puerto Rico</Option>
      <Option value="MD">Republic of Moldova</Option>
      <Option value="RE">Réunion</Option>
      <Option value="RO">Romania</Option>
      <Option value="RU">Russian Federation</Option>
      <Option value="SM">San Marino</Option>
      <Option value="SK">Slovakia</Option>
      <Option value="SI">Slovenia</Option>
      <Option value="ZA">South Africa</Option>
      <Option value="ES">Spain</Option>
      <Option value="LK">Sri Lanka</Option>
      <Option value="SJ">Svalbard and Jan Mayen Islands</Option>
      <Option value="SE">Sweden</Option>
      <Option value="TH">Thailand</Option>
      <Option value="MK">The former Yugoslav Republic of Macedonia</Option>
      <Option value="TR">Turkey</Option>
      <Option value="UA">Ukraine</Option>
      <Option value="GB">United Kingdom of Great Britain and Northern Ireland</Option>
      <Option value="US">United States of America</Option>
      <Option value="VI">United States Virgin Islands</Option>
      <Option value="UY">Uruguay</Option>
      <Option value="WF">Wallis and Futuna Islands</Option>
      <!-- <Option value=""></Option>
      <Option value=""></Option>
      <Option value=""></Option>
      <Option value=""></Option>
      <Option value=""></Option>
      <Option value=""></Option>
      <Option value=""></Option> -->
    </Select>
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
