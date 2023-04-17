<script setup lang="ts">
import { IChartApi } from 'lightweight-charts'

const { chart } = defineProps<{
  chart: IChartApi
}>()
const toolTipRef = ref()
const toolTip = reactive({
  visible: false,
  width: 80,
  height: 80,
  margin: 15
})
chart.subscribeCrosshairMove((param) => {
  if (
    param.point === undefined ||
    !param.time ||
    param.point.x < 0 ||
    param.point.x > chartRef.value.clientWidth ||
    param.point.y < 0 ||
    param.point.y > chartRef.value.clientHeight
  ) {
    toolTip.visible = false
  } else {
    // time will be in the same format that we supplied to setData.
    // thus it will be YYYY-MM-DD
    const dateStr = param.time
    toolTip.visible = true
    const data = param.seriesData.get(series!)
    const price = data!.value !== undefined ? data.value : data.close
    toolTipRef.value.innerHTML = `<div style="color: ${'#2962FF'}">Apple Inc.</div><div style="font-size: 24px; margin: 4px 0px; color: ${'black'}">
			${Math.round(100 * price) / 100}
			</div><div style="color: ${'black'}">
			${dateStr}
			</div>`

    const coordinate = series!.priceToCoordinate(price)
    let shiftedCoordinate = param.point.x - 50
    if (coordinate === null) {
      return
    }
    shiftedCoordinate = Math.max(0, Math.min(chartRef.value.clientWidth - toolTip.width, shiftedCoordinate))
    const coordinateY =
      coordinate - toolTip.height - toolTip.margin > 0
        ? coordinate - toolTip.height - toolTip.margin
        : Math.max(0, Math.min(chartRef.value.clientHeight - toolTip.height - toolTip.margin, coordinate + toolTip.margin))
    toolTipRef.value.style.left = shiftedCoordinate + 'px'
    toolTipRef.value.style.top = coordinateY + 'px'
  }
})
</script>

<template>
  <div v-show="toolTip.visible"></div>
</template>

<style lang="scss" scoped></style>
