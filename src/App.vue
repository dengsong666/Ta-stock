<script setup lang="ts">
import screenfull from 'screenfull'
import 'uno.css'
const index = reactive({
  data: [],
  markers: []
})
function handleIndexDay(index_day: never[]) {
  index.data = index_day
  index.markers = index_day.map((item) => {
    const { time, close, bollLower, bollMiddle, bollUpper } = item as any
    const bollPB = (close - bollLower) / (bollUpper - bollLower)
    // console.log(close, bollLower, bollUpper)
    let marker
    if (bollPB < 0) {
      marker = {
        time,
        position: 'belowBar',
        color: '#2196F3',
        shape: 'arrowUp',
        text: '买'
      }
    }
    if (bollPB > 1) {
      marker = {
        time,
        position: 'aboveBar',
        color: '#e91e63',
        shape: 'arrowDown',
        text: '卖'
      }
    }
    return marker
  })
}
</script>

<template>
  <n-loading-bar-provider>
    <n-message-provider>
      <div class="flex-row items-center px24px h60px">
        <Search @index-day="handleIndexDay" />
        <i @click="screenfull.toggle()" class="ml-auto i-my-full-screen"></i>
      </div>
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
