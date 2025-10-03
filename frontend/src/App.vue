<template>
  <NavBar />
  <RouterView />
</template>
<script lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import NavBar from './components/NavBar.vue'
export default {
  name: 'App',
  components: {
    NavBar,
    RouterLink,
    RouterView,
  },
}
</script>
<style scoped></style>
