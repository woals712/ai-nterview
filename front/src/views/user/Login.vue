<template>
  <div class="Login">
    <v-app>
      <v-container>
        <v-row justify="center">
          <v-col cols="10" sm="8" md="8" lg="4" style="max-height: 800px">
            <h2>AI:nterview에 오신것을 환영합니다</h2>
            <v-img
              contain
              class="image"
              max-height="600"
              max-width="800"
              src="../../assets/img/login/interview2.jpg"
            ></v-img>
            <h1></h1>
            <v-form class="form" ref="form" v-model="valid" lazy-validation>
              <v-text-field
                v-model="username"
                :rules="[idRules.required, idRules.min]"
                label="아이디"
                required
                outlined
                dense
              ></v-text-field>
              <v-text-field
                v-model="password"
                :rules="[rules.required, rules.min]"
                label="비밀번호"
                @click:append="show = !show"
                :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
                :type="show ? 'text' : 'password'"
                outlined
                dense
                @keypress.enter="login"
              ></v-text-field>
              <v-btn
                large
                class="button"
                :disabled="!valid"
                color="#0277BD"
                @click="login"
                rounded
              >로그인</v-btn>
            </v-form>
          </v-col>
        </v-row>
      </v-container>
    </v-app>
  </div>
</template>

<script>
import axios from "axios";

const API_URL = 'https://j3a206.p.ssafy.io/api';

export default {
  name: "Login",
  components: {},
  data: () => ({
    valid: true,
    username: "",
    idRules: {
      required: (value) => !!value || "아이디를 입력해주세요.",
      min: (v) => (v && v.length >= 5) || "아이디는 5글자 이상 입력해주세요.",
    },
    password: "",
    rules: {
      required: (value) => !!value || "비밀번호를 입력해주세요.",
      min: (v) => (v && v.length >= 8) || "비밀번호는 8글자 이상 입력해주세요.",
    },
    checkbox: false,
    show: false,
  }),
  created() {
    let token = this.$cookies.get("ain"); //ain이 key인 쿠키 가져옴
    if (token) {
      //토큰 존재하면
      this.$router.push("/"); //home으로 보냄
    }
  },
  methods: {
    login() {
      if (this.$refs.form.validate()) {
        axios
          .post(API_URL + "/rest-auth/login/", {
            username: this.username,
            password: this.password,
          })
          .then((res) => {
            this.setCookie(res.data.key);
            this.$store.commit("setIsLoggedIn", true);
            this.$store.commit("setUsername", this.username);
            console.log(res.config.data);
            alert("AI:nterview에 오신것을 환영합니다.");
            this.$router.push("/");
          })
          .catch((err) => {
            alert("아이디와 비밀번호를 확인해주세요");
            console.log(err);
          });
      }
    },
    setCookie(token) {
      this.$cookies.set("ain", token);
      this.isLoggedIn = true;
    },
  },
};
</script>

<style>
.login-body {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  /* min-height: 100vh; */
}

.form .button {
  cursor: pointer;
  color: #fff;
  display: block;
  font-size: 16px;
  width: 100%;
  padding: 10px;
}
.add-option .routers {
  margin: 0 5px;
  text-decoration: none;
  color: #222;
}
</style>
