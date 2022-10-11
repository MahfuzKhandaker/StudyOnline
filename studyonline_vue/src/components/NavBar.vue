<template>

<section class="hero is-primary is-bold">
  <!-- Hero header: will stick at the top -->
  <div class="hero-head">
    <nav class="navbar" style="min-height: 3rem">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item is-size-4">StudyOnline</router-link>
        <!--  
        <a class="navbar-item" href="/">
          <img src="http://bulma.io/images/bulma-logo.png" alt="Logo">
        </a>
      -->
      
        <!--
    Using the v-on: directive to listen for the click event and toggle the data property showNav. Also, using the v-bind: directive to reactively update the class attribute 'is-active' based on the showNav property.
    -->
        <div class="navbar-burger" @click="showNav = !showNav" :class="{ 'is-active': showNav }">
          <span></span>
          <span></span>
          <span></span>
        </div>
      </div>
      <!--
    Using the v-bind: directive to reactively update the class attribute 'is-active' based on the showNav property.
    -->
      <div class="navbar-menu" :class="{ 'is-active': showNav }">
        <div class="navbar-start">
          <router-link to="/" class="navbar-item">Home</router-link>
          <router-link to="/about" class="navbar-item">About</router-link>
          <router-link to="/courses" class="navbar-item">Courses</router-link>
      </div>

        <div class="navbar-end">
          <template v-if="$store.state.user.isAuthenticated">
            <router-link to="/dashboard/my-account" class="button is-info">My account</router-link>
          </template>
          <template v-else>
            <router-link to="/sign-up" class="button is-primary">Sign up</router-link>

            <router-link to="/log-in" class="button is-light">Log in</router-link>
          </template>
          
        </div>
      </div>
    </nav>
  </div>
  <!-- Hero content: will be in the middle -->
  <div class="hero-body">
    <div class="container has-text-centered">
    </div>
  </div>
</section>
</template>

<script>
  export default {
    data() {
      return {
      showNav: false
      }
    }
  }
</script>