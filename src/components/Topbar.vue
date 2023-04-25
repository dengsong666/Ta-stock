<script setup lang="ts">
import screenfull from 'screenfull'
const isFullscreen = ref(screenfull.isFullscreen)
// document.onkeyup = (e) => e.code == 'Escape' && screenfull.isFullscreen && (isFullscreen.value = true)
</script>

<template>
  <div class="flex-row items-center px24px h60px">
    <Filter />
    <Search v-bind="$attrs" />
    <span class="grid-1-2-8 mlauto">
      <i @click="screenfull.toggle(), (isFullscreen = !isFullscreen)" :class="`${isFullscreen ? 'i-my-full-screen-exit' : 'i-my-full-screen'}`"></i>
    </span>
  </div>
</template>

<style lang="scss" scoped></style>
