<template>
<div class="row file-wrapper">
  <div class="col-5">
    {{ file.name }}
  </div>
</div>
</template>

<script setup lang="ts">
defineProps({
  file: {
    type: Object,
    required: true
  }
})
</script>

<style lang="sass" scoped>
.file-wrapper
  border: 0.5px solid gray
  border-top: none
  min-height: 63px
  padding: 8px
  margin-right: 20px
</style>
