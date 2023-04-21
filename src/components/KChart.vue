<script lang="ts" setup>
import { defaultChartOptions, defaultSeriesOptions } from '@/configs'
import { useKChart } from '@/store'
import { createChart, IChartApi, ISeriesApi, SeriesMarker, SeriesType, Time } from 'lightweight-charts'
const props = defineProps<{
  type: SeriesType
  data: ChartOption.Data
  chartOptions?: ChartOption.Base
  autosize?: boolean
  seriesOptions?: ChartOption.Series
  timeScaleOptions?: ChartOption.TimeScale
  priceScaleOptions?: ChartOption.PriceScale
}>()
const kChart = useKChart()
const { data, chartOptions, seriesOptions, priceScaleOptions, timeScaleOptions, autosize } = props
const options = reactive({
  chart: { ...defaultChartOptions, ...chartOptions, ...kChart.option.chart },
  series: { ...defaultSeriesOptions, ...seriesOptions, ...kChart.option.series }
})
let series: ISeriesApi<SeriesType> | null
let chart: IChartApi | null

const chartRef = ref()
const resizeHandler = () => {
  if (!chart || !chartRef.value) return
  const dimensions = chartRef.value.getBoundingClientRect()
  chart.resize(dimensions.width, dimensions.height)
}
onMounted(() => {
  chart = createChart(chartRef.value, options.chart)
  series = chart![`add${props.type}Series`](options.series)
  const lineSeries = chart.addLineSeries({ color: '#2962FF' })
  series.setData(data)
  // lineSeries.setData(data.map((item) => ({ time: item.time, value: item.bollLower })))
  // lineSeries.setData(data.map((item) => ({ time: item.time, value: item.bollUpper })))
  // console.log(lineSeries)
  chart.subscribeCrosshairMove((param) => {
    // param.time && (kChart.crosshair = param.seriesData.get(series!) as any)
    if (param.logical) {
      param.logical && (kChart.crosshair = kChart.list[param.logical] as any)
    }
  })
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
  (newData) => {
    if (series) {
      series.setData(newData)

      series.setMarkers(kChart.calculate(kChart.indicator, newData as any))
    }
  }
)
watch(
  () => kChart.indicator,
  (newData) => {
    series && series.setMarkers(kChart.calculate(newData, props.data as any))
  },
  { deep: true }
)

watch(
  () => props.chartOptions,
  (newOptions) => chart && newOptions && chart.applyOptions(newOptions)
)

watch(
  () => props.seriesOptions,
  (newOptions) => series && newOptions && series.applyOptions(newOptions)
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
  <div class="relative h-[calc(100%-60px)]" ref="chartRef">
    <slot></slot>
  </div>
</template>

<style scoped></style>
