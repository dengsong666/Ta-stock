<script setup lang="ts">
import screenfull from 'screenfull'
const indicator = reactive({
  value: [],
  options: ['KDJ', 'BOLL']
})
</script>

<template>
  <div class="flex-row items-center px24px h60px">
    <slot></slot>
    <n-checkbox-group v-model:value="indicator.value">
      <n-checkbox v-for="v in indicator.options" :value="v" :label="v" />
    </n-checkbox-group>
    <i @click="screenfull.toggle()" class="ml-auto i-my-full-screen"></i>
  </div>
</template>

<style lang="scss" scoped></style>
