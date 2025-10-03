<template>
  <div class="section">
    <div class="grid">
      <movieCard v-for="movie in movies" :key="movie.id" :movie="movie" />
    </div>
  </div>
</template>
<script lang="ts">
import axios from 'axios'
import movieCard from './movieCard.vue'
export default {
  name: 'MoviesDetail',
  components: { movieCard },
  data() {
    return { movies: [] }
  },
  async mounted() {
    const moviesResponse = await axios.get('http://localhost:8888/movies')
    console.log(moviesResponse)
    this.movies = moviesResponse.data.objects
  },
}
</script>
<style>
.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}
</style>
