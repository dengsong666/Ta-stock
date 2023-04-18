<script setup lang="ts">
import KChart from '@/components/Kchart.vue'
import { test_data, test_markers } from './test'
import 'uno.css'
const kChart = ref()
</script>

<template>
  <KChart type="Candlestick" :data="test_data" :markers="test_markers" :autosize="true" ref="kChart" />
</template>
<style scoped></style>
