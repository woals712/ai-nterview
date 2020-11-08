<template>
  <v-app id="inspire" dark>
    <v-toolbar app fixed clipped-left v-if="!showResult">
      <v-toolbar-title>{{ msgQuestion }}</v-toolbar-title>
      <span id="time"></span>
    </v-toolbar>
    <div v-if="showResult">
      <img
        src="https://cdn.pixabay.com/photo/2018/01/04/21/14/young-3061648_1280.jpg"
        width="50%"
      />
      <ResultModal :result="valence_list" />
      <div>수고하셨습니다 :)</div>
    </div>
    <v-content v-if="!showResult">
      <v-container fluid fill-height>
        <v-layout row wrap justify-center align-center>
          <!-- <v-flex sm12>
            <v-alert :value="booted" dismissible type="success"
              >Booted successfully!</v-alert
            >
            <v-alert :value="failed" dismissible type="error"
              >Failed to load correctly.</v-alert
            >
            <v-alert :value="webcamOk" dismissible type="info"
              >This may take few minutes</v-alert
            >
            <v-alert :value="webcamOk" dismissible type="info"
              >Webcam access allowed...</v-alert
            >
            <v-alert :value="webcamNotOk" dismissible type="error"
              >Webcam access denied.</v-alert
            >
          </v-flex> -->
          <v-flex class="player-wrapper" sm12 md8>
            <webcam-player
              @start="onStart"
              @stop="onStop"
              @next="onNext"
            ></webcam-player>
          </v-flex>
          <v-flex sm12 md4>
            <v-card class="elevation-16 mx-auto">
              <v-card-text>
                <appearance></appearance>
                <emotions></emotions>
              </v-card-text>
            </v-card>
          </v-flex>
          <v-flex sm12>
            <expressions></expressions>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
    <v-footer app fixed> </v-footer>
  </v-app>
</template>

<script>
import $ from "jquery";
import { EventBus } from "@/plugins/event-bus.js";
import WebcamPlayer from "@/components/camera/WebcamPlayer";
import Appearance from "@/components/camera/Appearance";
import Emotions from "@/components/camera/Emotions";
import Expressions from "@/components/camera/Expressions";
import ResultModal from "../../components/result/ResultModal";

export default {
  name: "app",
  components: {
    ResultModal,
    Appearance,
    Emotions,
    Expressions,
    "webcam-player": WebcamPlayer,
  },
  data() {
    return {
      booted: false,
      failed: false,
      webcamOk: false,
      webcamNotOk: false,
      valence: 0,
      valence_list: [],
      polling: null,
      msgQuestion: "재생버튼을 누르면 면접을 시작합니다.",
      myTimer: null,
      showResult: false,
      num: 0,
    };
  },
  mounted() {
    const that = this;
    const divRoot = $("#canvas")[0];
    // TODO: calculate the width according to the size of the device
    console.log("width:", this.computedWidth);
    console.log("inner width:", $(".player").innerWidth());
    const width = this.computedWidth;
    console.log("height:", this.computedHeight);
    const height = this.computedHeight;
    // const width = 640
    // const height = 480
    /*
      Face detector configuration - If not specified, defaults to F
      affdex.FaceDetectorMode.LARGE_FACES
      affdex.FaceDetectorMode.LARGE_FACES=Faces occupying large portions of the frame
      affdex.FaceDetectorMode.SMALL_FACES=Faces occupying small portions of the frame
    */
    const FACE_MODE = affdex.FaceDetectorMode.SMALL_FACE;

    //Construct a FrameDetector and specify the image width / height and face detector mode.
    this.$store.commit(
      "detector",
      new affdex.CameraDetector(divRoot, width, height, FACE_MODE)
    );

    //Enable detection of all Expressions, Emotions and Emojis classifiers.
    this.detector.detectAllEmotions();
    this.detector.detectAllExpressions();
    this.detector.detectAllEmojis();
    this.detector.detectAllAppearance();

    //Add a callback to notify when the detector is initialized and ready for runing.
    this.detector.addEventListener("onInitializeSuccess", function() {
      EventBus.$emit("InitializeSuccess");
      that.booted = true;
      //Display canvas instead of video feed because we want to draw the feature points on it
      $("#face_video_canvas").css("display", "block");
      $("#face_video").css("display", "none");
    });
    //Add a callback to notify when the detector has failed to load.
    this.detector.addEventListener("onInitializeFailure", function() {
      that.failed = true;
    });

    this.detector.addEventListener("onWebcamConnectSuccess", function() {
      that.webcamOk = true;
    });

    this.detector.addEventListener("onWebcamConnectFailure", function(e) {
      that.webcamNotOk = true;
    });

    //Add a callback to receive the results from processing an image.
    //The faces object contains the list of the faces detected in an image.
    //Faces object contains probabilities for all the different expressions, emotions and appearance metrics
    this.detector.addEventListener("onImageResultsSuccess", function(
      faces,
      image,
      timestamp
    ) {
      if (faces.length > 0) {
        // draw the feature points
        that.drawFeaturePoints(
          that,
          image,
          faces[0].emojis.dominantEmoji,
          faces[0].featurePoints
        );
        // appearance
        that.$store.commit("appearance", faces[0].appearance);
        // emotions
        that.$store.commit("emotions", faces[0].emotions);
        // console.log(faces[0].emotions["valence"]);
        that.valence = faces[0].emotions["valence"];
        // expressions
        that.$store.commit("expressions", faces[0].expressions);
      }
    });
  },
  computed: {
    detector() {
      return this.$store.getters.getDetector;
    },
    computedWidth() {
      return $(".player").width() - 40;
    },
    computedHeight() {
      return $(".player").width() / 1.33;
    },
    selectedQuestion() {
      return this.$store.getters.getSelectedQuestion;
    },
    totalTime() {
      const q = this.selectedQuestion;
      var sum = 0;
      for (let i = 0; i < q.length; i++) {
        sum = sum + q[i].time;
      }
      return sum;
    },
  },
  methods: {
    save_valence() {
      this.$store.commit("reset_valence");
      this.polling = setInterval(() => {
        this.$store.commit("add_valence", this.valence);
        console.log(this.valence);
      }, 500);
    },
    async onStart() {
      this.msgQuestion = this.selectedQuestion[0]["question"];
      var display = document.querySelector("#time");
      await this.startTimer(this.selectedQuestion[0]["time"] * 60, display);
      this.save_valence();
    },
    onStop() {
      clearInterval(this.polling);
      var valenceList = this.$store.getters.getValenceList;
      valenceList.push(100);
      this.valence_list.push(this.$store.getters.getValenceList);
      clearInterval(this.myTimer);
      this.showResult = true;
    },
    onNext() {
      clearInterval(this.myTimer);
      clearInterval(this.polling);
      var valenceList = this.$store.getters.getValenceList;
      valenceList.push(100);
      this.valence_list.push(this.$store.getters.getValenceList);
      this.num++;
      if (this.num < this.selectedQuestion.length) {
        var display = document.querySelector("#time");
        this.msgQuestion = this.selectedQuestion[this.num]["question"];
        this.startTimer(this.selectedQuestion[this.num]["time"] * 60, display);
        this.save_valence();
      } else {
        this.showResult = true;
      }
    },
    startTimer(duration, display) {
      var timer = duration,
        minutes,
        seconds;
      this.myTimer = setInterval(() => {
        minutes = parseInt(timer / 60, 10);
        seconds = parseInt(timer % 60, 10);

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.textContent = minutes + ":" + seconds;

        if (--timer < 0) {
          clearInterval(this.polling);
          var valenceList = this.$store.getters.getValenceList;
          valenceList.push(100);
          this.valence_list.push(this.$store.getters.getValenceList);
          if (this.num + 1 < this.selectedQuestion.length) {
            this.num++;
            this.msgQuestion = this.selectedQuestion[this.num]["question"];
            timer = this.selectedQuestion[this.num]["time"] * 60;
            this.save_valence();
          } else {
            clearInterval(this.myTimer);
            this.showResult = true;
          }
        }
      }, 1000);
    },
    drawFeaturePoints(vm, img, emoji, featurePoints) {
      var contxt = $("#face_video_canvas")[0].getContext("2d");

      var hRatio = contxt.canvas.width / img.width;
      var vRatio = contxt.canvas.height / img.height;
      var ratio = Math.min(hRatio, vRatio);

      contxt.strokeStyle = "rgb(0, 0, 0, 0)";
      for (var id in featurePoints) {
        if (id == 11) {
          contxt.font = "50px Arial";
          contxt.fillText(
            emoji,
            featurePoints[id].x + -40,
            featurePoints[id].y + -120
          );
          contxt.fillStyle = "rgba(245, 214, 93, 1)";
          contxt.fill();
        }
        // else {
        //   contxt.beginPath();
        //   contxt.arc(
        //     featurePoints[id].x,
        //     featurePoints[id].y,
        //     3,
        //     0,
        //     2 * Math.PI
        //   );
        //   // contxt.fillStyle = "rgba(0. 0, 0, 0)";
        //   // contxt.fill();
        // }
      }
    },
  },
};
</script>

<style>
.player-wrapper {
  width: 100%;
}
footer {
  display: flex;
  justify-content: center;
}
/* .player-wrapper,
.elevation-16 {
  min-height: 100%;
} */
#time {
  color: brown;
  margin: 0 30px;
}
</style>
