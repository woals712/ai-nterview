<template>
  <div class='question-list'>
    <v-row class='question-box' justify="center">
      <v-expansion-panels popout>
        <v-expansion-panel v-for="(question, i) in questionData" :key="i"
        >
        <div v-if="state == question.category.category" class='d-flex ml-4'>
          <v-checkbox v-model="selectedQuestion" :value=question.id color="red darken-3"></v-checkbox>
          <v-expansion-panel-header>
            <div style="line-height: 1.5em;">
              {{ question.question }}
            </div>
            </v-expansion-panel-header>
        </div>
          <v-expansion-panel-content v-if="state == question.category.category">
            <i class="fas fa-stopwatch mr-2" style='color: gray'></i>
            {{ question.time }} 분
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
    </v-row>
  </div>
</template>

<script>
export default {
  watch: {
    selectedQuestion() {
      this.$emit('submit-selected-question', this.selectedQuestion)
    }
  },
  data() {
    return {
      selectedQuestion: [],
      questionList: [],
    }
  },
  props: {
    questionData: Array,  
    state: Number
  },
  methods: {
  }
}
</script>

<style>
.question-list {
  overflow:auto;
}
.question-box {
  width: 100%;
}
</style>