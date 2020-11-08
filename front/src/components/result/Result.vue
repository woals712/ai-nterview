<template>
  <div>
    <v-container>
      <div class="question">
        {{ selectedQuestions[state]["question"] }}
      </div>
      <v-flex class="mt-12">
        <v-row no-gutters>
          <v-col cols="12" md="8" class="result-container">
            <v-flex>
              <v-list class="mt-5">
                <v-list-item>
                  <v-list-item-title class="cyan--text text--darken-1"
                    >Emotion Curve</v-list-item-title
                  >
                </v-list-item>
              </v-list>
            </v-flex>
            <v-flex class="flex-container">
              <div class="emoticons">
                <div class="emoticon">
                  😁
                </div>
                <div class="emoticon">
                  😊
                </div>
                <div class="emoticon">
                  😐
                </div>
                <div class="emoticon">
                  😕
                </div>
                <div class="emoticon">
                  🙁
                </div>
              </div>
              <v-sparkline
                :value="result"
                :gradient="gradient"
                :smooth="radius || false"
                :pading="padding"
                :line-width="width"
                :stroke-linCap="lineCap"
                :gradient-direction="gradientDirection"
                :fill="fill"
                :type="type"
                :auto-line-width="autoLineWidth"
                auto-draw=""
              >
              </v-sparkline>
            </v-flex>
            <!-- <v-flex class="mt-5">
              <v-list class="ml-5">
                <v-list-item>
                  <v-list-item-avatar
                    color="cyan darken-1"
                    size="20px"
                  ></v-list-item-avatar>
                  <v-list-item-title>Average</v-list-item-title>
                  <v-list-item-avatar
                    color="cyan darken-1"
                    size="20px"
                  ></v-list-item-avatar>
                  <v-list-item-title class="ml-5">My Data</v-list-item-title>
                </v-list-item>
              </v-list>
            </v-flex> -->
          </v-col>
          <v-col cols="12" md="4" class="result-container">
            <v-flex class="score">
              <v-list class="mt-5">
                <v-list-item>
                  <v-list-item-title class="cyan--text text--darken-1"
                    >Score</v-list-item-title
                  >
                </v-list-item>
              </v-list>
              <!-- <div class="gauge">
                        <div class="gauge__body">
                          <div class="gauge__fill"></div>
                          <div class="gauge__cover"></div>
                        </div>
                      </div> -->
              <!-- <div class="inner-score">
                <progress :value="average" max="100"></progress>
                <h4>
                  {{ average }}
                </h4>
              </div> -->
              <h5>당신의 점수는...</h5>
              <h3>{{ average }}점</h3>
            </v-flex>
          </v-col>
        </v-row>
      </v-flex>
      <v-btn color="primary" text @click="$emit('close-dialog')" class="btn-ok">
        확인 !
      </v-btn>
    </v-container>
  </div>
</template>

<script>
const gradients = [
  ["#222"],
  ["#42b3f4"],
  ["red", "orange", "yellow"],
  ["purple", "violet"],
  ["#00c6ff", "#F0F", "#FF0"],
  ["#f72047", "#ffd200", "#1feaea"],
];

export default {
  components: {},
  props: {
    state: Number,
    result: Array,
  },
  data() {
    return {
      width: 2,
      radius: 10,
      padding: 8,
      lineCap: "round",
      gradient: gradients[5],
      gradientDirection: "top",
      gradients,
      fill: false,
      arrayEvents: null,
      type: "trend",
      autoLineWidth: false,
      date2: new Date().toISOString().substr(0, 10),
    };
  },
  computed: {
    average() {
      var sum = 0;
      for (var i = 0; i < this.result.length; i++) {
        sum = sum + this.result[i];
      }
      sum = (sum / this.result.length + 100) / 4 + 50;
      return parseInt(sum);
    },
    theme() {
      return this.$vuetify.theme.dark ? "dark" : "light";
    },
    selectedQuestions() {
      return this.$store.getters.getSelectedQuestion;
    },
  },
  watch: {
    state() {
      console.log("test");
      const gaugeElement = document.querySelector(".gauge");

      function setGaugeValue(gauge, value) {
        if (value < 0 || value > 1) {
          return;
        }

        gauge.querySelector(".gauge__fill").style.transform = `rotate(${value /
          2}turn)`;
        gauge.querySelector(".gauge__cover").textContent = `${Math.round(
          value * 100
        )}%`;
      }
      const average = this.average / 100;
      setGaugeValue(gaugeElement, average);
    },
  },
  mounted() {
    this.arrayEvents = [...Array(6)].map(() => {
      const day = Math.floor(Math.random() * 30);
      const d = new Date();
      d.setDate(day);
      return d.toISOString().substr(0, 10);
    });
  },
  methods: {
    functionEvents(date) {
      const [, , day] = date.split("-");
      if ([12, 17, 28].includes(parseInt(day, 10))) return true;
      if ([1, 19, 22].includes(parseInt(day, 10))) return ["red", "#00f"];
      return false;
    },
  },
};
</script>

<style scoped lang="scss">
.question {
  font-weight: 200;
  margin-top: 30px;
}
.result-container {
  padding: 0 15px;
  // display: flex;
  // align-content: ;
  .score {
    display: flex;
    flex-direction: column;
    align-items: flex-end;

    .inner-score {
      display: flex;
      flex-direction: column;
      align-items: flex-end;
    }
  }
}
.flex-container {
  display: flex;
  flex-direction: row;
}
svg {
  width: 50rem;
}
.emoticons {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.score {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
}
/* progress {
  background-color: #93cdff;
  width: 100%;
} */
.rounded {
  border-top-left-radius: 50px;
  border-bottom-left-radius: 50px;
}
.gauge {
  width: 100%;
  max-width: 250px;
  font-family: "Roboto", sans-serif;
  font-size: 32px;
  color: #004033;
}

.gauge__body {
  width: 100%;
  height: 0;
  padding-bottom: 50%;
  background: #b4c0be;
  position: relative;
  border-top-left-radius: 100% 200%;
  border-top-right-radius: 100% 200%;
  overflow: hidden;
}

.gauge__fill {
  position: absolute;
  top: 100%;
  left: 0;
  width: inherit;
  height: 100%;
  background: #009578;
  transform-origin: center top;
  transform: rotate(0.25turn);
  transition: transform 0.2s ease-out;
}

.gauge__cover {
  width: 75%;
  height: 150%;
  background: #ffffff;
  border-radius: 50%;
  position: absolute;
  top: 25%;
  left: 50%;
  transform: translateX(-50%);

  /* Text */
  display: flex;
  align-items: center;
  justify-content: center;
  padding-bottom: 25%;
  box-sizing: border-box;
}
.btn-ok {
  margin-top: 20px;
}
</style>
