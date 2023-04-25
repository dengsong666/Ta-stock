<script setup lang="ts">
const visible = ref(false)
</script>

<template>
  <i class="i-my-stock" @click="visible = true"></i>
  <n-drawer v-model:show="visible" :default-width="500" resizable placement="left">
    <n-drawer-content title="自选"> </n-drawer-content>
  </n-drawer>
</template>

<style lang="scss" scoped></style>
