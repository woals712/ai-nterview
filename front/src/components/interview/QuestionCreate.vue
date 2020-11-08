<template>
  <div>
    <v-form>
      <v-container>
        <v-row>
          <v-col
            cols="12"
            lg="6"
          >
            <v-text-field
              v-model="title"
              filled
              background-color="white"
              color="blue-grey lighten-2"
              label="질문 제목"
            ></v-text-field>
          </v-col>
          <v-col
            cols="12"
            lg="6"
          >
            <v-text-field
              v-model="myQuestionData.time"
              filled
              background-color="white"
              color="blue-grey lighten-2"
              label="시간"
            ></v-text-field>
          </v-col>
          <v-col
            cols="12"
          >
            <v-text-field
              v-model="myQuestionData.question"
              filled
              background-color="white"
              color="blue-grey lighten-2"
              label="질문 내용"
            ></v-text-field>
          </v-col>
        </v-row>
      </v-container>
    </v-form>
      <v-switch
        v-model="autoUpdate"
        class="mt-0"
        color="green lighten-2"
        hide-details
        label="질문 공유"
      ></v-switch>
    <button @click="questionCreate">test</button>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'https://j3a206.p.ssafy.io/api';

  export default {
    data () {
      return {
        autoUpdate: true,
        title: '',
        myQuestionData: {
          question: '',
          time: '',
        },
          category: '',
    }
  },
  methods: {
    questionCreate() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get("ain")}`
        }
      }
      axios.post(API_URL + '/interview/questions/create/', this.myQuestionData, config)
      .then(() => {
        this.$emit('submit-state', 29)
      })
      .catch(err => {
        console.log(err.response)
      })
    }
  },
  computed: {
    username() {
      return this.$store.getters.getUsername
    }
  },
  mounted() {
    this.category = this.username
  }
}
</script>