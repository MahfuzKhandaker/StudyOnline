<template>
  <app-nav-bar />
  <router-view />
  <app-footer-component />
</template>

<script>
  import NavBar from "@/components/NavBar.vue";
  import FooterComponent from "@/components/FooterComponent.vue";
  
  import axios from "axios";
  
  export default {
    name:"App",
    components: {
      'app-nav-bar': NavBar,
      'app-footer-component': FooterComponent,
    },
    beforeCreate() {
      this.$store.commit('initializeStore')

      const token = this.$store.state.user.token

      if (token) {
        axios.defaults.headers.common['Authorization'] = "Token" + token
      } else {
        axios.defaults.headers.common['Authorization'] = ""
      }
    }
  }
</script>
<style lang="scss">
@import "../node_modules/bulma";
</style>
