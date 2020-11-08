<template>
  <v-app>
    <v-container>
      <v-row justify="center">
        <v-col cols="10" md="8" lg="4">
          <h2 class="my-5">회원가입</h2>
          <v-img
            contain
            class="image"
            max-height="600"
            max-width="800"
            src="../../assets/img/login/interview2.jpg"
          ></v-img>
          <h1></h1>
          <v-form class="form" ref="form" v-model="valid" lazy-validation>
            <v-text-field v-model="username" :rules="nameRule" label="아이디" outlined dense required></v-text-field>
            <v-text-field v-model="email" :rules="emailRules" label="이메일" outlined dense required></v-text-field>
            <v-text-field
              v-model="password1"
              :rules="passwordRules"
              @click:append="show1 = !show1"
              :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
              :type="show1 ? 'text' : 'password'"
              label="비밀번호"
              required
              outlined
              dense
            ></v-text-field>
            <v-text-field
              v-model="password2"
              :rules="[passwordchkRules, passwordconfirmRules]"
              @click:append="show2 = !show2"
              :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
              :type="show2 ? 'text' : 'password'"
              label="비밀번호 확인"
              required
              outlined
              dense
            ></v-text-field>
            <v-btn
              large
              class="button"
              :disabled="!valid"
              color="#0277BD"
              @click="signup"
              rounded
            >회원가입</v-btn>
          </v-form>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
import axios from "axios";

const API_URL = 'https://j3a206.p.ssafy.io/api';

export default {
  name: "SignUp",
  components: {},
  data: () => ({
    valid: true,
    username: "",
    nameRule: [
      (v) => !!v || "아이디는 필수 입력항목입니다.",
      (v) => (v && v.length >= 5) || "5글자 이상 입력해야 합니다.",
    ],
    email: "",
    emailRules: [
      (v) => !!v || "E-Mail은 필수 입력항목입니다",
      (v) => /.+@.+\..+/.test(v) || "E-mail 양식이 올바르지 않습니다.",
    ],
    password1: "",
    passwordRules: [
      (v) => !!v || "비밀번호는 필수 입력항목입니다",
      (v) => (v && v.length >= 8) || "8글자 이상 입력해야 합니다.",
    ],
    password2: "",
    passwordchkRules: [(v) => !!v || "비밀번호 확인은 필수 입력항목입니다."],
    checkbox: false,
    show1: false,
    show2: false,
  }),

  computed: {
    passwordconfirmRules() {
      return () => this.password1 === this.password2 || "비밀번호가 다릅니다";
    },
    signupData() {
      return {
        username: this.username,
        email: this.email,
        password1: this.password1,
        password2: this.password2,
      };
    },
  },

  methods: {
    signup() {
      console.log(this.signupData);
      if (this.$refs.form.validate()) {
        axios
          .post(API_URL + "/rest-auth/registration/", this.signupData)
          .then((res) => {
            this.setCookie(res.data.key);
            this.$store.commit("setIsLoggedIn", true);
            this.$store.commit("setUsername", this.username);
            this.$router.push("/login");
          })
          .catch((err) => {
            alert("이미 등록된 아이디입니다.");
            console.log(err.response);
          });
      }
    },
    reset() {
      this.$refs.form.reset();
    },
    setCookie(token) {
      this.$cookies.set("ain", token);
      this.isLoggedIn = true;
    },
  },
};
</script>

<style scoped>
.form .button {
  cursor: pointer;
  color: #fff;
  display: block;
  font-size: 16px;
  width: 100%;
  padding: px;
}
</style>
