import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import vuetify from "./plugins/vuetify";
import store from "./store";
import "@babel/polyfill";
import VueCookie from "vue-cookie";
import axios from "axios";
import "./registerServiceWorker";

Vue.config.productionTip = false;
Vue.prototype.$http = axios;
Vue.use(VueCookie);

new Vue({
  router,
  vuetify,
  store,
  render: (h) => h(App),
}).$mount("#app");
