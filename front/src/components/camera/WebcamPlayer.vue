<template>
  <v-card class="player elevation-16 mx-auto">
    <v-card-text>
      <div v-show="!loading" id="canvas"></div>
      <v-layout v-show="loading" justify-center align-center>
        <v-progress-circular
          :size="70"
          :width="7"
          color="white"
          indeterminate
        ></v-progress-circular>
      </v-layout>
    </v-card-text>
    <v-divider></v-divider>
    <v-card-actions class="justify-center">
      <v-btn @click="reset" fab small color="cyan">
        <v-icon v-text="'mdi-replay'"></v-icon>
      </v-btn>
      <v-btn @click="start" fab large color="blue">
        <v-icon v-text="'mdi-play'"></v-icon>
      </v-btn>
      <v-btn @click="stop" fab small color="red">
        <v-icon v-text="'mdi-stop'"></v-icon>
      </v-btn>
      <v-btn @click="next" color="yellow">
        <span>다음 질문</span>
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import { EventBus } from "@/plugins/event-bus.js";

export default {
  data() {
    return {
      loading: false,
    };
  },
  mounted() {
    const that = this;
    EventBus.$on("InitializeSuccess", () => (that.loading = false));
  },
  computed: {
    detector() {
      return this.$store.getters.getDetector;
    },
  },
  methods: {
    start() {
      if (this.detector && !this.detector.isRunning) {
        this.detector.start();
        this.loading = true;
        this.$emit("start");
      }
    },

    stop() {
      if (this.detector && this.detector.isRunning) {
        this.detector.removeEventListener();
        this.detector.stop();
        this.loading = false;
        this.$emit("stop");
      }
    },

    reset() {
      if (this.detector && this.detector.isRunning) {
        this.detector.reset();
      }
    },

    next() {
      if (this.detector && this.detector.isRunning) {
        this.$emit("next");
      }
    },
  },
};
</script>

<style>
#canvas {
  display: flex;
  justify-content: center;
  transform: rotateY(180deg);
  /* height: 582.6 px; */
  /* width: 456.6 px; */
}
</style>
