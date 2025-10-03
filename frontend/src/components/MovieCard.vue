<template>
  <div class="card">
    <div class="card-body" @click="handleClick">
      <h5 class="card-title">{{ title }}</h5>
      <p class="card-text">{{ year }}</p>
    </div>
  </div>
</template>
<script lang="ts">
export default {
  name: 'MovieCard',
  props: {
    movie: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      id: this.movie.id,
      title: this.movie.title,
      year: this.movie.year,
    }
  },
  methods: {
    handleClick() {
      console.log('Card clicked')
      console.log(this.id)
      console.log(this.title)
      console.log(this.year)
    },
  },
}
</script>
<style>
.card {
  cursor: pointer;
  transition: transform 0.2s;
}
.card:hover {
  transform: scale(1.05);
}
</style>
