<template>
  <div class="card-group">
    <div class="card">
      <img class="card-img-top" src="..." alt="Card image cap" />
      <div class="card-body">
        <h5 class="card-title">{{ actor.name }}</h5>
        <p class="card-text">
          {{ actor.year }}
        </p>
        <!-- <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p> -->
      </div>
    </div>
  </div>
</template>
<script lang="ts">
export default {
  name: 'ActorCard',
  props: {
    actor: {
      type: Object,
      required: true,
    },
  },
}
</script>
