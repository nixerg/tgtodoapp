<template>
 <div class="app-container">
  <router-view />
  <navbar />
 </div>
</template>

<script>
import navbar from './components/navbar.vue'

export default {
  name: 'App',
  components: {
    navbar
  }
}
</script>

<style scoped>
.app-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh
}
</style> 