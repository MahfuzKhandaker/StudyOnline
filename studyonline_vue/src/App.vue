<template>
  <nav
    class="navbar is-info"
    role="navigation"
    aria-label="main navigation"
    style="min-height: 5rem"
  >
    <div class="navbar-brand">
      <a href="/" class="navbar-item is-size-4">StudyOnline</a>
    </div>

    <div id="navbar-item" class="navbar-menu">
      <div class="navbar-start">
        <a href="#" class="navbar-item">Home</a>
        <a href="#" class="navbar-item">About</a>
      </div>

      <div class="navbar-end">
        <div class="navbar-item">
          <div class="buttons">
            <a href="#" class="button is-primary">Sign up</a>
            <a href="#" class="button is-light">Log in</a>
          </div>
        </div>
      </div>
    </div>
  </nav>
  <router-view />

  <footer class="footer">
    <p class="has-text-centered">Copyright (c) 2022</p>
  </footer>
</template>

<style lang="scss">
@import "../node_modules/bulma";
</style>
