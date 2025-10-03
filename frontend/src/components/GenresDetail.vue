<template>
  <GenreCard v-for:="genre in genres" :key="genre.id" :genre="genre" />
</template>
<script lang="ts">
import axios from 'axios'
import GenreCard from './GenreCard.vue'

export default {
  name: 'GenresDetail',
  components: { GenreCard },
  data() {
    return { genres: [] }
  },
  async mounted() {
    const genresResponse = await axios.get('http://localhost:8888/genres')
    console.log(genresResponse)
    this.genres = genresResponse.data.objects
  },
}
</script>
