import { ChartOptions, PriceScaleOptions, SeriesOptions, SeriesOptionsMap, TimeScaleOptions } from 'lightweight-charts'
type DeepPartial<T> = Partial<{ [P in keyof T]: DeepPartial<T[P]> }>
export const color = {
  bg: '#1c1d21',
  up: '#ff3d3d',
  down: '#00a9b2'
}
export const chartOptions: DeepPartial<ChartOptions> = {
  layout: {
    background: { color: color.bg },
    textColor: '#DDD'
  },
  grid: {
    vertLines: { color: '#444' },
    horzLines: { color: '#444' }
  }
}
export const seriesOptions: DeepPartial<SeriesOptions<SeriesOptionsMap[keyof SeriesOptionsMap]>> = {
  color: '#2962FF',
  borderUpColor: color.up,
  wickUpColor: color.up,
  upColor: color.bg,
  borderDownColor: color.down,
  downColor: color.down,
  wickDownColor: color.down
}
export const timeScaleOptions: DeepPartial<TimeScaleOptions> = {}
export const priceScaleOptions: DeepPartial<PriceScaleOptions> = {}
