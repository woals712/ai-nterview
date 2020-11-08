<template>
  <header>
    <div class="container">
      <div class="row">
        <div class="col-md-12">
          <h1>Welcome!</h1>
          <p class="lead">AI 면접 걱정, ai:nterview에서 해결하세요</p>

          <div class="carousel">
            <div class="carousel-inner">
              <v-carousel hide-delimiters>
                <v-carousel-item v-for="i in 3" :key="i">
                  <div v-if="i == 1">
                    <img
                      src="../../assets/img/main/carousel-1.jpg"
                      alt=""
                      style="width: 100%;"
                    />
                  </div>
                  <div v-if="i == 2">
                    <img
                      src="../../assets/img/main/carousel-2.jpg"
                      alt=""
                      style="width: 100%;"
                    />
                  </div>
                  <div v-if="i == 3">
                    <img
                      src="../../assets/img/main/carousel-3.jpg"
                      alt=""
                      style="width: 100%;"
                    />
                    <v-btn
                      depressed
                      color="primary"
                      class="start"
                      @click="$router.push('/home')"
                    >
                      <div class="start-text">
                        지금 바로 시작하기
                      </div>
                    </v-btn>
                  </div>
                </v-carousel-item>
              </v-carousel>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  data() {
    return {
      items: [
        {
          src: "../../assets/img/main/carousel-1.jpg",
        },
        {
          src: "https://cdn.vuetifyjs.com/images/carousel/sky.jpg",
        },
        {
          src: "https://cdn.vuetifyjs.com/images/carousel/bird.jpg",
        },
        {
          src: "https://cdn.vuetifyjs.com/images/carousel/planet.jpg",
        },
      ],
    };
  },
  methods: {
    nav() {
      var scrollTop = window.scrollTop();

      if (scrollTop > 10) {
        document.querySelector(".navbar-default").addClass("fixed-to-top");
      } else if (scrollTop == 0) {
        document.querySelector(".navbar-default").removeClass("fixed-to-top");
      }
    },
  },
};
</script>

<style scoped>
header {
  padding: 150px 0px 0px 0px;
  height: 800px;
  background: url("../../assets/img/main/meetingroom2.jpg");
  background-color: white !important;
  background-size: cover;
  background-repeat: no-repeat;
  color: white;
  position: relative;
}

header h1 {
  text-transform: uppercase;
  font-weight: 700;
  font-weight: 300;
  font-size: 100px;
  font-family: "Roboto Condensed", sans-serif;
}

header p.lead {
  font-size: 36px;
}

header .carousel {
  margin-right: auto;
  margin-left: auto;
  margin-top: 100px;
  width: 800px;
  height: 500px;
  background: url("../../assets/img/main/notebook.png") no-repeat;
  background-size: 100%;
}

header .carousel-inner {
  position: relative;
  top: 25px;
  margin-right: auto;
  margin-left: auto;
  padding: 1px 0px 0px 4px;
  width: 76%;
  height: 76%;
}

header .start {
  position: relative;
  top: -100px;
}

header .start-text {
  color: white;
}
</style>
