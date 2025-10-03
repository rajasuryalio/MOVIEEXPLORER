<template>
  <div class="section">
    <div class="actor-list">
      <ActorCard v-for="actor in actors" :key="actor.id" :actor="actor" />
    </div>
  </div>
</template>
<script lang="ts">
import axios from 'axios'
import ActorCard from './ActorCard.vue'
export default {
  name: 'ActorsDetail',
  components: { ActorCard },
  data() {
    return { actors: [] }
  },
  async mounted() {
    const actorsResponse = await axios.get('http://localhost:8888/actors')
    console.log(actorsResponse)
    this.actors = actorsResponse.data.objects
  },
}
</script>
<style>
.actor-list {
  display: grid;
  grid-template-columns: repeat(4, minmax(200px, 1fr));
  gap: 16px;
}
</style>
