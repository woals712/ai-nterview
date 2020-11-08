<template>
  <v-card
    class='mb-2 question-list'
    color="grey lighten-1"
    height="552px">
    <v-row class='question-box' justify="center">
      <v-expansion-panels popout>
        <v-expansion-panel v-for="(question, i) in selectedQuestionData" :key="i"
        >
        <div class='d-flex ml-4'>
          <v-icon slot="append" color="red" type='button' @click='removeQuestion(i)'>mdi-minus</v-icon>
          <v-expansion-panel-header>
            {{ question.question }}
            </v-expansion-panel-header>
        </div>
          <v-expansion-panel-content>
            <i class="fas fa-stopwatch mr-2" style='color: gray'></i>
            {{ question.time }} 분
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
    </v-row>
    <!-- <div class='d-flex justify-content-center'>
      <div class='information'>
        {{ toalCount }}개의 질문 총 {{ totalTime }} 분의 인터뷰 !
      </div>
    </div> -->
  </v-card>
</template>

<script>
export default {
  props: {
    selectedQuestionData: Array,
    selectedQuestionNumbers: Array
  },
  computed: {
    toalCount() {
      return this.selectedQuestionNumbers.length
    },
    totalTime() {
      const q = this.selectedQuestionData
      var sum = 0
      for (let i = 0; i < q.length; i++) {
        sum = sum + q[i].time
      }
      return sum
    }
  },
  watch: {
  },
  methods: {
    removeQuestion(index) {
      this
          .selectedQuestionNumbers
          .splice(index, 1)
      this
          .selectedQuestionData
          .splice(index, 1)
    },
  }
}
</script>

<style scoped>
.question-list {
  overflow:auto;
  padding: 15px;
}
.question-box {
  width: 100%;
}
.information {
  align-items: center;
  justify-content: center;
  background-color: white;
  height: 2rem;
  width: 60%;
}
</style>