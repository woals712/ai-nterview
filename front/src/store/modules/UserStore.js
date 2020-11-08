export default {
  state: {
    isLoggedIn: false,
    username: '',
  },
  getters: {
    getIsLoggedIn(state) {
      return state.isLoggedIn
    },
    getUsername(state) {
      return state.username
    }
  },
  mutations: {
      setIsLoggedIn(state, payload) {
          state.isLoggedIn = payload
      },
      setUsername(state, payload) {
          state.username = payload
      },
  },
  actions: {
    
  },
}
