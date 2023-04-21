<script setup lang="ts">
import 'uno.css'
import { useKChart } from './store'
const kchart = reactive({
  data: [],
  markers: []
})
</script>

<template>
  <n-loading-bar-provider>
    <n-message-provider>
      <Topbar @k-data="kchart.data = $event" />
      <KChart type="Candlestick" :data="kchart.data" autosize>
        <KLegends />
      </KChart>
    </n-message-provider>
  </n-loading-bar-provider>
</template>
<style lang="scss">
::-webkit-scrollbar {
  display: none;
}
</style>
