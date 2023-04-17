<script lang="ts" setup>
import {
  ChartOptions,
  createChart,
  IChartApi,
  ISeriesApi,
  PriceScaleOptions,
  SeriesDataItemTypeMap,
  SeriesMarker,
  SeriesOptions,
  SeriesType,
  Time,
  TimeFormatterFn,
  TimeScaleOptions
} from 'lightweight-charts'
const props = withDefaults(
  defineProps<{
    type: SeriesType
    data: SeriesDataItemTypeMap[keyof SeriesDataItemTypeMap][]
    markers?: SeriesMarker<Time>[]
    chartOptions?: ChartOptions
    autosize?: boolean
    seriesOptions?: SeriesOptions<any>
    timeScaleOptions?: TimeScaleOptions
    priceScaleOptions?: PriceScaleOptions
  }>(),
  {
    // chartOptions: {  }
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
  <div class="h100%" style="height: 100%" ref="chartRef"></div>
</template>

<style scoped></style>
