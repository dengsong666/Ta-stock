<script setup lang="ts">
import 'uno.css'
const data = ref([])
</script>

<template>
  <Search @index-day="data = $event" />
  <KChart type="Candlestick" :data="data" :markers="[]">
    <KLegends />
  </KChart>
</template>
<style lang="scss"></style>
