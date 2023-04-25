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
  <div class="flex-row w100% p16px box-border absolute z100 c-#fff">
    <div class="grid-1-9-16">
      <span>日期：{{ kChart.crosshair?._internal_originalTime || '--' }}</span>
      <span>开盘：{{ kChart.crosshair?.open || '--' }}</span>
      <span>最高：{{ kChart.crosshair?.high || '--' }}</span>
      <span>最低：{{ kChart.crosshair?.low || '--' }}</span>
      <span>收盘：{{ kChart.crosshair?.close || '--' }}</span>
      <span>涨跌幅：{{ kChart.crosshair?.chgp || '--' }}%</span>
      <span>成交量：{{ kChart.crosshair?.vol || '--' }}万手</span>
    </div>
    <i class="mlauto i-my-select cursor-pointer"></i>
  </div>
</template>

<style lang="scss" scoped></style>
