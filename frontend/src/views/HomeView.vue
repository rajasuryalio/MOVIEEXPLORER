<template>
  <main>
    <!-- <RouterLink to="/">Home</RouterLink>
    <RouterLink to="/actors">Actors</RouterLink>
    <RouterLink to="/movies">Movies</RouterLink>
    <RouterLink to="/genres">Genres</RouterLink> -->
    <!-- {{ actors }}
    {{ movies }}
    {{ directors }}
    {{ genres }} -->
  </main>
</template>
<script lang="ts">
import axios from 'axios'
import NavBar from '@/components/NavBar.vue'

export default {
  name: 'HomeView',
  components: {
    NavBar,
  },
  data() {
    return {
      actors: '',
      movies: '',
      directors: '',
      genres: '',
    }
  },
  async mounted() {
    // const actorsResponse = await axios.get('http://localhost:8888/actors')
    // console.log(actorsResponse)
    // this.actors = actorsResponse.data.actors
    // const moviesResponse = await axios.get('http://localhost:8888/movies')
    // console.log(moviesResponse)
    // this.movies = moviesResponse.data.movies
    // const directorsResponse = await axios.get('http://localhost:8888/directors')
    // console.log(directorsResponse)
    // this.directors = directorsResponse.data.directors
    // const genresResponse = await axios.get('http://localhost:8888/genres')
    // console.log(genresResponse)
    // this.genres = genresResponse.data.genres
  },
}
</script>
