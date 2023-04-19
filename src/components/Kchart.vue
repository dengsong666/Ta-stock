<script lang="ts" setup>
import { chartOptions, seriesOptions } from '@/configs'
import { useCommon } from '@/store'
import {
  ChartOptions,
  createChart,
  IChartApi,
  ISeriesApi,
  PriceScaleOptions,
  SeriesDataItemTypeMap,
  SeriesMarker,
  SeriesOptions,
  SeriesOptionsMap,
  SeriesType,
  Time,
  TimeScaleOptions
} from 'lightweight-charts'
import { getCurrentInstance } from 'vue'
const props = withDefaults(
  defineProps<{
    type: SeriesType
    data: SeriesDataItemTypeMap[keyof SeriesDataItemTypeMap][]
    markers?: SeriesMarker<Time>[]
    chartOptions?: DeepPartial<ChartOptions>
    autosize?: boolean
    seriesOptions?: DeepPartial<SeriesOptions<SeriesOptionsMap[keyof SeriesOptionsMap]>>
    timeScaleOptions?: DeepPartial<TimeScaleOptions>
    priceScaleOptions?: DeepPartial<PriceScaleOptions>
  }>(),
  {
    chartOptions: () => chartOptions,
    seriesOptions: () => seriesOptions
  }
)
let series: ISeriesApi<SeriesType> | null
let chart: IChartApi | null

const chartRef = ref()

const resizeHandler = () => {
  if (!chart || !chartRef.value) return
  const dimensions = chartRef.value.getBoundingClientRect()
  chart.resize(dimensions.width, dimensions.height)
}
onMounted(() => {
  const { data, markers, chartOptions, seriesOptions, priceScaleOptions, timeScaleOptions, autosize } = props
  chart = createChart(chartRef.value, chartOptions)
  useCommon().chart = chart as any
  series = chart![`add${props.type}Series`](seriesOptions)
  series.setData(data)
  markers && series.setMarkers(markers)
  priceScaleOptions && chart.priceScale('').applyOptions(priceScaleOptions)
  timeScaleOptions && chart.timeScale().applyOptions(timeScaleOptions)

  chart.timeScale().fitContent()
  autosize && window.addEventListener('resize', resizeHandler)
})

onUnmounted(() => {
  chart && chart.remove()
  chart = null
  series = null
  window.removeEventListener('resize', resizeHandler)
})

watch(
  () => props.autosize,
  (enabled) => (enabled ? window.addEventListener('resize', resizeHandler) : window.removeEventListener('resize', resizeHandler))
)

watch(
  () => props.data,
  (newData) => series && series.setData(newData)
)

watch(
  () => props.chartOptions,
  (newOptions) => chart && newOptions && chart.applyOptions(newOptions)
)

watch(
  () => props.seriesOptions,
  (newOptions) => series && series.applyOptions(newOptions)
)

watch(
  () => props.priceScaleOptions,
  (newOptions) => chart && newOptions && chart.priceScale('').applyOptions(newOptions)
)

watch(
  () => props.timeScaleOptions,
  (newOptions) => chart && newOptions && chart.timeScale().applyOptions(newOptions)
)
</script>

<template>
  <div class="h50%" ref="chartRef">
    <slot></slot>
  </div>
</template>

<style scoped></style>
