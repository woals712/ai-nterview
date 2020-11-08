<template>
  <v-app>
    <div id="app">
      <NavBar />
      <div id="body">
        <router-view/>
      </div>
    </div>
  </v-app>
</template>

<script>
import NavBar from './components/common/NavBar.vue'

export default {
  components: {
    NavBar,
  },
}
</script>

<style>
@font-face { 
  font-family: 'NanumSquareRound'; 
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_two@1.0/NanumSquareRound.woff') format('woff'); 
  font-weight: 1000; 
  font-style: normal; }
@import url(https://cdn.jsdelivr.net/gh/moonspam/NanumSquare@1.0/nanumsquare.css);

#app {
  font-family: NanumSquareRound, Avenir, Helvetica, Arial, sans-serif;
  font-weight: 700;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
