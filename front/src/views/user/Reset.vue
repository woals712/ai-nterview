<template>
  <div>
  </div>
</template>

<script>
export default {
  methods: {
    reset() {
        this.$store.commit("setIsLoggedIn", false);
        this.$cookies.remove("ain");
        this.$store.commit("setUsername", "");
        this.$router.push('/')
    }
  },
  mounted() {
    this.reset()
  }
}
</script>

<style>

</style>