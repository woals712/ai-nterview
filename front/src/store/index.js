import Vue from "vue";
import Vuex from "vuex";
import QuestionList from "./modules/QuestionList";
import UserStore from "./modules/UserStore";
import InterviewStore from "./modules/InterviewStore";
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {},
  mutations: {},
  actions: {},
  modules: {
    QuestionList,
    UserStore,
    InterviewStore,
  },
  plugins: [
    createPersistedState({
      paths: ["QuestionList", "UserStore", "InterviewStore"],
    }),
  ],
});
