<script setup lang="ts">
import { IChartApi } from 'lightweight-charts'
import { ComponentInternalInstance } from 'vue'

const props = defineProps<{
  chart?: ComponentInternalInstance
}>()
console.log(props.chart)
onMounted(() => {
  if (props.chart) {
    console.log(props.chart)

    // props.chart.applyOptions({
    //   rightPriceScale: {
    //     scaleMargins: {
    //       top: 0.3,
    //       bottom: 0.25
    //     }
    //   },
    //   crosshair: {
    //     horzLine: {
    //       visible: false,
    //       labelVisible: false
    //     }
    //   },
    //   grid: {
    //     vertLines: {
    //       visible: false
    //     },
    //     horzLines: {
    //       visible: false
    //     }
    //   }
    // })

    // props.chart.subscribeCrosshairMove((param) => {
    //   console.log(param)
    // })
  }
})
</script>

<template>
  <div class="absolute left-12px z1"></div>
</template>

<style lang="scss" scoped></style>
