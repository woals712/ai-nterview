<template>
  <v-stepper v-model='e1'>
    <v-stepper-header>
      <v-stepper-step
        editable
        step="1"
        :complete="e1 > 1"
        @click='e1=1'
      >
        질문 모아보기
      </v-stepper-step>

      <v-divider></v-divider>

      <v-stepper-step
        editable
        step="2"
        :complete="e1 > 2"
      >면접 질문 선택</v-stepper-step>

      <v-divider></v-divider>

      <v-stepper-step
        step="3"
        editable
      >
        면접 준비
      </v-stepper-step>
    </v-stepper-header>
    <v-stepper-items class='row'>
      <QuestionCategory v-if="e1==1" @submit-question-state="changeState" class='col-lg-4' />
      <v-stepper-content step="1" class='step1-content col-lg-8'>
        <div v-if="state">
          <div v-if="state == 'newQuestion'" class='question'>
            <div v-if="isLoggedIn">
              <QuestionCreate @submit-state="state = username" />
            </div>
            <div v-else>
              <CheckLoginModal />
            </div>
          </div>
          <div v-else class='question'>
            <div v-if="state == username && !isLoggedIn">
              <CheckLoginModal />
            </div>
            <div v-else>
              <Question @submit-selected-question="selectedQuestion" :state="state" :questionData="questionData" class='question'/>
            </div>
          </div>
          <div class='btns'>
            <div>현재 선택된 질문 : {{ selectedQuestionNumbers.length }} </div>
            <v-btn
              color="primary"
              @click="e1 = 2"
            >
              Continue
            </v-btn>
          </div>
        </div>
        <v-card v-else class='non-question d-flex justify-content-center align-items-center'>
          <div>
            <h4 class='step'>STEP 1</h4>
            <img src="../../assets/img/interview/cart.png" alt="" class='message-icon' style="height: 200px; margin-bottom: 20px;">
            <h6>원하시는 카테고리 내의 면접 질문들을 선택하세요.</h6>
          </div>
        </v-card>
      </v-stepper-content>

      <v-stepper-content step="2">
        <QuestionDecision :selectedQuestionData="selectedQuestionData" :selectedQuestionNumbers="selectedQuestionNumbers" />
        <div class="btns">
          <v-btn @click="e1 = 1" class='back-btn' text>뒤로가기</v-btn>
          <div>
            {{ toalCount }}개의 질문 총 {{ totalTime }} 분의 인터뷰 !
          </div>
          <v-btn
            color="primary"
            @click="e1 = 3"
            class='continue-btn'
          >
            Continue
          </v-btn>
        </div>

      </v-stepper-content>

      <v-stepper-content step="3">
        <CameraTest />

        <div class="btns">
          <v-btn @click="e1 = 2" class='back-btn' text>뒤로가기</v-btn>
          <v-btn
            color="primary"
            @click="$router.push('/interview')"
            :selectedQuestionData="selectedQuestionData"
          >
            <div class='start-text continue-btn'>
              START
            </div>
          </v-btn>
        </div>

      </v-stepper-content>
    </v-stepper-items>
  </v-stepper>
</template>

<script>
import Question from "./Question.vue"
import QuestionCategory from "./QuestionCategory.vue"
import QuestionDecision from "./QuestionDecision.vue"
import CameraTest from "./CameraTest.vue"
import QuestionCreate from "./QuestionCreate.vue"
import CheckLoginModal from "../user/CheckLoginModal.vue"
import axios from 'axios'
import { mapGetters, mapMutations } from "vuex"

const API_URL = 'https://j3a206.p.ssafy.io/api';

export default {
  components: {
    CameraTest,
    QuestionDecision,
    Question,
    QuestionCreate,
    QuestionCategory,
    CheckLoginModal,
  },
  data () {
    return {
      e1: 1,
      state: null,
      questionData: null,
      selectedQuestionData: [],
      selectedQuestionNumbers: []
    }
  },
  methods: {
    changeState(state) {
     this.state = state 
     console.log(state)
    },
    getQuestionData() {
      axios.get(API_URL + '/interview/questions/')
      .then(res => {
        this.questionData = res.data
        console.log(res.data)
      })
      .catch(err => {
        console.log(err.response)
      })
    },
    selectedQuestion(res) {
      this.selectedQuestionNumbers = res
    },
    ...mapMutations({
      setSelectedQuestion: 'QuestionList/setSelectedQuestion'
    })
  },
  mounted() {
    this.getQuestionData()
  },
  computed: {
    ...mapGetters({
      getSelectedQuestion: 'QuestionList/getSelectedQuestion'
    }),
    isLoggedIn(){
      return this.$store.getters.getIsLoggedIn;
    },
    username(){
      return this.$store.getters.getUsername;
    },
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
    selectedQuestionNumbers() {
      var selectedQuestionData = []
      for (var i = 0; i < this.selectedQuestionNumbers.length; i++) {
        selectedQuestionData.push(this.questionData[this.selectedQuestionNumbers[i]-1])
      }
      this.selectedQuestionData = selectedQuestionData
      // this.setSelectedQuestion(selectedQuestionData)
      this.$store.commit('setSelectedQuestion', this.selectedQuestionData)
    }

  }
}
</script>

<style scoped>
.question {
  padding-bottom: 2rem;
  height: 550px;
}
.non-question {
  padding-bottom: 2rem;
  height: 600px;
}
.btns{
  height: 50px;
  display: flex;
  justify-content: space-between;
  padding: 13px 10px;
}

.start-text {
  color: white;
}
.step1-content {
  background-color: lightgrey;
}
.step {
  margin: auto;
  color: white;
  background-color: black;
  width: 130px;
}
</style>