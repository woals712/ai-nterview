<template>
  <div class="text-center">
    <v-dialog
      v-model="dialog"
      width="1000"
      min-height="800"
      :style="{ background: $vuetify.theme.themes.light.background }"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="red lighten-2"
          dark
          v-bind="attrs"
          v-on="on"
          @click="test"
        >
          결과 보기
        </v-btn>
      </template>

      <v-card :style="{ background: $vuetify.theme.themes.light.background }">
        <v-card-title class="text-center justify-center py-6">
          <h4 class="font-weight-bold display-3 basil--text">
            면접 결과
          </h4>
        </v-card-title>

        <v-tabs
          v-model="tab"
          background-color="transparent"
          color="basil"
          center-actvie
          grow
        >
          <v-tab v-for="i in result.length" :key="i"> Question {{ i }} </v-tab>
        </v-tabs>

        <v-tabs-items v-model="tab">
          <v-tab-item v-for="item in result" :key="item">
            <v-card color="basil" flat>
              <Result
                @close-dialog="dialog = false"
                :state="tab"
                :result="item"
              />
            </v-card>
          </v-tab-item>
        </v-tabs-items>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import Result from "./Result";
export default {
  props: {
    result: Array,
  },
  components: {
    Result,
  },
  data() {
    return {
      dialog: false,
      tab: -1,
    };
  },
  methods: {
    test() {
      this.tab = 0;
      console.log(this.tab);
    },
  },
};
</script>

<style></style>
