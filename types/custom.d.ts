import { ChartOptions, SeriesDataItemTypeMap, SeriesOptions, SeriesOptionsMap, TimeScaleOptions, PriceScaleOptions } from 'lightweight-charts'

declare global {
  type DeepPartial<T> = Partial<{ [P in keyof T]: DeepPartial<T[P]> }>

  namespace ChartOption {
    type Base = DeepPartial<ChartOptions>
    type Data = SeriesDataItemTypeMap[keyof SeriesDataItemTypeMap][]
    type Series = DeepPartial<SeriesOptions<SeriesOptionsMap[keyof SeriesOptionsMap]>>
    type TimeScale = DeepPartial<TimeScaleOptions>
    type PriceScale = DeepPartial<PriceScaleOptions>
  }

  type AnyObj = { [key: string]: string }
}
