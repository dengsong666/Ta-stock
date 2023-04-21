<script setup lang="ts">
import 'uno.css'
const index = reactive({
  data: [],
  markers: []
})
</script>

<template>
  <n-loading-bar-provider>
    <n-message-provider>
      <Topbar><Search @index-day="" /></Topbar>
      <KChart type="Candlestick" :data="index.data" :markers="index.markers" autosize>
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
