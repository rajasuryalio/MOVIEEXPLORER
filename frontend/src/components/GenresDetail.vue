<template>
  <div>{{ genres }}</div>
</template>
<script lang="ts">
import axios from 'axios'
export default {
  name: 'GenresDetail',
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
