<template>
  <div>
    <nav
      class="navbar navbar-default navbar-expand-lg navbar-light bg-light d-flex justify-content-between"
    >
      <img
        class="logo"
        src="../../assets/img/main/logo.png"
        type="button"
        alt
        @click="$router.push('/')"
      />
      <v-btn
        color="primary"
        text
        dark
        v-bind="attrs"
        v-on="on"
        @click="$router.push('/home')"
        >모의 면접 바로가기</v-btn
      >
      <div class="d-flex">
        <div v-if="!isLoggedIn" class="d-flex">
          <v-toolbar-items>
            <v-btn color="success" @click="$router.push('/login')">
              <v-icon left>mdi-pencil</v-icon>로그인
            </v-btn>
            <v-divider vertical></v-divider>
            <v-btn color="warning" @click="$router.push('/signup')">
              <v-icon left>mdi-account-circle</v-icon>회원가입
            </v-btn>
          </v-toolbar-items>
        </div>
        <div bottom v-else class="d-flex">
          <div>{{ username }} 님 환영합니다.</div>
          <v-menu open-on-hover center offset-y>
            <template v-slot:activator="{ on, attrs }">
              <v-btn color="success" text dark v-bind="attrs" v-on="on" small>
                <v-icon>mdi-account-circle</v-icon>
              </v-btn>
            </template>
            <v-list>
              <v-list-item>
                <v-list-item-title
                  style="cursor:pointer"
                  @click="$router.push('/mypage')"
                  >내 정보</v-list-item-title
                >
              </v-list-item>
              <v-list-item>
                <v-list-item-title style="cursor:pointer" @click="logout"
                  >로그아웃</v-list-item-title
                >
              </v-list-item>
            </v-list>
          </v-menu>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
import axios from "axios";

const API_URL = 'https://j3a206.p.ssafy.io/api';

export default {
  methods: {
    logout() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get("ain")}`,
        },
      };
      axios.post(API_URL + "/rest-auth/logout/", null, config).then(() => {
        this.$store.commit("setIsLoggedIn", false);
        this.$cookies.remove("ain");
        this.$store.commit("setUsername", "");
        alert("로그아웃 성공!");
        this.$router.push("/");
      });
    },
  },
  computed: {
    isLoggedIn() {
      return this.$store.getters.getIsLoggedIn;
    },
    username() {
      return this.$store.getters.getUsername;
    },
  },
};
</script>

<style scoped>
.nav-title {
  font-size: 2rem;
}

.navbar {
  height: 60px;
  padding-left: 40px;
  padding-right: 40px;
  font-size: 1.3rem;
  z-index: 100;
}
.navbar-default {
  border: none;
  border-bottom: 1px solid #eee;
  background: #fff;
  opacity: 0.95;
  display: none;
}
.navbar.fixed-to-top {
  top: 0px;
}
.logo {
  height: 50px;
}
.start-text {
  color: white;
}
</style>
