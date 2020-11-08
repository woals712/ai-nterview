<template>
  <nav>
    <v-navigation-drawer v-model="drawer" dark app mini-variant mini-variant-width="110" class='cyan darken-1'>
      <v-list>
        <v-list-item class='mb-12'>
          <v-lsit-item-action></v-lsit-item-action>
        </v-list-item>
      </v-list>
      <v-list flat>
        <v-list-item router to="">
          <v-list-item-content>
            <v-icon class="mb-2">fas fa-chart-line</v-icon>
            <v-list-item-subtitle align='center'>Dashboard</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
        <v-list-item router to="">
          <v-list-item-content>
            <v-icon class="mb-2">fas fa-notes-medical</v-icon>
            <v-list-item-subtitle align='center'>Doctor</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>

        <v-list-item router to="">
          <v-list-item-content>
            <v-icon class="mb-2">fas fa-user-md</v-icon>
            <v-list-item-subtitle align='center'>contact</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>

        <v-list-item router to="">
          <v-list-item-content>
            <v-icon class="mb-2">fas fa-signature</v-icon>
            <v-list-item-subtitle align='center'>Tracker</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-list>
      <v-list style='position: absolute; bottom:0' class="ml-3" flat>
        <v-list-item router to="">
          <v-list-item-action>
            <v-icon right>fas fa-sign-out-alt</v-icon>
          </v-list-item-action>
        </v-list-item>

      </v-list>
    </v-navigation-drawer>
  </nav>
</template>

<script>
export default {
data() {
  return {
    drawer: true
  }
}
}
</script>

<style>

</style>