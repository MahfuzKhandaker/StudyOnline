<template>
    <footer class="footer">
    <p class="has-text-centered">Copyright (c) - {{currentYear}}</p>
  </footer>
</template>

<script>
  export default {
    data() {
      return {
        currentYear: new Date().getFullYear() //2022
      }
    }
  }
</script>