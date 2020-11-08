export default {
  state: {
    selectedQuestionList: []
  },
  getters: {
    getSelectedQuestion(state) {
      return state.selectedQuestionList
    }
  },
  mutations: {
      setSelectedQuestion(state, payload) {
          state.selectedQuestionList = payload
      },
  },
  actions: {
    
  },
}
