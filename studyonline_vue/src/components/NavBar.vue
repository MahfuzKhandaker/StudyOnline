<template>

<section class="hero is-primary is-bold">
  <!-- Hero header: will stick at the top -->
  <div class="hero-head">
    <nav class="navbar" style="min-height: 3rem">
      <div class="navbar-brand">
        <a href="/" class="navbar-item is-size-4">StudyOnline</a>
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
        <a href="/" class="navbar-item">Home</a>
        <a href="/about" class="navbar-item">About</a>
      </div>

        <div class="navbar-end">
          <a href="/sign-up" class="button is-primary">Sign up</a>

          <a href="/log-in" class="button is-light">Log in</a>
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

  <!--  
    <nav
    class="navbar"
    style="min-height: 3rem"
  >
    <div class="navbar-brand">
      <a href="/" class="navbar-item is-size-4">StudyOnline</a>
    </div>

    <div id="navbar-item" class="navbar-menu">
      <div class="navbar-start">
        <a href="/" class="navbar-item">Home</a>
        <a href="/about" class="navbar-item">About</a>
      </div>

      <div class="navbar-end">
        <div class="navbar-item">
          <div class="buttons">
            <a href="/sign-up" class="button is-primary">Sign up</a>
            <a href="/log-in" class="button is-light">Log in</a>
          </div>
        </div>
      </div>
    </div>
  </nav>
  -->
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