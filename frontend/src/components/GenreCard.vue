<template>
  <div class="card">
    <div class="card-body" @click="handleClick">
      <h5 class="card-title">{{ name }}</h5>
    </div>
  </div>
</template>
<script lang="ts">
export default {
  name: 'GenreCard',
  props: {
    genre: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      id: this.genre.id,
      name: this.genre.name,
    }
  },
  methods: {
    handleClick() {
      console.log('Card clicked')
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
