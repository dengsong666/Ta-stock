<script setup lang="ts">
import { useKChart } from '@/store'
const kChart = useKChart()
kChart.option.chart = {
  rightPriceScale: {
    scaleMargins: {
      top: 0.3,
      bottom: 0.25
    }
  },
  crosshair: {
    horzLine: {
      labelVisible: false
    }
  }
}
watch(kChart.crosshair, (val) => console.log(val))
</script>

<template>
  <div class="grid-1-9-16 absolute left-12px top-8px z2 c-#fff">
    <!-- <span>日期：{{ kChart.crosshair._internal_originalTime || '--' }}</span> -->
    <span>开盘：{{ kChart.crosshair.open || '--' }}</span>
    <span>最高：{{ kChart.crosshair.high || '--' }}</span>
    <span>最低：{{ kChart.crosshair.low || '--' }}</span>
    <span>收盘：{{ kChart.crosshair.close }}</span>
    <span>涨跌幅：{{ kChart.crosshair.changePct || '--' }}%</span>
    <span>成交量：{{ kChart.crosshair.tradingVol || '--' }}</span>
    <span>滚动市盈率{{ kChart.crosshair.peg || '--' }}</span>
  </div>
</template>

<style lang="scss" scoped></style>
