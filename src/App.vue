<script setup lang="ts">
import Search from '@/components/Search.vue'
import KChart from '@/components/Kchart.vue'
import 'uno.css'
const data = ref([])
</script>

<template>
  <Search @index-day="data = $event" />
  <KChart type="Candlestick" :data="data" :markers="[]" />
</template>
<style lang="scss"></style>
